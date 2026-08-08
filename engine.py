# Add HoneycombPatternMaterial to your engine imports at the top
from patterns import 
import math
from patterns import CamouflageMaterial, TarmacMaterial, GoldHexMaterial, HoneycombPatternMaterial

class UnifiedCanvasEngine:
    """
    A core rendering engine. It handles geometry layouts, coordinate loops, 
    and document formatting while relying on injected material classes for styles.
    """
    def __init__(self, width=800, height=800):
        self.width = width
        self.height = height

    def compile_asset(self, material_instance, layout_mode="GRID", filename="output.svg"):
        """
        Accepts any polymorphic pattern material class instance and compiles 
        its data rules cleanly down to a structured SVG layout file.
        """
        with open(filename, "w") as f:
            # 1. Output Layout Header Attributes
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write(f'<svg xmlns="http://w3.org" viewBox="0 0 {self.width} {self.height}" width="100%" height="100%">\n\n')
            
            # 2. Extract and Inject XML Definitions (Gradients/Shaders)
            defs_content = material_instance.get_xml_defs()
            if defs_content:
                f.write('  <defs>\n' + defs_content + '\n  </defs>\n\n')
                
            # 3. Extract and Inject Modular CSS Stylesheets
            f.write('  <style type="text/css">\n' + material_instance.get_css_rules() + '\n  </style>\n\n')
            f.write('  <g id="compiled-render-layer">\n')

            # --- ROUTE A: STANDARD COLUMN/ROW SQUARE RECT PIPELINE ---
            if layout_mode == "GRID":
                spacing = 16
                cols, rows = self.width // spacing, self.height // spacing
                
                for r in range(rows):
                    for c in range(cols):
                        # Query the decoupled material module to find out what color class this coordinate gets
                        cls = material_instance.evaluate_pixel_class(c, r, cols, rows)
                        f.write(f'    <rect x="{c*spacing}" y="{r*spacing}" width="{spacing}" height="{spacing}" class="{cls}" />\n')

            # --- ROUTE B: PARAMETRIC VERTEX OBLIQUE HEXAGON PIPELINE ---
            elif layout_mode == "HEX":
                radius = 30.0
                hex_w, hex_h = math.sqrt(3) * radius, 1.5 * radius
                cols, rows = int(self.width / hex_w) + 2, int(self.height / hex_h) + 2
                
                # Base black backdrop for vector cutouts
                f.write(f'    <rect width="{self.width}" height="{self.height}" class="hex-void" />\n')
                
                for r in range(rows):
                    cy = r * hex_h
                    row_offset = (hex_w / 2.0) if (r % 2 != 0) else 0.0
                    for c in range(cols):
                        cx = c * hex_w + row_offset
                        
                        # Generate hexagon 6-corner coordinate paths
                        pts = []
                        for i in range(6):
                            ang = (math.pi / 3) * i + (math.pi / 6)
                            pts.append(f"{cx + radius * math.cos(ang):.1f},{cy + radius * math.sin(ang):.1f}")
                        
                        cls = material_instance.evaluate_pixel_class(c, r, cols, rows)
                        f.write(f'    <polygon class="{cls}" points="{" ".join(pts)}" />\n')

            f.write('  </g>\n</svg>\n')
        print(f"[Engine] Successfully compiled asset profile to '{filename}'")

# Inside your UnifiedCanvasEngine class, add this layout path condition:
# ... (Previous GRID and HEX conditions remain unchanged) ...

            # --- ROUTE C: HARDWARE-ACCELERATED NATIVE SVG TILED FILL ---
            elif layout_mode == "TILED_FILL":
                cls = material_instance.evaluate_pixel_class(0, 0, 1, 1)
                
                # Check if we are running the technical carbon fiber material profile
                if cls == "carbon-fiber-canvas":
                    f.write(f'    <!-- Layer 01: Multi-Layered Woven Polymer Texture Background -->\n')
                    f.write(f'    <rect width="{self.width}" height="{self.height}" class="carbon-fiber-canvas" />\n')
                    f.write(f'    <!-- Layer 02: Center-Focused Ambient Occlusion Vignette Overlay -->\n')
                    f.write(f'    <rect width="{self.width}" height="{self.height}" class="vignette-overlay" />\n')
                elif cls == "brushed-steel-plate":
                    # (Your existing brushed steel stacking layers remain safely intact here)
                    f.write(f'    <rect width="{self.width}" height="{self.height}" class="brushed-steel-plate" />\n')
                    f.write(f'    <rect width="{self.width}" height="{self.height}" class="brushed-grain-overlay" />\n')
                else:
                    # Fallback configuration pass for single-layer pattern fills
                    f.write(f'    <rect width="{self.width}" height="{self.height}" class="{cls}" />\n')

            f.write('  </g>\n</svg>\n')


# --- INITIALIZATION CONTROL LAYER ---
if __name__ == "__main__":
    engine = UnifiedCanvasEngine(width=800, height=800)
    
    # We can now effortlessly add and test new patterns by creating 
    # an instance of the pattern class and sending it down the engine line:
    engine.compile_asset(CamouflageMaterial(), layout_mode="GRID", filename="mat_camo.svg")
    engine.compile_asset(TarmacMaterial(),      layout_mode="GRID", filename="mat_tarmac.svg")
    engine.compile_asset(GoldHexMaterial(),     layout_mode="HEX",  filename="mat_gold_hex.svg")
