# GLSL

Baseline: the Khronos OpenGL Shading Language specification for the declared `#version`, plus the renderer's existing shader and uniform conventions.

- Keep vertex attributes, uniform block layout, and shader inputs and outputs consistent with the CPU structures and paired shader stage.
- Use explicit types and initialize outputs on every live path. Bound loops and avoid undefined functions, division by zero, and nonfinite values.
- Keep coordinate spaces and blend mode assumptions clear. Preserve depth, alpha, and culling behavior expected by the render pass.
- Validate changed shaders with `glslangValidator` when available, then inspect them in the target OpenGL runtime; offline validation alone cannot prove visual correctness.
