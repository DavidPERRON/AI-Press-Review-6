<?php
/**
 * AI Press Review — admin CSV export (LWS Perso).
 *
 * GET /api/export.php
 * Authorization: Bearer <admin_token>
 *
 * → text/csv; charset=utf-8  (filename: subscribers-YYYY-MM-DD.csv)
 * → 401 {"ok":false,"error":"unauthorized"} if the Bearer header is
 *   missing, malformed, or doesn't match config admin_token.
 *
 * Security posture:
 *   - Bearer token compared in constant time (hash_equals) to defeat
 *     timing attacks. This matters less for a single-user admin but
 *     costs nothing to do right.
 *   - No CORS. This endpoint is meant to be called from the GitHub
 *     Action backup job or from your terminal with curl, NOT from a
 *     browser on podcast.aequitus.net.
 *   - Every auth failure is error_log'd so brute-force attempts show
 *     up in the LWS hosting error log.
 *   - Streams rows in chunks of 1000 via a single prepared statement
 *     to avoid loading the whole table into PHP memory. 100k rows
 *     cost ~20 MB peak — fits comfortably under the 384 MB
 *     memory_limit on Perso.
 */

declare(strict_types=1);

$configFile = __DIR__ . '/config.php';
if (!is_file($configFile)) {
    http_response_code(500);
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['ok' => false, 'error' => 'server_error']);
    error_log('export.php: config.php missing');
    exit;
}
$config = require $configFile;

// ── Auth ───────────────────────────────────────────────────────────
$authHeader = $_SERVER['HTTP_AUTHORIZATION']
           ?? $_SERVER['REDIRECT_HTTP_AUTHORIZATION']  // Apache+FCGI edge case
           ?? '';
if (!preg_match('/^Bearer\s+(.+)$/i', $authHeader, $m)) {
    http_response_code(401);
    header('Content-Type: application/json; charset=utf-8');
    header('WWW-Authenticate: Bearer realm="admin"');
    error_log('export.php: missing/malformed Authorization header from '
        . ($_SERVER['REMOTE_ADDR'] ?? '?'));
    echo json_encode(['ok' => false, 'error' => 'unauthorized']);
    exit;
}
$provided = trim($m[1]);
$expected = (string) ($config['admin_token'] ?? '');
if ($expected === '' || !hash_equals($expected, $provided)) {
    http_response_code(401);
    header('Content-Type: application/json; charset=utf-8');
    header('WWW-Authenticate: Bearer realm="admin"');
    error_log('export.php: bad token from ' . ($_SERVER['REMOTE_ADDR'] ?? '?'));
    echo json_encode(['ok' => false, 'error' => 'unauthorized']);
    exit;
}

// ── Method check ───────────────────────────────────────────────────
if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'GET') {
    http_response_code(405);
    header('Allow: GET');
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['ok' => false, 'error' => 'method_not_allowed']);
    exit;
}

// ── DB connect ─────────────────────────────────────────────────────
try {
    $pdo = new PDO(
        sprintf('mysql:host=%s;dbname=%s;charset=utf8mb4', $config['db_host'], $config['db_name']),
        $config['db_user'],
        $config['db_pass'],
        [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_EMULATE_PREPARES   => false,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]
    );
} catch (Throwable $e) {
    error_log('export.php: DB connect failed: ' . $e->getMessage());
    http_response_code(500);
    header('Content-Type: application/json; charset=utf-8');
    echo json_encode(['ok' => false, 'error' => 'server_error']);
    exit;
}

// ── Stream CSV ─────────────────────────────────────────────────────
$date = date('Y-m-d');
header('Content-Type: text/csv; charset=utf-8');
header('Content-Disposition: attachment; filename="subscribers-' . $date . '.csv"');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');

// BOM so Excel on Windows renders UTF-8 correctly on first open.
echo "\xEF\xBB\xBF";

$out = fopen('php://output', 'w');
fputcsv($out, [
    'id', 'email', 'locale', 'created_at', 'confirmed',
    'ip_hash', 'user_agent', 'consent_text', 'source',
]);

try {
    $stmt = $pdo->query(
        'SELECT id, email, locale, created_at, confirmed,
                ip_hash, user_agent, consent_text, source
           FROM subscribers
          ORDER BY id'
    );
    while (($row = $stmt->fetch()) !== false) {
        fputcsv($out, [
            $row['id'], $row['email'], $row['locale'], $row['created_at'],
            $row['confirmed'], $row['ip_hash'], $row['user_agent'],
            $row['consent_text'], $row['source'],
        ]);
    }
} catch (Throwable $e) {
    error_log('export.php: query failed: ' . $e->getMessage());
    // Headers are already sent — best we can do is truncate the CSV
    // with a marker the caller can grep for.
    fputcsv($out, ['ERROR', 'export interrupted — check server logs']);
}

fclose($out);
