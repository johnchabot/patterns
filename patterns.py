
"""
patterns.py - Material Library Registry

This module acts as a polymorphic repository for texture definitions. 
Every class acts as a plug-and-play material socket implementing three required methods:
1. get_css_rules()         -> Emits styling rules for the SVG <style> container.
2. get_xml_defs()          -> Emits vector gradient, pattern, or shader macros.
3. evaluate_pixel_class()  -> Coordinates coordinate-aware cell class routing.
"""

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

class HoneycombPatternMaterial:
    """Pattern 4: Seamless Honeycomb Matrix with Polish-Edge Gold Gradients"""
    
    def get_css_rules(self):
        # We don't need complex sub-classes here because the fill pattern 
        # manages its own internal polygon stroke styles natively!
        return """
            .honeycomb-canvas-fill {
                fill: url(#honeycomb);
            }
        """

    def get_xml_defs(self):
        return """    <!-- Gold gradient for honeycomb lines -->
    <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#462523;stop-opacity:1" />
      <stop offset="22%" style="stop-color:#cb9b51;stop-opacity:1" />
      <stop offset="45%" style="stop-color:#f6e27a;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#f6f2c0;stop-opacity:1" />
      <stop offset="55%" style="stop-color:#f6e27a;stop-opacity:1" />
      <stop offset="78%" style="stop-color:#cb9b51;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#462523;stop-opacity:1" />
    </linearGradient>

    <!-- Honeycomb pattern with gold gradient lines -->
    <pattern id="honeycomb" x="0" y="0" width="40" height="69.28" patternUnits="userSpaceOnUse">
      <rect width="40" height="69.28" fill="#000000"/>
      <!-- Hexagon 1 -->
      <polygon points="20,0 40,11.55 40,34.64 20,46.19 0,34.64 0,11.55"
               fill="none" stroke="url(#goldGradient)" stroke-width="3"/>
      <!-- Hexagon 2 (offset down) -->
      <polygon points="40,34.64 60,46.19 60,69.28 40,80.83 20,69.28 20,46.19"
               fill="none" stroke="url(#goldGradient)" stroke-width="3"/>
      <!-- Hexagon 3 (offset up) -->
      <polygon points="0,34.64 20,46.19 20,69.28 0,80.83 -20,69.28 -20,46.19"
               fill="none" stroke="url(#goldGradient)" stroke-width="3"/>
    </pattern>"""

    def evaluate_pixel_class(self, c, r, cols, rows):
        # Unused by the tiled fill mode, but kept for polymorphic blueprint parity
        return "honeycomb-canvas-fill"





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


class ConcreteMaterial:
    """[Abstract Blueprint] Tactile industrial aggregate cement finish."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "concrete-mat-fallback"


class ObsidianMaterial:
    """[Abstract Blueprint] Deep vitreous volcanic glass sheen."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "obsidian-mat-fallback"


class WalnutMaterial:
    """[Abstract Blueprint] Organic flowing architectural hardwood woodgrain."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "walnut-mat-fallback"


class FrostedGlassMaterial:
    """[Abstract Blueprint] Translucent dithered glassmorphic diffusion matrix."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "frosted-glass-mat-fallback"


class DichroicGlassMaterial:
    """[Abstract Blueprint] Multi-chromatic light-splitting polarization surface."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "dichroic-glass-mat-fallback"


class SubwayTileMaterial:
    """[Abstract Blueprint] Interlocking offset geometric running-bond tile grid."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "subway-tile-mat-fallback"


class IridescentWhiteMaterial:
    """[Abstract Blueprint] Pearlescent, shimmering pearl-essence light strike."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "iridescent-white-mat-fallback"


class WaterMaterial:
    """[Abstract Blueprint] Caustic, fluid mathematical liquid ripple refraction."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "water-mat-fallback"


class PearlescentMaterial:
    """[Abstract Blueprint] Soft chromatic lustre shifting shell finish."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "pearlescent-mat-fallback"


class GinghamMaterial:
    """[Abstract Blueprint] Crossed intersecting checks and transparent weave tints."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "gingham-mat-fallback"


class CrumbledPaperMaterial:
    """[Abstract Blueprint] High-frequency geometric crease shadow heightmap."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "crumbled-paper-mat-fallback"


class NeonYellowMaterial:
    """[Abstract Blueprint] Piercing high-visibility radioactive tactical blast finish."""
    def get_css_rules(self) -> str:
        return ""

    def get_xml_defs(self) -> str:
        return ""
        
    def evaluate_pixel_class(self, c: int, r: int, cols: int, rows: int) -> str:
        return "neon-yellow-mat-fallback"

