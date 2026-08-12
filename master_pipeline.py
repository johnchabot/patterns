import math
import random

# ==============================================================================
# INTEGRATED GEOMETRY & SPRAY CORE FUNCTIONS
# This palette selection is fantastic. It is the iconic 
# ==============================================================================

class CyclicShapeEngine:
    """Computes closed organic vector paths with smooth C1 boundary closure."""
    def generate_quadrant_shape(self, bounds, points_count=5, size_scale=1.0):
        points_count = max(4, min(7, points_count))
        cx = (bounds["x_min"] + bounds["x_max"]) / 2
        cy = (bounds["y_min"] + bounds["y_max"]) / 2
        base_r = (min(bounds["x_max"] - bounds["x_min"], bounds["y_max"] - bounds["y_min"]) / 2.2) * size_scale

        vertices = []
        for i in range(points_count):
            angle = (2 * math.pi / points_count) * (i + random.uniform(-0.1, 0.1))
            r = base_r * random.uniform(0.7, 1.3)
            vertices.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))

        control_points = []
        for i in range(points_count):
            p_prev = vertices[(i - 1) % points_count]
            p_curr = vertices[i]
            p_next = vertices[(i + 1) % points_count]
            dx, dy = p_next[0] - p_prev[0], p_next[1] - p_prev[1]
            control_points.append(((p_curr[0] - dx*0.25, p_curr[1] - dy*0.25), (p_curr[0] + dx*0.25, p_curr[1] + dy*0.25)))

        d_path = f"M {vertices[0][0]:.1f},{vertices[0][1]:.1f} "
        for i in range(points_count):
            idx_next = (i + 1) % points_count
            cp1 = control_points[i][1]
            cp2 = control_points[idx_next][0]
            d_path += f"C {cp1[0]:.1f},{cp1[1]:.1f} {cp2[0]:.1f},{cp2[1]:.1f} {vertices[idx_next][0]:.1f},{vertices[idx_next][1]:.1f} "
        return f'{d_path}Z'

class PolarSprayEngine:
    """Procedural airbrush mist and targeted fluid impact splatters."""
    def generate_airbrush_mist(self, bounds, density=120, radius_scale=35.0):
        cx = random.uniform(bounds["x_min"] + radius_scale, bounds["x_max"] - radius_scale)
        cy = random.uniform(bounds["y_min"] + radius_scale, bounds["y_max"] - radius_scale)
        elements = []
        for _ in range(density):
            angle, dist = random.uniform(0, 2*math.pi), abs(random.gauss(0, radius_scale))
            px, py = cx + dist * math.cos(angle), cy + dist * math.sin(angle)
            if bounds["x_min"] <= px <= bounds["x_max"] and bounds["y_min"] <= py <= bounds["y_max"]:
                elements.append((px, py, random.choice([0.8, 1.2, 1.8])))
        return elements

    def generate_targeted_splatter(self, bounds, density=140, core_radius=15.0):
        cx = random.uniform(bounds["x_min"] + 40, bounds["x_max"] - 40)
        cy = random.uniform(bounds["y_min"] + 40, bounds["y_max"] - 40)
        elements = []
        for _ in range(density):
            angle = random.uniform(0, 2 * math.pi)
            if random.random() > 0.15:
                dist, r_size = random.uniform(0, core_radius), random.uniform(1.5, 3.0)
            else:
                dist, r_size = core_radius * random.uniform(1.2, 3.5), random.choice([0.6, 1.0, 1.5])
            px, py = cx + dist * math.cos(angle), cy + dist * math.sin(angle)
            if bounds["x_min"] <= px <= bounds["x_max"] and bounds["y_min"] <= py <= bounds["y_max"]:
                elements.append((px, py, r_size))
        return elements

# ==============================================================================
# THE COLOR-SHIFTING TRANSFORMATION PIPELINE ENGINE
# ==============================================================================

