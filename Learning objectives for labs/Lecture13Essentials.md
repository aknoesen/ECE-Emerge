### Fundamental Topics First‑Year Engineering Students Should Master — Lecture 13

*Difficulty ratings: 1 = easiest, 3 = most challenging*

1. Advanced 2‑D Line Plots and Multi‑Series Control — **Difficulty: 1**
   - Create multi‑series plots with plot, control line style/marker/color, add legends/annotations, and arrange multiple axes with tiledlayout/subplot.
   - *Plotting multiple series and setting styles/legends is API‑centric and easy once plotting basics are known.*

2. Visualizing Higher‑Dimensional Data by Slicing/Projection — **Difficulty: 2**
   - Reduce 3D+ data via slicing, projection, or collapse dimensions and present results across multiple axes or animated frames.
   - *Requires thinking about dimensionality reduction and arranging multiple views or animations.*

3. True‑Color (RGB) Image Handling — **Difficulty: 2**
   - Read, construct, and display M×N×3 RGB images with imread/image/imshow, manipulate color channels, and manage datatypes correctly.
   - *Reading/displaying RGB images is straightforward; careful handling of datatypes and channel manipulation adds modest complexity.*

4. Indexed Images and Colormaps — **Difficulty: 2**
   - Work with indexed images plus colormap, map indices to colors, change colormaps, and use imagesc/colormap for scaled visualization.
   - *Understanding indexed representations and colormap mapping is a new concept but follows clear APIs (imagesc, colormap).*

5. Grayscale and Intensity Image Processing — **Difficulty: 2**
   - Display and process single‑channel images, adjust contrast (imadjust or display options), and convert between grayscale and RGB forms.
   - *Basic display and contrast adjustments are simple; conversions and perceptual considerations add nuance.*

6. Image I/O and Metadata — **Difficulty: 1**
   - Read/write images with imread/imwrite, query size/class/alpha channels, and handle format and color‑space differences.
   - *imread/imwrite and querying size/class are routine tasks with predictable behavior.*

7. 3‑D Line Plots and Trajectories — **Difficulty: 2**
   - Plot trajectories with plot3, control view angles with view, add markers/lighting, and combine 3D lines with other 3D graphics.
   - *plot3 and view control are easy; meaningful 3D composition and interpretation require more practice.*

8. Regular Grid Evaluation and Surface Plots — **Difficulty: 2**
   - Create grids with meshgrid/ndgrid, evaluate functions on grids, and visualize with surf/mesh/contour while respecting axis scaling and CDataMapping.
   - *meshgrid + surf/contour use is straightforward, but attention to axis scaling and CData mapping is necessary.*

9. Triangulation and Irregular Mesh Visualization — **Difficulty: 3**
   - Represent irregular samples with delaunayTriangulation/triangulation, visualize with trisurf/trimesh, and interpolate scalar fields on triangles.
   - *Delaunay triangulation and interpolation on irregular meshes involve geometry and interpolation concepts that are more advanced.*

10. Surface Shading, Lighting, and Rendering Options — **Difficulty: 3**
    - Produce detailed surface visuals using shading, lighting, light objects, and colormap/CData settings to convey scalar values effectively.
    - *Lighting, shading, and rendering settings interact subtly; producing effective visuals requires experience.*

11. Scatter Plots and Multivariate Glyph Encoding — **Difficulty: 2**
    - Create scatter/scatter3 plots, map data dimensions to marker color/size/alpha, add colorbars/marginals, and interpret multivariate point clouds.
    - *Creating scatter/scatter3 with mapped color/size/alpha is accessible; designing clear multivariate encodings needs judgment.*
