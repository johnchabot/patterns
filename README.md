# patterns
It's a Procedural Vector Texture Recombobulator!

The Power of <feBlend mode="multiply">: Rather than lazily slapping a gray overlay on top of our shapes, the engine uses matrix math blending 🌐. The light levels from the heightmap actively transform the underlying camouflage vector colors 🌐. Whites stay bright, while shadows darken the green and brown color values symmetrically, preserving the exact color identity underneath.

exactly how a clean engine architecture should be split. By decoupling the sorting system and passing that operational control entirely to your layer, the core Python script transitions into a pure, mathematical 3D Vertex Projection and Geometric Code Compiler.

The Innocent engine that outputs textures and can wrap them around shapes for you
THe Cheater function helps making that "seamless" fix, as an auxiliary boundary problem-solver, helping "stitch" edges for known patterns

Polymorphic Blueprint Hooking: The engine code doesn’t care what pattern you are rendering anymore. It just expects that any material class passed to it implements three core methods: .get_css_rules(), .get_xml_defs(), and .evaluate_pixel_class().

Infinite Scale Without Code Bloat: If you want to add a fourth pattern (like a carbon fiber weave or a neon grid layout), you don't touch engine.py at all. You leave the core compiler safe and completely untouched, and just write a new tiny, isolated pattern class block at the bottom of patterns.py.

--- 

Engine  
- Single function call in a Python script, that effectively acts as a 2D or 3D asset compiler  
 2D objects and 3D objects are parsed using the exact same code engine paths. 2D is simply handled as a specialized, low-frequency 3D structure where the spatial coordinates align tightly along a single plane layer.
- Dimensionally aware of geometry and context it is handling (Flat 2D surface layouts vs. Projected 3D volumetric coordinates)  
- Asset Compiler Engine. Python should only handle the execution mechanics (loops, projection math, XML assembly), while JSON holds the structural descriptors, vertex nodes, and boundary rules.

Pattern Options
- Obsidian
- CAND.TV Test Pattern
- Multi-frequency camouflage matrix (mixing macro-blobs and micro-flecks via quantization thresholds),
- Paper (aka inject hardware-accelerated noise recipes) Fractal Noise Generator
- Construction Grid

Cartesian Plane
OR
X,Y,Z 3D: Cube, Sphere, Hexagonal Prism.. even 4 Hexagonal Prisms, wow!

- Pure math frequencies rather than tracking local 2D pixel coordinates. When the top face meets the right face along the cube edge, their shared points have matching 3D values. The modulo checks evaluate identically, causing the graph paper lines to seamlessly wrap around the corners.

Output
Frequency Separation Engine (Macro + Micro layers), the Quantization Pass, and groups vectors to keep the SVG optimized

- Clean, human-readable, semantic .svg files (Semantic Shading via CSS Variables, The Depth Sort / Painter's Algorithm:, he Projection Matrix (3D to 2D):
- (geometry separate from presentation by grouping shapes inside XML containers (<g>) and controlling colors and rendering profiles via modern embedded CSS classes)
- accessible (soon), low-co2

- y leaning heavily on clever geometry concepts—like the Symmetric Boundary Shield, Cyclic Bézier tangents, Polar coordinates, and SIRDS horizontal link shifts—we kept the code fast and elegant, offloading the heavy rendering tasks natively to the hardware.

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
