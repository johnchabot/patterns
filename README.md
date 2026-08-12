# Procedural Vector Texture Recombobulator (PVTRNS)
Apply repeating over a 2D canvas or 3D object asset compiler

### FUNCTION  
python matrix_painter.py --style WALLPAPER --output soft_wallpaper.svg  
python matrix_painter.py --style CAMO --stochastic --output random_camo.svg  

### ENGINE (engine.py):
* Clean engine architecture handing execution mechanics (loops, projection math, XML assembly), using JSON, which holds the structural descriptors, vertex nodes, and boundary rules
* Inspects the incoming data structure, detects the type of object being constructed (2D Grid vs. 3D Model) and updates its parsing routines, style blocks, and XML layout tags accordingly.  

  * Declarative Seam Schemas: Seam logic requires identifying matching boundaries. JSON allows you to map explicit coordinate relationships (e.g., "Edge A of Face 1 connects to Edge C of Face 5") as simple key-value pairs that the Python engine can easily parse.
  * Universal Compatibility: JSON maps directly to native Python dictionaries via the standard json library, allowing you to ingest complex network maps without any custom parsing scripts.
* Dimensionally aware of geometry and context it is handling (Flat 2D surface layouts vs. Projected 3D volumetric coordinates)   
* Polymorphic Blueprint Hooking: The engine code doesn’t care what pattern you are rendering anymore. It just expects that any material class passed to it implements three core methods: .get_css_rules(), .get_xml_defs(), and .evaluate_pixel_class().  
* By decoupling the sorting system and passing that operational control entirely to your layer, the core Python script transitions into a pure, mathematical 3D Vertex Projection and Geometric Code Compiler.  
* Semantic DOM Sorting over Hardcoded Coordinates  
* Vector Scaling with Pure Integrity: Because the math projects coordinates as relative vectors rather than fixed rasterized pixels, the entire 3D structure preserves absolute vector clarity. You can scale the browser layout window infinitely, and the projected vertices, crisp polygon joins (stroke-linejoin: round), and volumetric face shapes will remain perfectly sharp.
* The Canvas Driver: The core Python script acts as an asset compiler rather than a flat image renderer. It is entirely aware of the dimensional geometry context it is handling (Flat 2D surface layouts vs. Projected 3D volumetric coordinates).
Parametric Cyclic Bézier Spline Engine

### PATTERNS (patterns.py)
Material Library
| Name | Types   | Notes    |
| :---:   | :---: | :---: |
| Camouflage  | ERDL camouflage, pre_v3_digital_camouflage   | dynamic, tactile, textured digital camouflage matrices multi-frequency camouflage matrix (mixing macro-blobs and micro-flecks via quantization thresholds), inject hardware-accelerated noise recipes  |
| Hexagonal Grid | ds | hexagons to catch specular light paths |
| Paper | Construction grid; Rough   | 283   |
| Hilroy Paper | Construction grid; Rough   | 283   |
| Cotton Weave | cdc | adsads |
| Marrakesh by Divya Manian | cdc | adsads |
| Madras by Divya Manian | cdc | adsads |
| Plinth Tartan or Isometric Gingham | cdc | adsads |
| Carbon Fiber | cdc | adsads |
| Madras by Divya Manian | cdc | adsads |
| Code Page 437 ROM ░░░░░ | sffs | From a programmatic texture engine perspective, this is a brilliant conceptual input. It is the absolute digital symbol for ordered dithering, frequency attenuation, and procedural density masking. |
| Starry Sky | cdc |  High-frequency feTurbulence noise field, squeezes the color channels through a high-contrast feColorMatrix calculation to isolate single sharp pixels, creating a scattered field of bright white stars over an absolute black void |
| Stainless Steel | fsddsf | eates the optical illusion of chrome-like metal reflections catching a hard light source |
| Brushed Stele | sfdfsd | This creates a realistic brushed steel grain that catches light like real metal. |
| Repetitive Custom Patterns | Quadrant | 283   |
| Tarmac | NOT BUILD | Weathered Industrial Road Surface |
| Obsidian | NOT BUILT | dsa |
| Walnut | NOT BUILT | dsa |
| Frosted Glass | NOT BUILT | dsa |
| Dichroic Glass | NOT BUILT | dsa |
| Subway Tile | NOT BUILT | dsa |
| Water | NOT BUILT | dsa |
| Pearlescent | NOT BUILT | dsa |
| Gingham Picnic Tablecloth | NOT BUILT | dsa |
| Subway Tile | NOT BUILT | dsa |
| Crumpled Paper | NOT BUILT | dsa |
| Neon Yellow | NOT BUILT | dsa |
| IridescentWhiteMaterial | NOT BUILT | dsa |
| Single Image Random Dot Stereogram (SIRDS) | |

