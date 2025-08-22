"""Qwen-Image MCP Server - Local image generation for Claude Code."""

import sys
import subprocess
from pathlib import Path
from .server import app

def main():
    """Run the MCP server."""
    app.run()

def register():
    """Register the server with Claude Code."""
    print("🎨 Registering Qwen-Image MCP with Claude Code...")
    
    # Get the module path
    import qwen_image_mcp
    server_module = qwen_image_mcp.__file__.replace("__init__.py", "server.py")
    
    cmd = [
        "claude", "mcp", "add",
        "--scope", "user",
        "qwen-image",
        sys.executable,
        "--", server_module
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Successfully registered!")
            print("\nNext steps:")
            print("1. Restart Claude Code or run '/mcp'")
            print("2. Generate images by asking Claude")
        else:
            print(f"❌ Registration failed: {result.stderr}")
            print(f"\nTry manually: claude mcp add --scope user qwen-image {sys.executable} -- {server_module}")
    except FileNotFoundError:
        print("❌ 'claude' command not found. Is Claude Code installed?")
        print(f"\nManual command: claude mcp add --scope user qwen-image {sys.executable} -- {server_module}")

__all__ = ['main', 'register', 'app']