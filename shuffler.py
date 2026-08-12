"""
matrix_painter.py - Multi-Pass Quadrant Shuffling Engine Core Compiler
"""
import argparse
import json
import math
import random

class GeometryCompiler:
    """Generates smooth cyclic organic shapes enforcing C1 boundary closure matching."""
    @staticmethod
    def generate_cyclic_shape(bounds, point_count=5, size_scale=1.0):
        cx, cy = (bounds["x_min"] + bounds["x_max"]) / 2, (bounds["y_min"] + bounds["y_max"]) / 2
        base_r = (min(bounds["x_max"] - bounds["x_min"], bounds["y_max"] - bounds["y_min"]) / 2.2) * size_scale
        
        vertices = []
        for i in range(point_count):
            angle = (2 * math.pi / point_count) * (i + random.uniform(-0.1, 0.1))
            vertices.append((cx + base_r * random.uniform(0.7, 1.3) * math.cos(angle), 
                             cy + base_r * random.uniform(0.7, 1.3) * math.sin(angle)))
            
        control_points = []
        for i in range(point_count):
            p_prev, p_curr, p_next = vertices[i-1], vertices[i], vertices[(i+1)%point_count]
            dx, dy = p_next[0] - p_prev[0], p_next[1] - p_prev[1]
            control_points.append(((p_curr[0] - dx*0.25, p_curr[1] - dy*0.25), 
                                   (p_curr[0] + dx*0.25, p_curr[1] + dy*0.25)))
            
        d_path = f"M {vertices[0][0]:.1f},{vertices[0][1]:.1f} "
        for i in range(point_count):
            nxt = (i + 1) % point_count
            cp1, cp2 = control_points[i][1], control_points[nxt][0]
            d_path += f"C {cp1[0]:.1f},{cp1[1]:.1f} {cp2[0]:.1f},{cp2[1]:.1f} {vertices[nxt][0]:.1f},{vertices[nxt][1]:.1f} "
        return vertices, f'{d_path}Z'


class PolarSprayCompiler:
    """Computes Gaussian airbrush mists and exponential targeted fluid impact splatters."""
    @staticmethod
    def generate_airbrush_mist(bounds, density=80, scale=35.0):
        cx = random.uniform(bounds["x_min"] + scale, bounds["x_max"] - scale)
        cy = random.uniform(bounds["y_min"] + scale, bounds["y_max"] - scale)
        elements = []
        for _ in range(density):
            angle, dist = random.uniform(0, 2*math.pi), abs(random.gauss(0, scale))
            px, py = cx + dist * math.cos(angle), cy + dist * math.sin(angle)
            if bounds["x_min"] <= px <= bounds["x_max"] and bounds["y_min"] <= py <= bounds["y_max"]:
                elements.append((px, py, random.choice([0.8, 1.2, 1.8])))
        return elements

    @staticmethod
    def generate_targeted_splatter(bounds, density=100, scale=15.0):
        cx = random.uniform(bounds["x_min"] + 40, bounds["x_max"] - 40)
        cy = random.uniform(bounds["y_min"] + 40, bounds["y_max"] - 40)
        elements = []
        for _ in range(density):
            angle = random.uniform(0, 2 * math.pi)
            if random.random() > 0.15:
                dist, r_size = random.uniform(0, scale), random.uniform(1.5, 3.0)
            else:
                dist, r_size = scale * random.uniform(1.2, 3.5), random.choice([0.6, 1.0, 1.5])
            px, py = cx + dist * math.cos(angle), cy + dist * math.sin(angle)
            if bounds["x_min"] <= px <= bounds["x_max"] and bounds["y_min"] <= py <= bounds["y_max"]:
                elements.append((px, py, r_size))
        return elements


