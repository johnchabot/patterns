import random

def generate_pre_v3_digital_camouflage(filename="digital_camo.svg"):
    # Canvas properties
    width, height = 1000, 1000
    pixel_size = 10  # This enforces a rigid quantization matrix grid size
    
    cols = width // pixel_size
    rows = height // pixel_size
    
    # 4-Color Palette Schema (Standard Woodland Digital Taxonomy)
    # Layer 0: Dark Base Matrix, Layer 1: Macro-Distortion, Layer 2: Micro-Noise, Layer 3: Edge Contrast
    colors = {
        0: "#1E241E",  # Deep Charcoal / Substrate Base
        1: "#3B4E3B",  # Medium Olive / Macro shapes
        2: "#627B57",  # Foliage Green / Micro texture
        3: "#92A47D"   # Desert Khaki Accent / Edge Breakup
    }
    
    # Ensure reproducibility via a deterministic pseudo-random seed
    random.seed(1997) 
    
    # 1. SPATIAL GENERATION SUBSYSTEM: Create Low-Frequency Macro Structures
    # We populate a grid with large multi-pixel blocks (clumping factor)
    macro_field = {}
    macro_scale = 12  # Defines the size boundaries of the macro clumps
    
    for r in range(0, rows, macro_scale):
        for c in range(0, cols, macro_scale):
            macro_value = random.random()
            # Assign the same base macro value to the local neighborhood block
            for dr in range(macro_scale):
                for dc in range(macro_scale):
                    if (r + dr) < rows and (c + dc) < cols:
                        macro_field[(r + dr, c + dc)] = macro_value

    # Group coordinates by color index to structure our SVG efficiently using <g> tags
    svg_color_buckets = {1: [], 2: [], 3: []}

    # 2. TUNING PARAMETERS LAYER: Iterate across the structural grid
    for r in range(rows):
        for c in range(cols):
            # Fetch the low-frequency background data
            macro_signal = macro_field.get((r, c), 0.5)
            
            # Generate the high-frequency micro signal (individual pixel jitter)
            micro_signal = random.random()
            
            # Combine frequencies programmatically: 70% weight to Macro shapes, 30% weight to Micro details
            composite_value = (macro_signal * 0.70) + (micro_signal * 0.30)
            
            # 3. QUANTIZATION STEP: Force continuous math values into stepped color bands
            if composite_value > 0.75:
                color_assignment = 3
            elif composite_value > 0.48:
                color_assignment = 2
            elif composite_value > 0.26:
                color_assignment = 1
            else:
                color_assignment = 0  # Allowed to drop back into the base matrix color

            # If it's not the background color, bucket its coordinates for the vector generation
            if color_assignment > 0:
                x = c * pixel_size
                y = r * pixel_size
                svg_color_buckets[color_assignment].append((x, y))

    # 4. OUTPUT IMMUTABLE VECTOR FORMAT (.SVG)
    with open(filename, "w") as f:
        # Write XML Header and root SVG canvas element boundaries
        f.write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">\n')
        
        # Draw the solid foundational Base Matrix block layer (Color 0)
        f.write(f'  <rect width="{width}" height="{height}" fill="{colors[0]}"/>\n')
        
        # Inject the grouped pixel layers into quantized color blocks
        for color_idx, coordinate_list in svg_color_buckets.items():
            f.write(f'  <!-- Layering Color Code: {colors[color_idx]} -->\n')
            f.write(f'  <g fill="{colors[color_idx]}">\n')
            
            for x, y in coordinate_list:
                f.write(f'    <rect x="{x}" y="{y}" width="{pixel_size}" height="{pixel_size}"/>\n')
                
            f.write('  </g>\n')
            
        f.write('</svg>\n')
    
    print(f"Success: Pattern baked and exported cleanly to '{filename}'")

# Execute the engine pipeline
if __name__ == "__main__":
    generate_pre_v3_digital_camouflage()
