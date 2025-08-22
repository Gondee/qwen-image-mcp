#!/usr/bin/env python3
"""
Qwen-Image MCP Server
A Model Context Protocol server for local image generation using the Qwen-Image model.
"""

import os
import sys
from datetime import datetime
from typing import Optional
from pathlib import Path

try:
    from mcp.server.fastmcp import FastMCP
    from diffusers import QwenImagePipeline
    import torch
except ImportError as e:
    print(f"Error: Missing required dependencies: {e}", file=sys.stderr)
    print("Please install requirements: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# Initialize MCP server
app = FastMCP("qwen-image")

# Global pipeline instance (lazy loaded)
_pipe = None

def get_default_output_dir() -> str:
    """Get the default output directory for generated images."""
    # Use Pictures folder if available, otherwise use home directory
    pictures_dir = Path.home() / "Pictures" / "qwen_images"
    if sys.platform == "win32":
        # Windows: Use Pictures folder
        pictures_dir = Path.home() / "Pictures" / "qwen_images"
    elif sys.platform == "darwin":
        # macOS: Use Pictures folder
        pictures_dir = Path.home() / "Pictures" / "qwen_images"
    else:
        # Linux: Use Pictures or home directory
        pictures_dir = Path.home() / "Pictures" / "qwen_images"
    
    return str(pictures_dir)

def _get_pipe():
    """Load and cache the Qwen-Image pipeline."""
    global _pipe
    if _pipe is None:
        print("Loading Qwen-Image model... This may take a few minutes on first run.", file=sys.stderr)
        
        model_id = "Qwen/Qwen-Image"
        
        # Determine device and dtype based on available hardware
        if torch.cuda.is_available():
            dtype = torch.bfloat16
            device = "cuda"
            print(f"Using CUDA device with bfloat16 precision", file=sys.stderr)
        elif torch.backends.mps.is_available():
            dtype = torch.float32  # MPS doesn't support bfloat16
            device = "mps"
            print(f"Using MPS (Apple Silicon) device with float32 precision", file=sys.stderr)
        else:
            dtype = torch.float32
            device = "cpu"
            print(f"Using CPU device with float32 precision", file=sys.stderr)
            print("Warning: CPU inference will be slow. GPU recommended.", file=sys.stderr)
        
        try:
            p = QwenImagePipeline.from_pretrained(
                model_id, 
                torch_dtype=dtype,
                trust_remote_code=True,
                cache_dir=os.getenv("HF_HOME", None)  # Use HF_HOME if set
            )
            p = p.to(device)
            
            # Enable memory optimizations if available
            if hasattr(p, "enable_attention_slicing"):
                p.enable_attention_slicing()
            
            print("Model loaded successfully!", file=sys.stderr)
            _pipe = p
        except Exception as e:
            print(f"Error loading model: {e}", file=sys.stderr)
            raise
    
    return _pipe

@app.tool()
def generate_image(
    prompt: str,
    size: str = "1024x1024",
    steps: int = 50,
    guidance: float = 4.0,
    seed: Optional[int] = None,
    out_dir: Optional[str] = None,
    filename: Optional[str] = None
) -> str:
    """
    Generate an image using the Qwen-Image model.
    
    Qwen-Image excels at:
    - High-fidelity text rendering (especially Chinese and English)
    - Multiple artistic styles
    - Complex scene composition
    - Photorealistic imagery
    
    Args:
        prompt: Text description of the image to generate
        size: Image size - "512x512", "768x768", "1024x1024", "portrait" (768x1152), "landscape" (1152x768)
        steps: Number of diffusion steps (default 50, range 20-100)
        guidance: True CFG scale (default 4.0, range 1.0-10.0, lower=more creative, higher=more literal)
        seed: Random seed for reproducibility (optional)
        out_dir: Directory to save the image (defaults to ~/Pictures/qwen_images)
        filename: Output filename without extension (optional)
    
    Returns:
        Absolute path to the generated image
    """
    # Load pipeline
    pipe = _get_pipe()
    
    # Parse size parameter
    size_map = {
        "portrait": (768, 1152),
        "landscape": (1152, 768),
        "square": (1024, 1024),
        "square-hd": (1024, 1024),
        "hd": (1024, 1024)
    }
    
    if size in size_map:
        w, h = size_map[size]
    elif "x" in size:
        try:
            w, h = map(int, size.split("x"))
        except ValueError:
            print(f"Invalid size format: {size}, using default 1024x1024", file=sys.stderr)
            w = h = 1024
    else:
        # Try to extract number from size string
        import re
        nums = re.findall(r'\d+', size)
        if nums:
            w = h = int(nums[0])
        else:
            w = h = 1024
    
    # Validate dimensions
    if w < 256 or h < 256:
        print(f"Warning: Very small image size ({w}x{h}). Minimum recommended is 512x512", file=sys.stderr)
    if w > 2048 or h > 2048:
        print(f"Warning: Very large image size ({w}x{h}). This may cause memory issues", file=sys.stderr)
    
    # Set seed for reproducibility
    generator = None
    if seed is not None:
        generator = torch.Generator(device=pipe.device).manual_seed(seed)
    
    # Generate image
    try:
        print(f"Generating {w}x{h} image with {steps} steps...", file=sys.stderr)
        image = pipe(
            prompt=prompt,
            width=w,
            height=h,
            num_inference_steps=steps,
            true_cfg_scale=guidance,  # QwenImage uses true_cfg_scale
            generator=generator
        ).images[0]
    except Exception as e:
        print(f"Error during generation: {e}", file=sys.stderr)
        raise
    
    # Prepare output directory
    if out_dir is None:
        out_dir = get_default_output_dir()
    
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Create a safe version of the prompt for filename (first 30 chars)
        safe_prompt = "".join(c for c in prompt[:30] if c.isalnum() or c in " -_").strip()
        safe_prompt = safe_prompt.replace(" ", "_")[:30]
        filename = f"qwen_{safe_prompt}_{timestamp}"
    
    # Ensure .png extension
    if not filename.endswith(('.png', '.jpg', '.jpeg')):
        filename += '.png'
    
    # Save image
    filepath = out_path / filename
    image.save(str(filepath))
    
    print(f"Image saved to: {filepath}", file=sys.stderr)
    return str(filepath)

if __name__ == "__main__":
    # Run the MCP server
    app.run()