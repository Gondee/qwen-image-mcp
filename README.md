# 🎨 Qwen-Image MCP Server

A Model Context Protocol (MCP) server that enables Claude Code to generate images locally using the state-of-the-art Qwen-Image model.

## 🚀 One-Line Install

```bash
uvx --from git+https://github.com/Gondee/qwen-image-mcp.git qwen-image-mcp-register
```

That's it! Restart Claude Code and start generating images locally.

## ✨ Features

- **Local Generation**: Run entirely on your machine - no API keys or cloud services required
- **High-Quality Output**: Powered by Qwen-Image, a 20B parameter model with exceptional capabilities
- **Text Rendering**: Superior text rendering in images (especially for Chinese and English)
- **Multiple Styles**: Support for photorealistic, artistic, anime, and various other styles
- **Cross-Platform**: Works on macOS, Linux, and Windows with CUDA support

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Claude Code with MCP support
- 20GB free disk space for model download (first run only)
- Recommended: GPU with 8GB+ VRAM (works on CPU but slower)

### ⚠️ Important: Automatic Model Download

**The Qwen-Image model (~20GB) will download automatically on your first image generation.** This is a one-time download that will be cached for all future use. The first image generation will take 5-15 minutes depending on your internet speed. Subsequent generations will only take 30-60 seconds.

## 🎯 Installation Options

### Option 1: One-Line Install with uvx (Simplest)

```bash
# Install and register with Claude Code in one command
uvx --from git+https://github.com/Gondee/qwen-image-mcp.git qwen-image-mcp-register

# Or with pipx
pipx run --spec git+https://github.com/Gondee/qwen-image-mcp.git qwen-image-mcp-register
```

That's it! Restart Claude Code and start generating images.

### Option 2: Install with pip/uv

```bash
# Using uv
uv pip install git+https://github.com/Gondee/qwen-image-mcp.git

# Or using pip
pip install git+https://github.com/Gondee/qwen-image-mcp.git

# Then register with Claude Code
qwen-image-mcp-register
```

### Option 3: Clone and Install

1. **Clone the repository:**
```bash
git clone https://github.com/Gondee/qwen-image-mcp.git
cd qwen-image-mcp
```

2. **Run the installer:**
```bash
python install.py
```

### Option 4: Manual Registration

If automatic registration doesn't work:

```bash
# Find where the server is installed
python -c "import qwen_image_mcp; print(qwen_image_mcp.__file__)"

# Register with Claude Code (adjust path from above)
claude mcp add --scope user qwen-image python /path/to/qwen_image_mcp/server.py
```

After any installation method, restart Claude Code or run `/mcp` command.

## 💬 Usage in Claude Code

Once installed, you can generate images by simply asking Claude:

```
"Generate an image of a majestic mountain landscape at sunset"
"Create a portrait of a happy golden retriever in a garden"
"Make an image with the text 'Welcome' in elegant typography"
```

### Parameters You Can Specify

- **Size**: "512x512", "768x768", "1024x1024", "portrait", "landscape"
- **Steps**: Number of generation steps (20-100, default 50)
- **Guidance**: CFG scale (1.0-10.0, default 4.0)
- **Seed**: For reproducible results

Example with parameters:
```
"Generate a 1024x1024 image of a tropical beach, 
use 60 steps and guidance 5.0"
```

## 🎯 Model Capabilities

Qwen-Image excels at:

- **Text Rendering**: Accurately renders text in multiple languages
- **Photorealistic Images**: High-quality realistic imagery
- **Artistic Styles**: From oil paintings to anime aesthetics
- **Complex Compositions**: Multi-element scenes with proper relationships
- **Detail Preservation**: Maintains fine details even in complex scenes

## 🛠️ Configuration

### Environment Variables

- `HF_HOME`: Cache directory for model downloads (optional)
- `CUDA_VISIBLE_DEVICES`: GPU selection for multi-GPU systems

### Output Directory

By default, images are saved to:
- macOS/Linux: `~/Pictures/qwen_images/`
- Windows: `%USERPROFILE%\Pictures\qwen_images\`

## 📊 System Requirements

### Minimum
- CPU: Any modern x86_64 or ARM64 processor
- RAM: 16GB
- Storage: 25GB free space

### Recommended
- GPU: NVIDIA GPU with 8GB+ VRAM or Apple Silicon with 16GB+ unified memory
- RAM: 32GB
- Storage: 50GB free space (for model and generated images)

## ⚙️ Auto-Start Configuration

The MCP server starts automatically when Claude Code launches after registration. For additional auto-start options or system-service configuration, see [AUTOSTART.md](AUTOSTART.md).

## 🔧 Troubleshooting

### Server not connecting
```bash
# Check if server runs standalone
python server.py

# Re-register with Claude Code
claude mcp remove qwen-image
claude mcp add --scope user qwen-image python /path/to/server.py
```

### Out of memory errors
- Reduce image size (try 512x512 or 768x768)
- Close other applications
- Consider using CPU mode (slower but uses system RAM)

### Black/corrupted images
- Ensure model downloaded completely
- Check you have latest version of diffusers
- Try reinstalling: `pip install --upgrade diffusers transformers`

### First run is slow
- **This is normal!** The model downloads automatically on first use
- Download size: ~20GB (one-time only)
- First generation: 5-15 minutes (includes download)
- Future generations: 30-60 seconds (uses cached model)
- Download location: `~/.cache/huggingface/hub/` (or `HF_HOME` if set)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Qwen Team](https://github.com/QwenLM) for the amazing Qwen-Image model
- [Anthropic](https://anthropic.com) for Claude and MCP
- [Hugging Face](https://huggingface.co) for the diffusers library

## 📚 Links

- [Qwen-Image Model](https://huggingface.co/Qwen/Qwen-Image)
- [MCP Documentation](https://modelcontextprotocol.io)
- [Claude Code](https://claude.ai/code)

---

**Note**: This server requires ~20GB for the model download on first use. The model is cached locally for subsequent runs.