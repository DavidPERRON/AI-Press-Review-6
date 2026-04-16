<?php
/**
 * AI Press Review — self-service unsubscribe (LWS Perso).
 *
 * GET /api/unsubscribe.php?t=<unsubscribe_token>
 *
 * On match: deletes the row (subscribers table) and writes a hashed
 * audit trail to unsubscribe_log. Returns a minimal HTML confirmation
 * page (FR+EN on a single page — the user's locale was already set by
 * the newsletter link they clicked through).
 *
 * On miss: same visual response as a successful unsubscribe. Don't
 * leak whether the token exists. This is enumeration-resistant.
 *
 * Usage in newsletter footer:
 *   EN: <a href="https://aequitus.net/api/unsubscribe.php?t={{unsub_token}}">Unsubscribe</a>
 *   FR: <a href="https://aequitus.net/api/unsubscribe.php?t={{unsub_token}}">Se désinscrire</a>
 */

declare(strict_types=1);

$configFile = __DIR__ . '/config.php';
if (!is_file($configFile)) {
    http_response_code(500);
    error_log('unsubscribe.php: config.php missing');
    exit;
}
$config = require $configFile;

$token = isset($_GET['t']) ? trim((string) $_GET['t']) : '';
// 48 hex chars (24 bytes). Reject anything that doesn't look like our
// format before touching the DB.
$validFormat = (bool) preg_match('/^[a-f0-9]{48}$/', $token);

$deleted = false;
if ($validFormat) {
    try {
        $pdo = new PDO(
            sprintf('mysql:host=%s;dbname=%s;charset=utf8mb4', $config['db_host'], $config['db_name']),
            $config['db_user'],
            $config['db_pass'],
            [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_EMULATE_PREPARES => false,
            ]
        );

        // Fetch-then-delete so we can log the hashed email for audit.
        $sel = $pdo->prepare(
            'SELECT email FROM subscribers WHERE unsubscribe_token = :t LIMIT 1'
        );
        $sel->execute([':t' => $token]);
        $row = $sel->fetch(PDO::FETCH_ASSOC);

        if ($row) {
            $pdo->beginTransaction();

            $del = $pdo->prepare('DELETE FROM subscribers WHERE unsubscribe_token = :t');
            $del->execute([':t' => $token]);

            $emailHash = substr(
                hash('sha256', ($config['ip_hash_salt'] ?? '') . '|' . $row['email']),
                0,
                32
            );
            $log = $pdo->prepare(
                'INSERT INTO unsubscribe_log (email_hash, reason) VALUES (:h, :r)'
            );
            $log->execute([':h' => $emailHash, ':r' => 'user-click']);

            $pdo->commit();
            $deleted = true;
        }
    } catch (Throwable $e) {
        error_log('unsubscribe.php: ' . $e->getMessage());
        // Fall through to the generic confirmation page.
    }
}

// Always return the same visible response (even on bad/unknown token).
http_response_code(200);
header('Content-Type: text/html; charset=utf-8');
header('Cache-Control: no-store');
?><!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Unsubscribed — AI Press Review</title>
<style>
  :root{--bg:#01040F;--ink:#F4ECDC;--ink-soft:#C5BAA0;--gold:#D9A24A;--rule:rgba(217,162,74,.25)}
  *{box-sizing:border-box}html,body{margin:0;padding:0}
  body{font-family:'EB Garamond','Garamond',Georgia,serif;background:var(--bg);color:var(--ink);
       line-height:1.6;font-size:18px;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:2rem}
  .card{max-width:540px;text-align:center;padding:2.4rem 2rem;border:1px solid var(--rule);border-radius:8px}
  h1{font-variant:small-caps;letter-spacing:.18em;color:var(--gold);font-size:1.2rem;margin:0 0 1rem}
  p{margin:0 0 .8rem;color:var(--ink-soft)}
  a{color:var(--gold);border-bottom:1px solid var(--gold)}
  hr{border:0;border-top:1px solid var(--rule);margin:1.6rem 0}
</style>
</head>
<body>
  <div class="card">
    <h1>Unsubscribed</h1>
    <p>You're no longer on the AI Press Review mailing list. If you ever change your mind,
       the <a href="https://podcast.aequitus.net/">home page</a> has a signup form.</p>
    <hr>
    <h1>Désinscription effectuée</h1>
    <p>Vous ne recevrez plus la lettre d'information de la Revue de Presse IA.
       Si vous changez d'avis, la <a href="https://podcast.aequitus.net/fr/">page d'accueil</a>
       contient un formulaire d'inscription.</p>
  </div>
</body>
</html>
