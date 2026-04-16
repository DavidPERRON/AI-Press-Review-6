<?php
/**
 * Liveness + DB probe. Useful for the GH Action backup job to verify
 * the server is up before the curl on export.php, and for you to
 * confirm your deploy worked with a single GET.
 *
 * GET /api/health.php  →  200  {"ok":true,"ts":"2026-…","db":true}
 *                      →  500  {"ok":false,"error":"..."}
 *
 * Does NOT require authentication — it reveals nothing useful beyond
 * "the stack is alive". It does open a DB connection to validate the
 * MySQL path, then closes it. Keep this lightweight.
 */

declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

$configFile = __DIR__ . '/config.php';
if (!is_file($configFile)) {
    http_response_code(500);
    echo json_encode(['ok' => false, 'error' => 'config_missing']);
    exit;
}
$config = require $configFile;

$dbOk = false;
try {
    $pdo = new PDO(
        sprintf('mysql:host=%s;dbname=%s;charset=utf8mb4', $config['db_host'], $config['db_name']),
        $config['db_user'],
        $config['db_pass'],
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_TIMEOUT => 3]
    );
    $dbOk = (bool) $pdo->query('SELECT 1')->fetchColumn();
} catch (Throwable $e) {
    error_log('health.php: ' . $e->getMessage());
}

echo json_encode([
    'ok' => $dbOk,
    'ts' => gmdate('c'),
    'db' => $dbOk,
]);
