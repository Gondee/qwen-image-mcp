#!/usr/bin/env python3
"""Entry point for qwen-image-mcp when run as a module."""

from .server import app

if __name__ == "__main__":
    app.run()