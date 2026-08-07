import random

class TextureEngine:
    def __init__(self, width=1000, height=1000, seed=1997):
        self.width = width
        self.height = height
        self.seed = seed
        
    def generate_v2_digital_grid(self, filename="output_digital_v2.svg"):
        """
        Option A: The Pre-v3 Digital Camouflage School
        Uses quantization matrices and multi-scale frequency separation.
        """
        pixel_size = 10
        cols = self.width // pixel_size
        rows = self.height // pixel_size
        
        # Foundational Camouflage Palette 
        colors = {
            0: "#1E241E", # Base Substrate Matrix
            1: "#3B4E3B", # Low-Frequency Macro Blobs
            2: "#627B57", # High-Frequency Micro Noise
            3: "#92A47D"  # High-Contrast Edge Disruption
        }
        
        random.seed(self.seed)
        
        # Build Low-Frequency Macro structures
        macro_field = {}
        macro_scale = 12
        for r in range(0, rows, macro_scale):
            for c in range(0, cols, macro_scale):
                macro_val = random.random()
                for dr in range(macro_scale):
                    for dc in range(macro_scale):
                        if (r + dr) < rows and (c + dc) < cols:
                            macro_field[(r + dr, c + dc)] = macro_val

        # Sort coordinates into buckets to optimize final SVG file size
        svg_buckets = {1: [], 2: [], 3: []}

        for r in range(rows):
            for c in range(cols):
                macro_signal = macro_field.get((r, c), 0.5)
                micro_signal = random.random()
                
                # Frequency mixing (70% Macro structural layout, 30% Micro texture detail)
                composite = (macro_signal * 0.70) + (micro_signal * 0.30)
                
                # Quantization Thresholds (Snapping smooth signals into rigid blocks)
                if composite > 0.75:
                    assignment = 3
                elif composite > 0.48:
                    assignment = 2
                elif composite > 0.26:
                    assignment = 1
                else:
                    assignment = 0

                if assignment > 0:
                    svg_buckets[assignment].append((c * pixel_size, r * pixel_size))

        # Output the structural SVG grid file
        with open(filename, "w") as f:
            f.write(f'<svg xmlns="http://w3.org" viewBox="0 0 {self.width} {self.height}" width="100%" height="100%">\n')
            f.write(f'  <rect width="{self.width}" height="{self.height}" fill="{colors[0]}"/>\n')
            for idx, coords in svg_buckets.items():
                f.write(f'  <g fill="{colors[idx]}">\n')
                for x, y in coords:
                    f.write(f'    <rect x="{x}" y="{y}" width="{pixel_size}" height="{pixel_size}"/>\n')
                f.write('  </g>\n')
            f.write('</svg>\n')
        print(f"[-] Option A baked successfully: '{filename}'")

    def generate_rough_paper_texture(self, filename="output_rough_paper.svg"):
        """
        Option B: The Analog Lighting Noise Texture
        Programmatically maps complex procedural noise filters directly into the vector metadata.
        """
        with open(filename, "w") as f:
            f.write(f'<svg xmlns="http://w3.org" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}">\n')
            f.write('  <defs>\n')
            # Inject your exact procedural texture algorithm inside the hardware-accelerated definitions
            f.write("    <filter id='roughpaper' x='0%' y='0%' width='100%' height='100%'>\n")
            f.write(f"      <feTurbulence type='fractalNoise' baseFrequency='0.04' result='noise' numOctaves='5' seed='{self.seed}' />\n")
            f.write("      <feDiffuseLighting in='noise' lighting-color='white' surfaceScale='2'>\n")
            f.write("        <feDistantLight azimuth='45' elevation='60' />\n")
            f.write("      </feDiffuseLighting>\n")
            f.write("    </filter>\n")
            f.write('  </defs>\n')
            # Render the canvas surface utilizing the texture filter mapping
            f.write(f'  <rect width="100%" height="100%" filter="url(#roughpaper)" fill="#EAE6DF"/>\n')
            f.write('</svg>\n')
        print(f"[-] Option B baked successfully: '{filename}'")

# --- EXECUTION PIPELINE ---
if __name__ == "__main__":
    # Instantiate our new unified Engine system with a standard seed
    engine = TextureEngine(width=1000, height=1000, seed=42)
    
    # Run Generation Option A
    engine.generate_v2_digital_grid("digital_camo_output.svg")
    
    # Run Generation Option B (Your exact requested layout)
    engine.generate_rough_paper_texture("analog_rough_paper_output.svg")
