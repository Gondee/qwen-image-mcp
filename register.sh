#!/bin/bash
# Cross-platform registration script for Qwen-Image MCP Server

set -e

echo "======================================"
echo "🎨 Qwen-Image MCP Registration"
echo "======================================"

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SERVER_PATH="$SCRIPT_DIR/qwen_image_mcp/server.py"

# Find Python executable
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "❌ Python not found. Please install Python 3.10+"
    exit 1
fi

echo "✅ Using Python: $PYTHON_CMD"
echo "✅ Server path: $SERVER_PATH"

# Check if claude command exists
if ! command -v claude &> /dev/null; then
    echo "❌ 'claude' command not found."
    echo "   Please ensure Claude Code is installed and in PATH"
    exit 1
fi

# Remove existing registration if present
echo ""
echo "📝 Removing any existing registration..."
claude mcp remove qwen-image 2>/dev/null || true

# Register the server
echo "📝 Registering Qwen-Image server..."
if claude mcp add --scope user qwen-image "$PYTHON_CMD" -- "$SERVER_PATH"; then
    echo ""
    echo "✅ Successfully registered!"
    echo ""
    echo "Next steps:"
    echo "1. Restart Claude Code or run '/mcp' command"
    echo "2. Generate images by asking Claude"
    echo ""
    echo "Example prompts:"
    echo '  "Generate an image of a sunset"'
    echo '  "Create a portrait of a cat"'
else
    echo "❌ Registration failed"
    echo ""
    echo "Try manual registration:"
    echo "  claude mcp add --scope user qwen-image $PYTHON_CMD -- $SERVER_PATH"
    exit 1
fi