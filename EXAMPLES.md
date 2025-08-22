# 🎨 Qwen-Image Generation Examples

This document provides example prompts and tips for getting the best results from the Qwen-Image model.

## 📸 Photorealistic Images

### Nature & Landscapes
```
"A misty mountain valley at dawn, with layers of fog between pine-covered peaks, 
golden sunlight breaking through clouds, photorealistic, 8K quality"

"Crystal clear alpine lake reflecting snow-capped mountains, wildflowers in 
foreground, dramatic cumulus clouds, golden hour lighting, ultra realistic"
```

### Animals
```
"Close-up portrait of a majestic snow leopard with piercing blue eyes, 
detailed fur texture, snowflakes on whiskers, bokeh background, 
wildlife photography style"

"A hummingbird frozen in flight approaching a red hibiscus flower, 
wings showing motion blur, dewdrops on petals, macro photography"
```

### Urban & Architecture
```
"Modern glass skyscraper at blue hour, reflections of city lights, 
long exposure light trails from traffic below, architectural photography"

"Cozy European café on a cobblestone street, warm light spilling from windows, 
rain-wet pavement reflecting lights, evening atmosphere"
```

## 🎭 Artistic Styles

### Oil Painting Style
```
"Portrait of a woman in Renaissance style, oil painting technique, 
rich colors, dramatic chiaroscuro lighting, wearing period dress"
```

### Watercolor Style
```
"Loose watercolor painting of a Venice canal, soft washes of color, 
visible brush strokes, dreamy atmosphere"
```

### Anime/Manga Style
```
"Anime character with long flowing silver hair, large expressive eyes, 
cherry blossoms in background, studio Ghibli style"
```

## ✍️ Text in Images

Qwen-Image excels at rendering text accurately:

```
"A vintage coffee shop sign that says 'The Daily Grind' in elegant script, 
weathered wood background, warm lighting"

"Motivational poster with text 'Dream Big, Work Hard' in bold modern font, 
abstract geometric background, minimalist design"

"Chinese calligraphy writing '春夏秋冬' (four seasons) on rice paper, 
traditional ink brush style, artistic composition"
```

## 🎬 Complex Scenes

### Multi-element Compositions
```
"A busy farmers market scene: vendors selling colorful produce, 
customers browsing, a musician playing guitar, children running, 
morning sunlight filtering through tent canopies"

"Home office workspace: modern desk with laptop, coffee mug with steam, 
succulent plants, notebook with handwritten notes, warm natural light 
from window showing garden view"
```

## 💡 Tips for Better Results

### 1. Be Specific About Style
- Instead of "beautiful image", use "photorealistic", "oil painting style", "minimalist design"
- Mention specific photography terms: "bokeh", "macro", "long exposure"

### 2. Describe Lighting
- "golden hour", "blue hour", "studio lighting", "dramatic shadows"
- "soft diffused light", "harsh directional light", "rim lighting"

### 3. Add Technical Details
- "8K resolution", "ultra detailed", "sharp focus"
- "shallow depth of field", "tilt-shift effect"

### 4. Specify Mood and Atmosphere
- "peaceful", "dramatic", "mysterious", "vibrant"
- "moody", "ethereal", "cinematic"

### 5. Use Composition Terms
- "rule of thirds", "centered composition", "symmetrical"
- "close-up", "wide angle", "bird's eye view"

## 🔧 Parameter Tuning

### For Maximum Detail
```python
size="1024x1024"
steps=70
guidance=3.5
```

### For Artistic/Creative Results
```python
size="1024x1024" 
steps=50
guidance=2.5  # Lower guidance for more creative interpretation
```

### For Text Rendering
```python
size="1024x1024"
steps=60
guidance=5.0  # Higher guidance for accurate text
```

### For Fast Previews
```python
size="512x512"
steps=30
guidance=4.0
```

## ❌ What to Avoid

- **Overly complex prompts**: Keep it under 200 words
- **Contradictory descriptions**: "dark bright image" confuses the model
- **Too many style mixtures**: "oil painting watercolor anime style" gives inconsistent results
- **Impossible physics**: "water flowing upward naturally" may produce artifacts

## 🌍 Language Support

Qwen-Image handles multiple languages well:

```
"Sign that says 'Welcome' in English, '欢迎' in Chinese, and 'Bienvenido' 
in Spanish, modern design, clean typography"
```

## 🎯 Specific Use Cases

### Product Photography
```
"Luxury watch on black velvet surface, dramatic lighting highlighting 
metal details, reflection on watch face, product photography style"
```

### Food Photography
```
"Gourmet burger with melting cheese, fresh lettuce, sesame seed bun, 
on wooden board, shallow depth of field, restaurant photography style"
```

### Portrait Photography
```
"Professional headshot of businessman, confident expression, 
soft studio lighting, neutral gray background, corporate photography"
```

### Event Photography
```
"Wedding couple first dance, soft romantic lighting, bokeh lights 
in background, candid moment, photojournalistic style"
```

## 🔄 Iterating on Results

If your first result isn't perfect:

1. **Adjust guidance**: Lower for more creative, higher for more literal
2. **Add more specific details**: Colors, textures, positioning
3. **Change style descriptors**: Try different artistic influences
4. **Modify composition**: Specify viewing angle, distance, framing
5. **Use a seed**: Set a seed number and make small prompt adjustments

Remember: The model needs to download (~20GB) on first use, but subsequent generations are much faster!