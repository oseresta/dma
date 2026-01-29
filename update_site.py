import os

# 1. Configuration
DATA_DIR = '/Users/oseresta/www/dma/forward'
PICS_FILE = '/Users/oseresta/www/dma/forward/index.html' # Or 'forward/index.html' if using clean URLs

# 2. Get all images from the data folder
valid_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.webp')
images = [f for f in os.listdir(DATA_DIR) if f.lower().endswith(valid_extensions)]

# 3. Create the HTML content
img_tags = "\n".join([f'        <div class="card"><img src="{img}"><p>{img}</p></div>' for img in images])

html_template = f"""<!DOCTYPE html>
<html>
<head>
    <title>DMA Forward Testing Gallery</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; background: #fafafa; }}
        .gallery {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(500px, 1fr)); gap: 20px; }}
        .card {{ background: white; padding: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }}
        img {{ max-width: 100%; border-radius: 4px; }}
        a {{ display: inline-block; margin-bottom: 20px; color: #007bff; text-decoration: none; }}
    </style>
</head>
<body>
    <a href="../index.html">← Back to Dashboard</a>
    <h2>Auto-Generated Gallery</h2>
    <div class="gallery">
{img_tags}
    </div>
</body>
</html>"""

# 4. Write to the file
with open(PICS_FILE, 'w') as f:
    f.write(html_template)
