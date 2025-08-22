# 🔧 Troubleshooting Guide

## Common Issues and Solutions

### 🔴 MCP Server Not Connecting

**Symptoms:**
- Claude Code shows "Failed to connect to qwen-image"
- `/mcp` command shows server as disconnected

**Solutions:**

1. **Check Python installation:**
```bash
python3 --version  # Should be 3.10+
```

2. **Test server manually:**
```bash
python3 server.py
# Should wait for input (Ctrl+C to exit)
```

3. **Re-register the server:**
```bash
claude mcp remove qwen-image
claude mcp add --scope user qwen-image python3 -- /full/path/to/server.py
```

4. **Check Claude Code logs:**
- Look for error messages in Claude Code output
- Ensure no other process is using the same name

---

### 💾 Model Download Issues

**Symptoms:**
- First generation takes forever
- Disk space errors
- Connection timeouts

**Solutions:**

1. **Check available disk space:**
```bash
df -h  # Linux/Mac
# Need at least 25GB free
```

2. **Set custom cache directory:**
```bash
export HF_HOME=/path/to/large/disk
python3 server.py
```

3. **Resume interrupted download:**
- Simply try generating again - Hugging Face resumes partial downloads

4. **Use different mirror (for users in certain regions):**
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

---

### ⚫ Black or Corrupted Images

**Symptoms:**
- Generated images are all black
- Images have artifacts or corruption
- Partial/incomplete images

**Solutions:**

1. **Update dependencies:**
```bash
pip install --upgrade diffusers transformers torch
```

2. **Check GPU memory:**
```python
import torch
print(torch.cuda.is_available())  # Should be True for GPU
print(torch.cuda.get_device_name(0))  # Your GPU name
```

3. **Use CPU mode (slower but stable):**
- The server automatically falls back to CPU if GPU unavailable

4. **Reduce image size:**
- Try 512x512 instead of 1024x1024
- Lower step count to 30

---

### 🧠 Out of Memory Errors

**Symptoms:**
- "CUDA out of memory" errors
- "MPS out of memory" on Mac
- Server crashes during generation

**Solutions:**

1. **For GPU memory issues:**
```python
# Add to server.py after model loading:
import torch
torch.cuda.empty_cache()  # Clear GPU cache
```

2. **Reduce memory usage:**
- Generate smaller images (512x512)
- Use fewer steps (30 instead of 50)
- Close other GPU-using applications

3. **For Mac (MPS) users:**
```bash
export PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0
```

4. **Use system RAM (CPU mode):**
- Remove GPU/MPS code, force CPU usage
- Slower but works with system RAM

---

### 🐌 Slow Generation

**Symptoms:**
- Each image takes 10+ minutes
- CPU usage at 100%
- No GPU acceleration

**Solutions:**

1. **Verify GPU is being used:**
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"MPS available: {torch.backends.mps.is_available()}")
```

2. **Install CUDA (NVIDIA GPUs):**
- Check NVIDIA driver: `nvidia-smi`
- Install appropriate CUDA version for your PyTorch

3. **For Apple Silicon Macs:**
- Ensure using PyTorch 2.0+
- MPS should be automatically detected

4. **Optimize settings for speed:**
```python
steps=30  # Reduce from 50
size="768x768"  # Smaller than 1024x1024
```

---

### 📝 Text Rendering Issues

**Symptoms:**
- Text in images is garbled
- Characters are incorrect
- Text positioning is wrong

**Solutions:**

1. **Use clearer text prompts:**
```
"A sign with the exact text 'HELLO WORLD' in bold Arial font"
```

2. **Increase guidance for text:**
```python
guidance=6.0  # Higher for better text adherence
```

3. **Specify text language:**
```
"Chinese characters '你好' in traditional calligraphy style"
```

---

### 🔄 Server Crashes/Restarts

**Symptoms:**
- Server disconnects during generation
- Need to restart after each image
- Python process dies

**Solutions:**

1. **Check Python error logs:**
```bash
python3 server.py 2>&1 | tee server.log
```

2. **Monitor system resources:**
```bash
# During generation, watch:
top  # or htop
```

3. **Increase system limits:**
```bash
ulimit -n 4096  # Increase file handles
```

4. **Run in background with logging:**
```bash
nohup python3 server.py > server.log 2>&1 &
```

---

### 🚫 Permission Errors

**Symptoms:**
- Can't save images
- "Permission denied" errors
- Can't create output directory

**Solutions:**

1. **Check directory permissions:**
```bash
ls -la ~/Pictures/
chmod 755 ~/Pictures/qwen_images  # If exists
```

2. **Use different output directory:**
- Specify `out_dir` parameter in generation
- Use `/tmp` for testing

3. **Run with correct user:**
```bash
whoami  # Check current user
```

---

### ❓ Other Issues

**Can't find 'claude' command:**
- Ensure Claude Code is in PATH
- Try full path: `/usr/local/bin/claude`

**Multiple Python versions:**
```bash
which python3
# Use full path in registration
```

**Firewall/Antivirus blocking:**
- Add Python and Claude Code to exceptions
- Temporarily disable to test

**Still having issues?**

1. **Collect debug info:**
```bash
python3 --version
pip list | grep -E "diffusers|torch|transformers"
claude mcp list
```

2. **Test minimal setup:**
```python
from diffusers import QwenImagePipeline
print("Import successful")
```

3. **Report issue with:**
- Error messages
- System info (OS, Python version, GPU)
- Steps to reproduce

---

## 🆘 Getting Help

- **GitHub Issues**: Report bugs with full error messages
- **Discussions**: Ask questions about usage
- **Discord/Community**: Real-time help from other users

Remember: Most issues are related to environment setup, not the model itself!