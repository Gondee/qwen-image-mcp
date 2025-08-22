#!/usr/bin/env python3
"""
Installation helper for Qwen-Image MCP Server
Handles cross-platform Claude Code registration
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import shutil

def get_server_command():
    """Get the appropriate command to run the server."""
    server_path = Path(__file__).parent / "server.py"
    python_cmd = sys.executable
    return [python_cmd, str(server_path)]

def check_claude_command():
    """Check if claude command is available."""
    if shutil.which("claude") is None:
        print("❌ 'claude' command not found.")
        print("   Please ensure Claude Code is installed and the 'claude' command is in your PATH.")
        return False
    return True

def register_with_claude():
    """Register the MCP server with Claude Code."""
    if not check_claude_command():
        return False
    
    print("\n📝 Registering Qwen-Image MCP server with Claude Code...")
    
    server_path = Path(__file__).parent / "server.py"
    python_cmd = sys.executable
    
    # Build the claude mcp add command
    cmd = [
        "claude", "mcp", "add", 
        "--scope", "user",
        "qwen-image",
        python_cmd,
        "--",
        str(server_path)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Successfully registered with Claude Code!")
            print("\n📋 Next steps:")
            print("   1. Restart Claude Code or run '/mcp' command")
            print("   2. The server will be available as 'qwen-image'")
            print("   3. First run will download the model (~20GB)")
            return True
        else:
            print(f"❌ Failed to register: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Error during registration: {e}")
        return False

def install_dependencies():
    """Install Python dependencies."""
    print("📦 Installing Python dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            check=True
        )
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        print("\nYou can manually install with:")
        print(f"  pip install -r {requirements_file}")
        return False

def main():
    """Main installation process."""
    print("=" * 60)
    print("🎨 Qwen-Image MCP Server Installer")
    print("=" * 60)
    
    # Check Python version
    if sys.version_info < (3, 10):
        print(f"❌ Python 3.10+ required (you have {sys.version})")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Install dependencies
    print("\nStep 1: Installing dependencies...")
    if not install_dependencies():
        print("\n⚠️  Dependency installation failed, but continuing...")
    
    # Register with Claude Code
    print("\nStep 2: Registering with Claude Code...")
    if register_with_claude():
        print("\n🎉 Installation complete!")
    else:
        print("\n⚠️  Automatic registration failed.")
        print("\nManual registration:")
        server_path = Path(__file__).parent / "server.py"
        print(f"  claude mcp add --scope user qwen-image {sys.executable} -- {server_path}")
    
    # Print usage information
    print("\n" + "=" * 60)
    print("📖 Usage Information:")
    print("=" * 60)
    print("\nIn Claude Code, you can generate images by asking:")
    print('  "Generate an image of a sunset over mountains"')
    print('  "Create a portrait of a happy golden retriever"')
    print("\nThe model excels at:")
    print("  • High-fidelity text rendering")
    print("  • Multiple artistic styles")
    print("  • Photorealistic imagery")
    print("  • Complex scene composition")
    
    print("\n⚠️  Note: First generation will download the model (~20GB)")
    print("   This is a one-time download that will be cached locally.")

if __name__ == "__main__":
    main()