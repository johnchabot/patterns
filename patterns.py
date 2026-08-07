import math
import random

class CamouflageMaterial:
    """Pattern 1: Pre-v3 Digital Disruptive Camouflage Matrix"""
    def get_css_rules(self):
        return """
            rect { shape-rendering: crispEdges; }
            .camo-base    { fill: #1D231A; }
            .camo-macro   { fill: #34442D; }
            .camo-micro   { fill: #566E4C; }
            .camo-accent  { fill: #8A9B74; }
        """
    def get_xml_defs(self):
        return "" # No extra XML gradient tags needed
        
    def evaluate_pixel_class(self, c, r, cols, rows):
        # Multi-scale pseudo-random threshold grouping
        random.seed(c * 37 + r * 101) # Deterministic position seed
        roll = random.random()
        if roll > 0.85: return "camo-accent"
        if roll > 0.60: return "camo-micro"
        if roll > 0.35: return "camo-macro"
        return "camo-base"

class TarmacMaterial:
    """Pattern 2: Weathered Industrial Road Surface"""
    def get_css_rules(self):
        return """
            rect { shape-rendering: crispEdges; }
            .tarmac-base    { fill: #2A2C2E; }
            .tarmac-aggregate { fill: #55585C; }
            .tarmac-silt    { fill: #8B8E93; }
            .tarmac-stain   { fill: #1E2522; }
        """
    def get_xml_defs(self):
        return ""
        
    def evaluate_pixel_class(self, c, r, cols, rows):
        random.seed(c * 13 + r * 53)
        roll = random.random()
        if roll > 0.90: return "tarmac-stain"
        if roll > 0.75: return "tarmac-silt"
        if roll > 0.40: return "tarmac-aggregate"
        return "tarmac-base"

class GoldHexMaterial:
    """Pattern 3: Geometric Honeycomb Wire painted in Specular Gold"""
    def get_css_rules(self):
        return """
            .hex-void { fill: #0B0C10; }
            .hex-wire { 
                fill: url(#metallic-gold); 
                stroke: #2A1A04; 
                stroke-width: 1.5; 
                stroke-linejoin: round; 
            }
        """
    def get_xml_defs(self):
        return """    <linearGradient id="metallic-gold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%"   stop-color="#BF953F" />
      <stop offset="25%"  stop-color="#FCF6BA" />
      <stop offset="50%"  stop-color="#B38728" />
      <stop offset="75%"  stop-color="#FBF5B7" />
      <stop offset="100%" stop-color="#AA771C" />
    </linearGradient>"""
        
    def evaluate_pixel_class(self, c, r, cols, rows):
        return "hex-wire" # Uniform class mapping across the mesh geometric polygons
