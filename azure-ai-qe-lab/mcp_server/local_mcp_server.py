import sys
import json
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "test_metrics.db")

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

def get_test_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT component, pass_rate, open_bugs FROM test_metrics")
    rows = cursor.fetchall()
    conn.close()
    return [{"component": r[0], "pass_rate": r[1], "open_bugs": r[2]} for r in rows]

def handle_jsonrpc():
    init_db()
    # Simple JSON-RPC over STDIO handler for MCP Inspector
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            req_id = request.get("id")
            method = request.get("method")
            
            # MCP Protocol Handshaking & Tool listing
            if method == "initialize":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "enterprise-qe-mcp-server", "version": "1.0.0"}
                    }
                }
            elif method == "tools/list":
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [
                            {
                                "name": "get_test_metrics",
                                "description": "Retrieve enterprise component test pass rates and open bug counts.",
                                "inputSchema": {"type": "object", "properties": {}}
                            }
                        ]
                    }
                }
            elif method == "tools/call":
                params = request.get("params", {})
                tool_name = params.get("name")
                if tool_name == "get_test_metrics":
                    metrics = get_test_metrics()
                    response = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "result": {
                            "content": [
                                {
                                    "type": "text",
                                    "text": json.dumps(metrics, indent=2)
                                }
                            ]
                        }
                    }
                else:
                    response = {
                        "jsonrpc": "2.0",
                        "id": req_id,
                        "error": {"code": -32601, "message": f"Tool not found: {tool_name}"}
                    }
            else:
                response = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32601, "message": f"Method not found: {method}"}
                }
            
            sys.stdout.write(json.dumps(response) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)}
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    handle_jsonrpc()
