#!/usr/bin/env python3
"""fanbom — ローカルサーバー起動スクリプト"""
import http.server
import socketserver
import webbrowser
import os

PORT = 8765
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)
    def log_message(self, fmt, *args):
        pass  # 静かに

print(f"\n  🎬 fanbom が起動しました")
print(f"  ブラウザで開く: http://localhost:{PORT}\n")
print("  終了するには Ctrl+C を押してください\n")

webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n  fanbom を終了しました。")
