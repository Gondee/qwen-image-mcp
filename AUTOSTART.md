# 🚀 Auto-Start Configuration

This guide explains how to make the Qwen-Image MCP server start automatically with Claude Code.

## 📌 Important Note

**MCP servers registered with Claude Code already start automatically when Claude Code launches!** You typically don't need additional configuration. However, if you want the server to run as a system service or have issues with automatic startup, follow the guides below.

## 🍎 macOS

### Option 1: Claude Code Auto-Start (Recommended)
Once registered with `claude mcp add`, the server starts automatically when Claude Code launches. No additional setup needed.

### Option 2: Launch Agent (System-wide)
Create a Launch Agent to start the server at login:

1. Create the plist file:
```bash
nano ~/Library/LaunchAgents/com.qwen-image.mcp.plist
```

2. Add this content (adjust paths):
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.qwen-image.mcp</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>/path/to/qwen-image-mcp/server.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/tmp/qwen-image-mcp.err</string>
    <key>StandardOutPath</key>
    <string>/tmp/qwen-image-mcp.out</string>
</dict>
</plist>
```

3. Load the agent:
```bash
launchctl load ~/Library/LaunchAgents/com.qwen-image.mcp.plist
```

To stop: `launchctl unload ~/Library/LaunchAgents/com.qwen-image.mcp.plist`

## 🐧 Linux

### Option 1: Claude Code Auto-Start (Recommended)
Once registered with `claude mcp add`, the server starts automatically when Claude Code launches.

### Option 2: Systemd Service
Create a systemd service:

1. Create service file:
```bash
sudo nano /etc/systemd/system/qwen-image-mcp.service
```

2. Add this content:
```ini
[Unit]
Description=Qwen-Image MCP Server
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/path/to/qwen-image-mcp
ExecStart=/usr/bin/python3 /path/to/qwen-image-mcp/server.py
Restart=always
RestartSec=10
StandardOutput=append:/var/log/qwen-image-mcp.log
StandardError=append:/var/log/qwen-image-mcp-error.log

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
```bash
sudo systemctl daemon-reload
sudo systemctl enable qwen-image-mcp
sudo systemctl start qwen-image-mcp
```

Check status: `sudo systemctl status qwen-image-mcp`

### Option 3: Cron Job
Add to your crontab:
```bash
crontab -e
```

Add this line:
```bash
@reboot /usr/bin/python3 /path/to/qwen-image-mcp/server.py >> /tmp/qwen-mcp.log 2>&1
```

## 🪟 Windows

### Option 1: Claude Code Auto-Start (Recommended)
Once registered with `claude mcp add`, the server starts automatically when Claude Code launches.

### Option 2: Task Scheduler

1. Open Task Scheduler (taskschd.msc)
2. Create Basic Task → Name it "Qwen-Image MCP"
3. Trigger: "When I log on"
4. Action: "Start a program"
5. Program: `C:\Python311\python.exe` (your Python path)
6. Arguments: `C:\path\to\qwen-image-mcp\server.py`
7. Start in: `C:\path\to\qwen-image-mcp`
8. Finish and test

### Option 3: Startup Folder
Create a batch file:

1. Create `start-qwen-mcp.bat`:
```batch
@echo off
cd C:\path\to\qwen-image-mcp
python server.py
```

2. Place in Startup folder:
   - Press `Win + R`, type `shell:startup`
   - Copy the batch file there

### Option 4: Windows Service
Using NSSM (Non-Sucking Service Manager):

1. Download NSSM: https://nssm.cc/download
2. Install service:
```cmd
nssm install QwenImageMCP "C:\Python311\python.exe" "C:\path\to\qwen-image-mcp\server.py"
nssm set QwenImageMCP AppDirectory "C:\path\to\qwen-image-mcp"
nssm set QwenImageMCP DisplayName "Qwen-Image MCP Server"
nssm set QwenImageMCP Start SERVICE_AUTO_START
```

3. Start service:
```cmd
nssm start QwenImageMCP
```

## 🐋 Docker (All Platforms)

Create a Docker container that auto-starts:

1. Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "server.py"]
```

2. Build and run:
```bash
docker build -t qwen-image-mcp .
docker run -d --restart=always --name qwen-mcp qwen-image-mcp
```

## ✅ Verify Auto-Start

After setting up auto-start:

1. Reboot your system
2. Open Claude Code
3. Check if the server is connected: `/mcp` command
4. Try generating an image

## 🔧 Troubleshooting Auto-Start

### Server not starting automatically:
- Check Claude Code's MCP configuration: `claude mcp list`
- Verify Python path is correct
- Check logs for errors

### Permission issues:
- Ensure the script has execute permissions: `chmod +x server.py`
- Run with your user account, not root

### Port conflicts:
- MCP servers use stdio, not network ports, so conflicts are rare
- Check if another instance is running: `ps aux | grep qwen-image`

## 💡 Tips

1. **Claude Code Integration**: The simplest approach is using Claude Code's built-in MCP management
2. **Resource Usage**: The model loads on-demand, so auto-start doesn't consume GPU/RAM until first use
3. **Logging**: Always configure logging when using auto-start to debug issues
4. **Updates**: Remember to restart the service after updating the server code

## 🎯 Recommended Approach

For most users, the Claude Code automatic management (Option 1 on each platform) is sufficient. The server will:
- Start when Claude Code launches
- Stop when Claude Code closes
- Restart automatically if it crashes
- Not consume resources when idle

Only use system-level auto-start if you need the server running independently of Claude Code.