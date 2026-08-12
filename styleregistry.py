"""
style_registry.py - Style and Presentation Variable Registry
"""

class ModernPresentationStyle:
    """Manages the Wong color blindness contrast palettes and global CSS wrappers."""
    def __init__(self, theme_style="WALLPAPER"):
        self.theme = theme_style.upper()
        # The iconic Wong color blindness contrast accessible array sequence
        self.wong_palette = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]

    def get_color_by_index(self, index):
        """Cyclic ring buffer configuration to support infinite pass loops safely."""
        return self.wong_palette[index % len(self.wong_palette)]

    def get_embedded_css(self):
        """Compiles clean, global presentation selectors inside the SVG header."""
        if self.theme == "WALLPAPER":
            return """
                rect { shape-rendering: crispEdges; }
                .canvas-backdrop { fill: #FAF9F6; } /* Soft Alabaster Paper */
                polygon, path   { stroke-linejoin: round; }
            """
        else: # CAMO theme base defaults
            return """
                rect { shape-rendering: crispEdges; }
                .canvas-backdrop { fill: #1D231A; } /* Matte Dark Substrate Shadow */
                polygon, path   { stroke-linejoin: round; }
            """
