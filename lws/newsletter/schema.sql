-- AI Press Review — subscriber schema (LWS Perso MySQL)
--
-- Run ONCE via phpMyAdmin on your LWS-provided database:
--   1. Log into your LWS panel, open phpMyAdmin for the database
--      (named something like lwsXXXXXX_newsletter).
--   2. Click the database in the left sidebar.
--   3. Open the "SQL" tab.
--   4. Paste this whole file, click "Execute".
--
-- The table uses utf8mb4 so names/emails with emoji, accents, or any
-- non-BMP characters round-trip correctly. InnoDB is the default
-- engine on LWS MySQL 5.7+/8.x so UNIQUE constraints and transactions
-- behave as expected.
--
-- The ~200-byte row size × 1000 subscribers = ~200 KB total — well
-- below the 1 GB per-DB quota of the Perso plan.

CREATE TABLE IF NOT EXISTS `subscribers` (
  `id`                INT UNSIGNED NOT NULL AUTO_INCREMENT,

  -- RFC 5321 caps total email length at 254 (64 local + @ + 255 domain,
  -- practical limit 254). VARCHAR(254) + UNIQUE gives us dedup for free.
  `email`             VARCHAR(254) NOT NULL,

  -- 'en' or 'fr' today; leave room for 'es'/'de'/… later without schema change.
  `locale`            VARCHAR(8)   NOT NULL DEFAULT 'en',

  `created_at`        TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,

  -- 1 = user is receiving the newsletter.
  -- Flip to 0 + require token click if/when we wire double opt-in.
  `confirmed`         TINYINT(1)   NOT NULL DEFAULT 1,

  -- Nullable: only populated in the double-opt-in path.
  `confirm_token`     VARCHAR(64)  NULL,

  -- Always populated on INSERT. Users click a link like
  --   https://aequitus.net/api/unsubscribe.php?t=<token>
  -- to self-remove without authenticating.
  `unsubscribe_token` VARCHAR(64)  NOT NULL,

  -- SHA-256(salt + REMOTE_ADDR), truncated to 32 hex chars.
  -- Non-reversible; stored only for (a) the 60s per-IP rate limit and
  -- (b) GDPR Art. 7 "proof of affirmative action". Never logs the
  -- raw IP.
  `ip_hash`           CHAR(32)     NULL,

  -- Truncated to 300 chars in PHP. Also GDPR Art. 7 evidence.
  `user_agent`        VARCHAR(300) NULL,

  -- Exact wording the user agreed to, in their locale. Stored per-row
  -- so if the consent text ever changes, historical proof stays intact.
  `consent_text`      TEXT         NULL,

  -- 'web' for the form; reserved for 'import', 'api', etc. later.
  `source`            VARCHAR(16)  NOT NULL DEFAULT 'web',

  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_email`             (`email`),
  UNIQUE KEY `uq_unsubscribe_token` (`unsubscribe_token`),
  UNIQUE KEY `uq_confirm_token`     (`confirm_token`),
  KEY `idx_locale`     (`locale`),
  KEY `idx_created_at` (`created_at`),
  KEY `idx_ip_hash`    (`ip_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Optional: audit trail for unsubscribes, useful for debugging
-- "why did X disappear from my list?" 6 months later. Keep it tiny.
CREATE TABLE IF NOT EXISTS `unsubscribe_log` (
  `id`         INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `email_hash` CHAR(32)     NOT NULL,           -- sha256(salt + email), 32 hex
  `reason`     VARCHAR(64)  NULL,               -- 'user-click', 'bounce', 'manual'
  `created_at` TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `idx_email_hash` (`email_hash`),
  KEY `idx_created_at` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