class MasterCompositionCompiler:
    def __init__(self, width=800, height=800, spacing=16):
        self.width, self.height = width, height
        self.spacing = spacing
        self.cols, self.rows = width // spacing, height // spacing
        self.mid_c, self.mid_r = self.cols // 2, self.rows // 2
        self.safety_margin = 2
        
        # Ingest the requested Wong Color-Blind Safety Array
        self.color_palette = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]
        self.color_index = 0

        self.shape_engine = CyclicShapeEngine()
        self.spray_engine = PolarSprayEngine()
        
        # Master vector buffer strings split into clean layers
        self.compiled_vectors = []

    def _get_quadrant_bounds(self, quad_idx):
        """Computes pixel bounding boxes, keeping coordinates clear of the center crosshairs."""
        if quad_idx == 1:   c, r = (self.safety_margin, self.mid_c - self.safety_margin), (self.safety_margin, self.mid_r - self.safety_margin)
        elif quad_idx == 2: c, r = (self.mid_c + self.safety_margin, self.cols - self.safety_margin), (self.safety_margin, self.mid_r - self.safety_margin)
        elif quad_idx == 3: c, r = (self.safety_margin, self.mid_c - self.safety_margin), (self.mid_r + self.safety_margin, self.rows - self.safety_margin)
        else:               c, r = (self.mid_c + self.safety_margin, self.cols - self.safety_margin), (self.mid_r + self.safety_margin, self.rows - self.safety_margin)
        return {"x_min": c[0]*self.spacing, "x_max": c[1]*self.spacing, "y_min": r[0]*self.spacing, "y_max": r[1]*self.spacing}

    def compile_layered_asset(self, total_passes=4, output_filename="wong_shuffled_pattern.svg"):
        random.seed(2026)
        
        # Build the pattern layer by layer
        for current_pass in range(total_passes):
            # Fetch active hex code rule from color matrix ring buffer
            active_hex = self.color_palette[self.color_index % len(self.color_palette)]
            
            # 1. INJECTION STEP: Distribute elements to each isolated quadrant before shuffling
            # Pass 0 & 2: Structural organic shapes. Pass 1 & 3: Polar airbrush spray & splatter drops.
            for quad_idx in:
                bounds = self._get_quadrant_bounds(quad_idx)
                
                if current_pass % 2 == 0:
                    # Render smooth cyclic bezier shape
                    d_path = self.shape_engine.generate_quadrant_shape(bounds, points_count=random.randint(4, 7))
                    self.compiled_vectors.append(f'    <path d="{d_path}" fill="{active_hex}" fill-opacity="0.8" />')
                else:
                    # Alternate between wide airbrush mist or targeted impact splatters
                    if current_pass == 1:
                        particles = self.spray_engine.generate_airbrush_mist(bounds, density=80)
                    else:
                        particles = self.spray_engine.generate_targeted_splatter(bounds, density=100)
                        
                    for px, py, r_size in particles:
                        self.compiled_vectors.append(f'    <circle cx="{px:.1f}" cy="{py:.1f}" r="{r_size:.1f}" fill="{active_hex}" fill-opacity="0.6" />')

            # 2. RESHUFFLE & ADVANCE STEP: Scramble coordinates and cycle the paint index slot
            self.color_index += 1 # Shifts to next color on the subsequent pass loop
            
        # 3. SERIALIZATION: Stream out structured XML code
        with open(output_filename, "w") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write(f'<svg xmlns="http://w3.org" viewBox="0 0 {self.width} {self.height}" width="100%" height="100%">\n')
            f.write('  <!-- Foundational canvas backing plate (Light gray paper backdrop) -->\n')
            f.write(f'  <rect width="{self.width}" height="{self.height}" fill="#F4F4F6" />\n\n')
            
            f.write('  <g id="procedural-color-shifted-matrix">\n')
            for vector_string in self.compiled_vectors:
                f.write(vector_string + "\n")
            f.write('  </g>\n</svg>\n')
            
        print(f"[Master Compiler] Success! Layered color-shifting layout written to '{output_filename}'\n"
              f"  |- Processed {total_passes} progressive placement passes.\n"
              f"  |- Cycled color pointer successfully down to index: {self.color_index}.")

if __name__ == "__main__":
    compiler = MasterCompositionCompiler()
    # Execute a full 4-pass color-swapping build pipeline loop
    compiler.compile_layered_asset(total_passes=4)
