# Akatz Loop Nodes for ComfyUI

Custom nodes for loops, flow control, lazy switches, image processing, and latent manipulation.

## Node Categories

### Flow Control
- **WhileLoopOpen/Close** - While loop with condition checking
- **ForLoopOpen/Close** - For loop with iteration counter
- **ExecutionBlocker** - Conditionally block execution

### Logic (Lazy Nodes)
- **LazySwitch** - Switch between inputs based on condition
- **LazyIndexSwitch** - Switch between multiple inputs by index
- **LazyMixImages** - Blend images based on condition
- **LazyConditional** - Conditional value selection

### Accumulation & Lists
- **AccumulateNode** - Accumulate values across iterations
- **AccumulationHead/Tail** - Get first/last from accumulation
- **AccumulationToList/ListToAccumulation** - Convert between types
- **AccumulationGetLength/GetItem/SetItem** - Manipulation utilities
- **MakeListNode** - Create lists from values
- **GetFloatFromList/GetIntFromList** - Extract values
- **IntegerListGeneratorNode** - Generate integer sequences

### Utility
- **SamplerSelector** - Select samplers with override
- **SchedulerSelector** - Select schedulers with override
- **StringToCombo** - Convert strings to combo type
- **DebugPrint** - Debug output

### Image
- **ColorCorrection** - Adaptive saturation and white balance
- **AdaptiveSharpening** - Edge-aware sharpening
- **ColorCorrectionAndSharpening** - Combined processor
- **SmartLoopPreviewImage** - Preview with loop iteration accumulation

### Latent
- **SeedInterpNoise** - Interpolated noise with SLERP/LERP
- **PrepareLatentDenoise** - Prepare latents for denoising

## Credits

Based on execution inversion concepts from https://github.com/BadCafeCode/execution-inversion-demo-comfyui
