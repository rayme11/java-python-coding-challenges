import http.server
import socketserver
import json
import sqlite3
import os

PORT = int(os.getenv("LOCAL_MCP_SERVER_PORT", 8000))
DB_PATH = "test_metrics.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            component TEXT,
            pass_rate REAL,
            open_bugs INTEGER,
            last_run TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # Insert seed data if empty
    cursor.execute("SELECT COUNT(*) FROM test_metrics")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('AuthService', 98.5, 0)")
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('CheckoutAPI', 91.2, 2)")
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('UI-Dashboard', 85.0, 5)")
        conn.commit()
    conn.close()

class MCPToolHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/mcp/tools/get_test_metrics":
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT component, pass_rate, open_bugs FROM test_metrics")
            rows = cursor.fetchall()
            conn.close()
            
            metrics = [{"component": r[0], "pass_rate": r[1], "open_bugs": r[2]} for r in rows]
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"mcp_protocol_version": "1.0", "tools_executed": "get_test_metrics", "data": metrics}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    init_db()
    print(f"[Local MCP Server] Starting Model Context Protocol server on port {PORT}...")
    print(f"[Local MCP Server] Endpoints available: http://localhost:{PORT}/mcp/tools/get_test_metrics")
    with socketserver.TCPServer(("", PORT), MCPToolHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Local MCP Server] Shutting down...")