SPRAYS
1. Digital Airbrush (Gaussian/Normal): (Smooth, mist-like fading edges), The Math: Generates a random angle uniformly between \(0\), The Visual: This concentrates particles at the origin and creates a smooth, mist-like gradient fade toward the edges, matching the look of a real pneumatic airbrush
2. Targeted Splatter (Inverse Power/Exponential): (Dense core, sudden violent splatter flecks), The Math: Uses an Exponential Decay or Inverse Square distance filter. The majority of points are clamped tightly to the center core, but a secondary high-velocity threshold calculation forces a few random particles to burst outward at extreme distances. The Visual: This forms a solid, heavy paint hit at the center point, surrounded by a ring of chaotic, high-velocity impact splatters.
+

The "Potato" Shape (Continuous Bézier Curves)
The "Spray" Pattern (Stipple Particle Clouds)
Layer Accumulation Effect:
Absolute Edge Protection


LAYOUT
The Core Quadrant-Shuffling Engine Mode + Symmetric Boundary Shield + Zero Cut Motifs + Randomized Reshuffle (Stochastic Shuffling)
Integrating Shuffling Modes Directly into JSON Configuration
This is an incredibly rich extension to the Procedural Multi-Pass Shuffling Engine. By injecting fresh geometric layers—specifically organic Bézier-curved shapes and high-frequency stipple spray patterns—into each quadrant before executing the next positional shuffle, you are building an authentic Layer-Accumulation Vector Texture Engine.


COLORS
Wong Color Palette, specifically engineered in computational biology and data science to guarantee absolute maximum visual contrast and accessibility (Color Vision Deficiency / Colorblind safety)
Golden
Neon Yellow
White

The Math-First Approach: By leaning heavily on clever geometry concepts—like the Symmetric Boundary Shield, Cyclic Bézier tangents, Polar coordinates, and SIRDS horizontal link shifts—we kept the code fast and elegant, offloading the heavy rendering tasks natively to the hardware.
Unlike random camouflage, which requires 4 to 8 passes to scramble chaotic noise, a luxury monogram needs perfect, deliberate symmetry. The passes map out like this:

/quadrant-shuffle-engine
 │
 ├── 1. manifest.json      (The Shield Rules & Pass Configuration) manifest.json (The Pipeline Configuration Blueprint)
 ├── 2. matrix_painter.py  (The Core Multi-Pass Shuffle Compiler) matrix_painter.py (The Structural Asset Compiler Engine)
 └── 3. style_registry.py  (The Clean CSS and Color Token Palettes) style_registry.py (The Modern Palette & CSS Storage)

