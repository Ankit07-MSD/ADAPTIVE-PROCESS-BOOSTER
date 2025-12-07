#!/usr/bin/env python3
"""
Utility script to convert architecture diagrams to multiple formats
"""

from PIL import Image
import os
import sys

def convert_diagram(input_file, output_formats=['jpg', 'webp', 'pdf']):
    """Convert a diagram to multiple formats."""
    
    if not os.path.exists(input_file):
        print(f"❌ File not found: {input_file}")
        return False
    
    base_name = os.path.splitext(input_file)[0]
    print(f"\n📊 Converting {input_file}...")
    
    try:
        img = Image.open(input_file)
        
        # Convert to RGB if needed (for JPG/PDF)
        if img.mode in ('RGBA', 'LA', 'P'):
            rgb_img = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode == 'RGBA':
                rgb_img.paste(img, mask=img.split()[-1])
            else:
                rgb_img.paste(img)
            img = rgb_img
        
        success_count = 0
        for fmt in output_formats:
            try:
                output_file = f"{base_name}.{fmt}"
                if fmt == 'pdf':
                    img.save(output_file, 'PDF', resolution=300.0)
                elif fmt == 'webp':
                    img.save(output_file, 'WEBP', quality=90)
                elif fmt == 'jpg' or fmt == 'jpeg':
                    img.save(output_file, 'JPEG', quality=95)
                elif fmt == 'png':
                    img.save(output_file, 'PNG')
                else:
                    print(f"⚠️  Unsupported format: {fmt}")
                    continue
                
                file_size = os.path.getsize(output_file) / 1024  # KB
                print(f"  ✅ Created: {output_file} ({file_size:.1f} KB)")
                success_count += 1
            except Exception as e:
                print(f"  ⚠️  Error creating {fmt}: {e}")
        
        print(f"  ✓ Successfully converted to {success_count} format(s)")
        return True
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False


def convert_all_diagrams():
    """Convert all architecture diagrams."""
    diagrams = [
        'System_Architecture_Diagram.png',
        'Threading_Architecture_Diagram.png',
        'Data_Flow_Diagram.png',
        'Process_Flowchart_Diagram.png'
    ]
    
    print("=" * 60)
    print("Architecture Diagram Converter")
    print("=" * 60)
    
    found_diagrams = []
    for diagram in diagrams:
        if os.path.exists(diagram):
            found_diagrams.append(diagram)
        else:
            print(f"⚠️  {diagram} not found (skipping)")
    
    if not found_diagrams:
        print("\n❌ No diagram files found!")
        print("Please run create_architecture_diagram.py first.")
        return
    
    print(f"\n📁 Found {len(found_diagrams)} diagram(s) to convert\n")
    
    # Ask for formats
    print("Available formats: png, jpg, pdf, webp")
    print("Enter formats to convert (comma-separated, or 'all' for all):")
    user_input = input("> ").strip().lower()
    
    if user_input == 'all':
        formats = ['jpg', 'pdf', 'webp']
    else:
        formats = [f.strip() for f in user_input.split(',') if f.strip()]
        if not formats:
            formats = ['jpg', 'pdf', 'webp']  # Default
    
    print(f"\n🔄 Converting to: {', '.join(formats)}\n")
    
    success_count = 0
    for diagram in found_diagrams:
        if convert_diagram(diagram, formats):
            success_count += 1
    
    print("\n" + "=" * 60)
    print(f"✅ Conversion complete! {success_count}/{len(found_diagrams)} diagrams converted.")
    print("=" * 60)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Convert specific file
        input_file = sys.argv[1]
        formats = sys.argv[2].split(',') if len(sys.argv) > 2 else ['jpg', 'pdf', 'webp']
        convert_diagram(input_file, formats)
    else:
        # Convert all diagrams
        convert_all_diagrams()




