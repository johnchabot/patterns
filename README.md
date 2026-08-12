# patterns - Procedural Vector Texture Recombobulator
Creates a pre-set pattern over a 2D canvas or 3D object asset compiler

### COOL PATTERNS
| Name | Types   | Notes    |
| :---:   | :---: | :---: |
| Camo  | pre_v3_digital_camouflage   | dynamic, tactile, textured digital camouflage matrices  |
| Paper | Construction grid; Rough   | 283   |
| Customized | Logo or Shapes on 4 quadrants, repeat   | 283   |
- Obsidian
- CAND.TV Test Pattern
- Construction Grid

### X,Y,Z 3D SHAPES
| Name | Types   | Notes    |
| :---:   | :---: | :---: |
| Cube  | test   | It's a cube  |
| Hexagonal Prism | Regular, Gem, Garage | 283   |
| 4 Hexagonal Prisms | maybe | 283   |

### INPUT:

### ENGINE:
* This complete Python script inspects the incoming data structure. It automatically detects the type of object being constructed (2D Grid vs. 3D Model) and updates its parsing routines, style blocks, and XML layout tags accordingly.  
* Clean engine architecture offering Infinite Scale Without Code Bloat (Engine.py; Easily-expanded Patterns.py)  
* You feed it structural data, and it decides whether to route that data through a Coordinate Projection Engine or a Pixel/Grid Map Engine  
* Asset Compiler Engine. Python should only handle the execution mechanics (loops, projection math, XML assembly), while JSON holds the structural descriptors, vertex nodes, and boundary rules.  
* Dimensionally aware of geometry and context it is handling (Flat 2D surface layouts vs. Projected 3D volumetric coordinates)   
* Polymorphic Blueprint Hooking: The engine code doesn’t care what pattern you are rendering anymore. It just expects that any material class passed to it implements three core methods: .get_css_rules(), .get_xml_defs(), and .evaluate_pixel_class().  
* By decoupling the sorting system and passing that operational control entirely to your layer, the core Python script transitions into a pure, mathematical 3D Vertex Projection and Geometric Code Compiler.  
* Semantic DOM Sorting over Hardcoded Coordinates  
* Vector Scaling with Pure Integrity: Because the math projects coordinates as relative vectors rather than fixed rasterized pixels, the entire 3D structure preserves absolute vector clarity. You can scale the browser layout window infinitely, and the projected vertices, crisp polygon joins (stroke-linejoin: round), and volumetric face shapes will remain perfectly sharp.  
* Camo: Rather than lazily slapping a gray overlay on top of our shapes, the engine uses matrix math blending. The light levels from the heightmap actively transform the underlying camouflage vector colors. Whites stay bright, while shadows darken the green and brown color values symmetrically, preserving the exact color identity underneath.  

### 2D Cartesian Plane  
* 2D is simply handled as a specialized, low-frequency 3D structure where the spatial coordinates align tightly along a single plane layer  
* Symmetric Boundary Shield, Cyclic Bézier tangents, Polar coordinates, and SIRDS horizontal link shifts—we kept the code fast and elegant, offloading the heavy rendering tasks natively to the hardware  
* The script wraps the coordinates around a virtual cylinder or torus using trigonometry (\(\cos \)  

### 3D Vertex Projection, Texture Mapping and Coordinate Seaming
* The Stacking Matrix: Authority over how the array elements inside cube_faces are prioritized. Because the compiler processes the faces linearly from the first item to the last item in the list, you can structure, shift, or completely re-sort that input array on your end to enforce the exact layout depth stacking order you want.  
* For 3D Objects (Cubes, Hexagonal Prisms, Spheres): The engine iterates through the geometry using the true 3D spatial positions of the points. Because the mathematical function evaluates seamlessly across 3D space, the pattern naturally flows around corners, from the top face down across the side facets, with absolute continuity  
* Object-Space Texture Generation. It queries a 3D noise function at the exact \((X,Y,Z)\)  
* The "Innocent" engine that outputs textures and can wrap them around shapes for you  
* Pure math frequencies rather than tracking local 2D pixel coordinates. When the top face meets the right face along the cube edge, their shared points have matching 3D values. The modulo checks evaluate identically, causing the graph paper lines to seamlessly wrap around the corners.  
* THe "Cheater" function helps making a 'seamless' fix, acting as an auxiliary boundary problem-solver, helping "stitch" edges for known patterns  



### .SVG OUTPUT
* Clean, human-readable, semantic .svg files
* geometry separate from presentation by grouping shapes inside XML containers (<g>) and controlling colors and rendering profiles via modern embedded CSS classes
* Semantic Shading via CSS Variables
* accessible (soon), low-co2
* groups vectors to keep the SVG optimized

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