1. Straight Repeat (Formal & Structured): Standard rectilinear mapping. The column spacing (\(X\)
2. Diagonal / Offset Brick Repeat (The Classic Monogram): Alternating row interleaving. To create a perfect brick pattern, every odd-numbered row shifts horizontally by exactly half a column width.
3. Diamond Lattice & Quatrefoils (Enclosed Heritage Geometry): 45-degree coordinate rotation mixed with a bounding lattice. A true Quatrefoil is constructed programmatically by combining a central square box with four overlapping border circles tracking the midpoints of the box edges.



### SHAPES (shapes.json)
| Name | Types   | Notes    |
| :---:   | :---: | :---: |
| Cube  | test   | It's a cube  |
| Hexagonal Prism | Regular, Gem, Garage | 283   |


### PATTERNS
* Symmetric Boundary Shield, Cyclic Bézier tangents, Polar coordinates, and SIRDS horizontal link shifts—we kept the code fast and elegant, offloading the heavy rendering tasks natively to the hardware  
* Camo: Rather than lazily slapping a gray overlay on top of our shapes, the engine uses matrix math blending. The light levels from the heightmap actively transform the underlying camouflage vector colors. Whites stay bright, while shadows darken the green and brown color values symmetrically, preserving the exact color identity underneath.  

### 2D Cartesian Plane  
* 2D is simply handled as a specialized, low-frequency 3D structure where the spatial coordinates align tightly along a single plane layer
* treats a flat 2D plane as a deliberate, single-facet mathematical surface rather than just an arbitrary array of flat pixel blocks.
* The script wraps the coordinates around a virtual cylinder or torus using trigonometry (\(\cos \)
* Infinite Wrapping (2D mode): In the 2D pipeline, the code maps the columns and rows onto a circular coordinate path (math.cos(angle_x)). Because a circle has no beginning or end, the calculated noise patterns on the absolute left edge of your texture automatically blend with the numbers on the right edge, giving you an infinite tiling asset.
* To map a 2D canvas using the 3D JSON format, you treat the Z-axis as a structural layer index (depth) or a height/displacement variable while utilizing multi-node parametric coordinates.
* You can warp, skew, stretch, or rotate the 2D surface coordinate grid simply by modifying the vertex map values in the JSON file.

### 3D Vertex Projection, Texture Mapping and Coordinate Seaming
* The Stacking Matrix: Authority over how the array elements inside cube_faces are prioritized. Because the compiler processes the faces linearly from the first item to the last item in the list, you can structure, shift, or completely re-sort that input array on your end to enforce the exact layout depth stacking order you want.
* Instead of flatly drawing coordinates where shapes overwrite each other randomly, the Z-axis becomes an explicit layer index scale
* The Cube Mapping Approach (Object-Space Grids): A cube has six flat faces. Instead of pasting a flat 2D image onto each face separately (which creates alignment errors at the corners), the engine queries the true 3D spatial coordinate \((X, Y, Z)\)
* The Sphere Mapping Approach (Spherical Polar Projection): A sphere has no flat sides. To wrap grid lines cleanly around it, the engine translates 3D spatial points into Latitude (\(\phi \)
* For 3D Objects (Cubes, Hexagonal Prisms, Spheres): The engine iterates through the geometry using the true 3D spatial positions of the points. Because the mathematical function evaluates seamlessly across 3D space, the pattern naturally flows around corners, from the top face down across the side facets, with absolute continuity  
* Object-Space Texture Generation. It queries a 3D noise function at the exact \((X,Y,Z)\)  
* The "Innocent" engine that outputs textures and can wrap them around shapes for you  
* Pure math frequencies rather than tracking local 2D pixel coordinates. When the top face meets the right face along the cube edge, their shared points have matching 3D values. The modulo checks evaluate identically, causing the graph paper lines to seamlessly wrap around the corners.  
* THe "Cheater" function helps making a 'seamless' fix, acting as an auxiliary boundary problem-solver, helping "stitch" edges for known patterns
* The "Cheater" Function Position: The Cheater function is an auxiliary boundary problem-solver. Because many textures will naturally show an edge discontinuity or seam depending on the shape they are wrapped around, the Cheater is treated as a secondary tool. The engine functions independently without it; the Cheater is simply turned on when a specific geometry combination requires automated edge management.
* Adopting the "cheater" mindset is a brilliant architectural move. By letting that module specialize entirely in the pure spatial coordinate math—smartly calculating how geometry intersections align seamlessly in object-space—we can keep the XML rendering pipeline flat, fast, and simple.


### .SVG OUTPUT
* Clean, human-readable, semantic .svg files
* geometry separate from presentation by grouping shapes inside XML containers (<g>) and controlling colors and rendering profiles via modern embedded CSS classes
* Semantic Shading via CSS Variables
* accessible (soon), low-co2
* 100% Native CSS-to-Vector Hooking: Look at how the CSS rule .honeycomb-wire { fill: url(#metallic-gold); } links up. Every single hexagon across the entire pattern reads from the exact same global linear gradient coordinates mapping. This ensures that as the pattern prints across the canvas, the gold highlights behave like a single large sheet of metal catching light evenly across the grid framework.
* groups vectors to keep the SVG optimized
* Clean Structural Output: If you open the generated file in a code editor, you won't see messy style strings inline. It stays beautifully organized: a single background <rect>, a cleanly declared style matrix block, and an ordered list of structured <polygon> nodes that construct your layout.
* The Output Protocol: The engine strictly outputs clean, human-readable, semantic .svg files. It keeps geometry separate from presentation by grouping shapes inside XML containers (<g>) and controlling colors and rendering profiles via modern embedded CSS classes.

### MORE

[CAMOUFLAGE ENGINE CORE]
 │
 ├── 1. Spatial Generation Subsystem (The Architecture)
 │    ├── Deterministic Pseudo-Random Seed
 │    ├── Fractal Brownian Motion (fBm) Loop
 │    └── Quantization / Pixel Snapping Function
 │
 ├── 2. Structural Tuning Parameters (The Mathematical Scales)
 │    ├── Macro-Frequency (Distance Blending / Silhouette Breakup)
 │    └── Micro-Frequency (Close-Range / Texture Simulation)
 │
 └── 3. Edge Manipulation Layer (The Dither Engine)
      ├── Sharp/Stark Hard Boundaries (Maximum Disruption)
      └── Spatial Jitter / Bayer Matrix (Perceptual Blending)
