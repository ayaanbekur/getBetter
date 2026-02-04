"""
Script to generate properly sized PNG icons for PWA from GetBetter.jpg
Run this script: python generate_icons.py
"""

from PIL import Image, ImageDraw
import os

# Create icons directory
icons_dir = os.path.join('static', 'icons')
os.makedirs(icons_dir, exist_ok=True)

# Try to load existing GetBetter.jpg
jpg_path = os.path.join('static', 'GetBetter.jpg')

try:
    # Load and convert JPG to PNG with proper sizing
    img = Image.open(jpg_path)
    print(f"Loaded GetBetter.jpg - Size: {img.size}")
    
    # Create 192x192 regular icon
    icon_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192.save(os.path.join(icons_dir, 'icon-192x192.png'), 'PNG')
    print("✓ Created icon-192x192.png")
    
    # Create 512x512 regular icon
    icon_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    icon_512.save(os.path.join(icons_dir, 'icon-512x512.png'), 'PNG')
    print("✓ Created icon-512x512.png")
    
    # Create maskable icons (for adaptive icons on Android)
    # Maskable icons need padding - keeping them centered
    maskable_192 = Image.new('RGBA', (192, 192), (10, 10, 10, 255))  # Dark background
    offset = (0, 0)
    maskable_192.paste(img.resize((192, 192), Image.Resampling.LANCZOS), offset, img.resize((192, 192), Image.Resampling.LANCZOS) if img.mode == 'RGBA' else None)
    maskable_192.save(os.path.join(icons_dir, 'icon-maskable-192x192.png'), 'PNG')
    print("✓ Created icon-maskable-192x192.png")
    
    maskable_512 = Image.new('RGBA', (512, 512), (10, 10, 10, 255))  # Dark background
    maskable_512.paste(img.resize((512, 512), Image.Resampling.LANCZOS), (0, 0), img.resize((512, 512), Image.Resampling.LANCZOS) if img.mode == 'RGBA' else None)
    maskable_512.save(os.path.join(icons_dir, 'icon-maskable-512x512.png'), 'PNG')
    print("✓ Created icon-maskable-512x512.png")
    
    print("\n✅ All icons generated successfully!")
    print(f"Icons location: {icons_dir}/")
    
except FileNotFoundError:
    print(f"❌ Error: GetBetter.jpg not found at {jpg_path}")
    print("\nCreating fallback icons with 'Get Better' text...")
    
    # Create simple fallback icons with text
    for size in [192, 512]:
        # Create background
        img = Image.new('RGB', (size, size), color=(10, 10, 10))  # Dark background
        draw = ImageDraw.Draw(img)
        
        # Draw a simple arrow-up symbol for "Get Better"
        margin = size // 8
        arrow_color = (255, 255, 255)
        
        # Draw upward arrow
        center_x = size // 2
        center_y = size // 2
        arrow_size = size // 3
        
        # Arrow shaft
        draw.rectangle(
            [(center_x - arrow_size//6, center_y - arrow_size//3),
             (center_x + arrow_size//6, center_y + arrow_size//3)],
            fill=arrow_color
        )
        
        # Arrow head
        draw.polygon(
            [(center_x - arrow_size//2, center_y),
             (center_x + arrow_size//2, center_y),
             (center_x, center_y - arrow_size//2)],
            fill=arrow_color
        )
        
        img.save(os.path.join(icons_dir, f'icon-{size}x{size}.png'), 'PNG')
        
        # Also create maskable version
        img.save(os.path.join(icons_dir, f'icon-maskable-{size}x{size}.png'), 'PNG')
        
        print(f"✓ Created icon-{size}x{size}.png (fallback)")
    
    print("\n✅ Fallback icons created!")
    print("⚠️  These are placeholder icons. Replace with your actual design when ready.")

print("\nNext steps:")
print("1. Update manifest.json (already done)")
print("2. Push changes to GitHub")
print("3. Redeploy to Render")
print("4. Run PWABuilder again")
