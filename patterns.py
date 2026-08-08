
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


class StarrySkyMaterial:
    """Pattern 7: Procedural Starry Sky Void via High-Contrast Noise Matrix"""
    
    def get_css_rules(self):
        return """
            .starry-sky-void {
                fill: #000000;              /* Absolute deep-space backing black */
                filter: url(#starry-sky);   /* Apply the GPU-accelerated star generator */
            }
        """

    def get_xml_defs(self):
        return """    <!-- STARRY SKY SHADER: High-frequency noise squeezed through an isolation matrix -->
    <filter id="starry-sky" x="0%" y="0%" width="100%" height="100%">
      <!-- Pass 1: Generate high-frequency digital noise mapping -->
      <feTurbulence type="fractalNoise" baseFrequency="0.2" numOctaves="1" result="raw-noise" />
      
      <!-- Pass 2: Color Matrix isolation. 
                   Squeezes the red, green, and blue values drastically (x9 multiplier, -4 offset) 
                   to collapse the broad noise fields into tiny, piercing white starlight pins. -->
      <feColorMatrix in="raw-noise" type="matrix"
                     values="0 0 0 9 -4
                             0 0 0 9 -4
                             0 0 0 9 -4
                             0 0 0 0 1" />
    </filter>"""

    def evaluate_pixel_class(self, c, r, cols, rows):
        return "starry-sky-void"


class ERDLCamoMaterial:
    """Pattern 8: GPU-Driven ERDL Camouflage via Discrete Channel Slicing Matrices"""
    
    def get_css_rules(self):
        return """
            .erdl-camo-canvas {
                fill: #000000;              /* Fallback foundation base */
                filter: url(#erdl-camo);    /* Execute the procedural channel shader */
            }
        """

    def get_xml_defs(self):
        return """    <!-- ERDL CAMOUFLAGE SHADER LAYER -->
    <filter id="erdl-camo" x="0%" y="0%" width="100%" height="100%">
      <!-- Pass 1: Create an organic, flowing mathematical landscape baseline -->
      <feTurbulence type="fractalNoise" baseFrequency="0.02" numOctaves="3" result="base-noise"/>
      
      <!-- Pass 2: Quantization. Slice the continuous gradient channels into discrete color index bands -->
      <feComponentTransfer in="base-noise" result="indexed-bands">
        <feFuncR type="discrete" tableValues="0 0 1"/>
        <feFuncG type="discrete" tableValues="0 0 0 1 1"/>
        <feFuncB type="discrete" tableValues="0 1"/>
      </feComponentTransfer>
      
      <!-- Pass 3: Isolate channel distributions to prepare for final color mapping -->
      <feColorMatrix in="indexed-bands" result="isolated-channels"
                     values="1  0 0 0 0
                            -1  1 0 0 0
                            -1 -1 1 0 0
                             0  0 0 0 1"/>
                             
      <!-- Pass 4: The Palette Transformation. Maps the isolated channel segments 
                   directly to classic organic ERDL woodland camo color values. -->
      <feColorMatrix in="isolated-channels"
                     values="-.08  .42  .09 0 .08
                             -.17  .35 -.08 0 .17
                             -.08  .15 -.04 0 .08
                              0    0     0    0 1"/>
    </filter>"""

    def evaluate_pixel_class(self, c, r, cols, rows):
        return "erdl-camo-canvas"



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


class HilroyWasHereMaterial:
    """Pattern 9: Hilroy Fine-Ruled Notebook Paper Alignment Grid"""
    
    def get_css_rules(self):
        return """
            .hilroy-paper-canvas {
                fill: url(#hilroy-ruled-lines); /* Apply the infinite linear rule tile */
                opacity: 0.8;                   /* Enforce the requested 80% canvas transparency */
            }
        """

    def get_xml_defs(self):
        return """    <!-- HILROY GRID ENGINE: Seamless 20px repeating horizontal notebook rule tiles -->
    <pattern id="hilroy-ruled-lines" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <!-- Base padding background tone block -->
      <rect width="20" height="20" fill="#E5E5F7" />
      
      <!-- 1px precision horizontal rule line tracking your exact CSS color matrix -->
      <line x1="0" y1="0" x2="20" y2="0" stroke="#444CF7" stroke-width="1" />
    </pattern>"""

    def evaluate_pixel_class(self, c, r, cols, rows):
        return "hilroy-paper-canvas"

class MarrakeshMaterial:
    """Pattern 10: Divya Manian's Marrakesh Concentric Mosaic Tiling System"""
    
    def get_css_rules(self):
        return """
            .marrakesh-canvas {
                fill: url(#marrakesh-mosaic-tile); /* Bind canvas background to our structural mesh */
            }
        """

    def get_xml_defs(self):
        return """    <!-- MARRAKESH GRID PIPELINE: Concentric radial ring networks stacked over a 0,0 alignment axis -->
    <pattern id="marrakesh-mosaic-tile" x="0" y="0" width="90" height="90" patternUnits="userSpaceOnUse">
      <!-- Foundational bright white grout substrate layer -->
      <rect width="90" height="90" fill="#ffffff" />
      
      <!-- Layer 01: Core Geometric Grid Repetition Loops -->
      <!-- Emulates the 30px x 30px micro-cell star groupings across the 90px master patch -->
      <pattern id="marrakesh-sub-star" x="0" y="0" width="30" height="30" patternUnits="userSpaceOnUse">
        <!-- 9px focused central midnightblue circle focal point -->
        <circle cx="0" cy="0" r="9" fill="midnightblue" />
        <circle cx="30" cy="0" r="9" fill="midnightblue" />
        <circle cx="0" cy="30" r="9" fill="midnightblue" />
        <circle cx="30" cy="30" r="9" fill="midnightblue" />
      </pattern>
      <rect width="90" height="90" fill="url(#marrakesh-sub-star)" />

      <!-- Layer 02: Concentric Ripple Rings (The 90px x 90px repeating-radial core) -->
      <!-- Simulates the nested geometric wave pulses pulsing outward from center coordinates -->
      <!-- Ring 1 (0px to 4px) -->
      <circle cx="0" cy="0" r="4" fill="none" stroke="midnightblue" stroke-width="4" />
      <!-- Ring 2 (21px to 25px) -->
      <circle cx="0" cy="0" r="23" fill="none" stroke="midnightblue" stroke-width="4" />
      
      <!-- Mirror repeat anchors across the 90px grid boundary matrix corners to ensure perfect seaming -->
      <circle cx="90" cy="0" r="4" fill="none" stroke="midnightblue" stroke-width="4" />
      <circle cx="90" cy="0" r="23" fill="none" stroke="midnightblue" stroke-width="4" />
      <circle cx="0" cy="90" r="4" fill="none" stroke="midnightblue" stroke-width="4" />
      <circle cx="0" cy="90" r="23" fill="none" stroke="midnightblue" stroke-width="4" />
      <circle cx="90" cy="90" r="4" fill="none" stroke="midnightblue" stroke-width="4" />
      <circle cx="90" cy="90" r="23" fill="none" stroke="midnightblue" stroke-width="4" />
    </pattern>"""

    def evaluate_pixel_class(self, c, r, cols, rows):
        return "marrakesh-canvas"




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