class SirdsPipeline:
    """Calculates horizontal coordinate displacements to output hidden 3D autostereograms."""
    @staticmethod
    def _inside_poly(x, y, poly):
        inside = False
        n = len(poly)
        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x) and p1y != p2y:
                if x <= (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x: inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def generate_layer(self, bounds, width, shapes, color_hex):
        elements = []
        for y in range(int(bounds["y_min"]), int(bounds["y_max"]), 8):
            same = [i for i in range(width)]
            for x in range(int(bounds["x_min"]), int(bounds["x_max"])):
                z = 0.45 if any(self._inside_poly(x, y, s) for s in shapes) else 0.0
                sep = int(140 - (z * 30))
                left, right = x - (sep//2), x + (sep - (sep//2))
                if left >= 0 and right < width: same[right] = same[left]
            
            colors = [None] * width
            for x in range(int(bounds["x_min"]), int(bounds["x_max"])):
                colors[x] = color_hex if same[x] == x and random.random() > 0.4 else (colors[same[x]] if same[x] != x else "transparent")
                if colors[x] != "transparent" and (x % 6 == 0) and random.random() > 0.3:
                    elements.append(f'    <circle cx="{x}" cy="{y + random.uniform(-2,2)}" r="{random.choice([1.0, 1.5])}" fill="{colors[x]}" />')
        return "\n".join(elements)


class MasterProductionShuffler:
    """The central orchestrator engine that handles loops, boundaries, and transformations."""
    def __init__(self, config_path="manifest.json", theme="WALLPAPER", force_stochastic=False):
        with open(config_path, "r") as f: self.config = json.load(f)
        c_set = self.config["canvas_settings"]
        self.width, self.height, self.spacing = c_set["width"], c_set["height"], c_set["cell_spacing"]
        self.cols, self.rows = self.width // self.spacing, self.height // self.spacing
        self.mid_c, self.mid_r = self.cols // 2, self.rows // 2
        
        rules = self.config["shield_rules"]
        self.margin = rules["center_safety_margin_cells"] if rules["enforce_insulated_borders"] else 0
        self.stochastic = force_stochastic or (self.config.get("shuffle_mode") == "stochastic")
        
        from style_registry import ModernPresentationStyle
        self.style = ModernPresentationStyle(theme)
        self.color_index = 0
        self.output_buffer = []

    def _get_quadrant_bounds(self, quad_idx):
        if quad_idx == 1:   c, r = (self.margin, self.mid_c - self.margin), (self.margin, self.mid_r - self.margin)
        elif quad_idx == 2: c, r = (self.mid_c + self.margin, self.cols - self.margin), (self.margin, self.mid_r - self.margin)
        elif quad_idx == 3: c, r = (self.margin, self.mid_c - self.margin), (self.mid_r + self.margin, self.rows - self.margin)
        else:               c, r = (self.mid_c + self.margin, self.cols - self.margin), (self.mid_r + self.margin, self.rows - self.margin)
        return {"x_min": c[0]*self.spacing, "x_max": c[1]*self.spacing, "y_min": r[0]*self.spacing, "y_max": r[1]*self.spacing}

    def _get_shuffle_map(self):
        quads = [1, 2, 3, 4]
        if self.stochastic:
            dests = quads.copy(); random.shuffle(dests)
            return dict(zip(quads, dests))
        return {1: 4, 4: 1, 2: 3, 3: 2} # Planned Cross-Inversion Mode

    def compile(self, filename="baked_output.svg"):
        random.seed(2026)
        sirds = SirdsPipeline()
        
        for p in self.config["pipeline_passes"]:
            shuffler = self._get_shuffle_map()
            active_color = self.style.get_color_by_index(self.color_index)
            
            for src_quad in:
                dest_bounds = self._get_quadrant_bounds(shuffler[src_quad])
                
                if p["type"] == "SHAPE":
                    verts, d = GeometryCompiler.generate_cyclic_shape(dest_bounds, p["points"], p["scale"])
                    self.output_buffer.append(f'    <path d="{d}" fill="{active_color}" fill-opacity="0.8" />')
                    if p["run_sirds"]:
                        self.output_buffer.append(sirds.generate_layer(dest_bounds, self.width, [verts], active_color))
                        
                elif p["type"] == "AIRBRUSH":
                    for px, py, r in PolarSprayCompiler.generate_airbrush_mist(dest_bounds, p["density"], p["scale"]):
                        self.output_buffer.append(f'    <circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" fill="{active_color}" fill-opacity="0.5" />')
                        
                elif p["type"] == "SPLATTER":
                    for px, py, r in PolarSprayCompiler.generate_targeted_splatter(dest_bounds, p["density"], p["scale"]):
                        self.output_buffer.append(f'    <circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="{active_color}" fill-opacity="0.6" />')

            self.color_index += 1

        with open(filename, "w") as f:
            f.write('<?xml version="1.0" encoding="utf-8"?>\n')
            f.write(f'<svg xmlns="http://w3.org" viewBox="0 0 {self.width} {self.height}" width="100%" height="100%">\n')
            f.write(f'  <style type="text/css">\n{self.style.get_embedded_css()}  </style>\n')
            f.write(f'  <rect width="{self.width}" height="{self.height}" class="canvas-backdrop" />\n\n')
            f.write('  <g id="viewport-matrix-stream">\n')
            for vec in self.output_buffer: f.write(vec + "\n")
            f.write('  </g>\n</svg>\n')
        print(f"[Pipeline Success] Output cleanly written to: '{filename}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Pass Transformation Engine CLI Driver")
    parser.add_argument("--stochastic", action="store_true", help="Forces random scrambling over planned loops.")
    parser.add_argument("--style", type=str, default="WALLPAPER", choices=["WALLPAPER", "CAMO"], help="Toggles visual profiles.")
    parser.add_argument("--output", type=str, default="pattern_out.svg", help="Target filename.")
    args = parser.parse_args()
    
    shuffler = MasterProductionShuffler(theme=args.style, force_stochastic=args.stochastic)
    shuffler.compile(args.output)
