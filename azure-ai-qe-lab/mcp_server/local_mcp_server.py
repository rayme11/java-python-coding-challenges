import http.server
import socketserver
import json
import sqlite3
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

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
    cursor.execute("SELECT COUNT(*) FROM test_metrics")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('AuthService', 98.5, 0)")
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('CheckoutAPI', 91.2, 2)")
        cursor.execute("INSERT INTO test_metrics (component, pass_rate, open_bugs) VALUES ('UI-Dashboard', 85.0, 5)")
        conn.commit()
    conn.close()

class VerboseMCPInspectorHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override default logging to provide clean, structured console inspector logs
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [MCP INSPECTOR LOG] {format % args}")

    def do_GET(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n{'='*70}")
        print(f"[{timestamp}] 📥 INCOMING MCP PROMPT / TOOL REQUEST")
        print(f"Path: {self.path}")
        print(f"Headers:\n{self.headers}")
        print(f"{'='*70}")

        if self.path.startswith("/mcp/tools/get_test_metrics"):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT component, pass_rate, open_bugs FROM test_metrics")
            rows = cursor.fetchall()
            conn.close()
            
            metrics = [{"component": r[0], "pass_rate": r[1], "open_bugs": r[2]} for r in rows]
            response_data = {
                "mcp_protocol_version": "1.0",
                "server_status": "active",
                "tools_executed": "get_test_metrics",
                "data": metrics
            }

            response_body = json.dumps(response_data, indent=2)
            
            print(f"[{timestamp}] 📤 OUTGOING MCP TOOL RESPONSE:")
            print(response_body)
            print(f"{'='*70}\n")

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response_body.encode())
        else:
            print(f"[{timestamp}] ❌ MCP Tool Not Found: {self.path}")
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"MCP Tool Not Found")

if __name__ == "__main__":
    init_db()
    print(f"\n[Verbose Local MCP Inspector Server]")
    print(f"Listening on: http://localhost:{PORT}")
    print(f"Available Tool Endpoint: http://localhost:{PORT}/mcp/tools/get_test_metrics")
    print(f"All incoming agent prompts, tool calls, and JSON payloads will be logged below in real-time...\n")
    
    with socketserver.TCPServer(("", PORT), VerboseMCPInspectorHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[Local MCP Server] Shutting down inspector...")
