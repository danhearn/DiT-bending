# Surfacing Control: Targeted Interventions in DiT Models for Creative Expression in Multiple Domains

This repository contains the official supplementary code, audio, and images for the paper:

**Surfacing Control: Targeted Interventions in DiT Models for Creative Expression in Multiple Domains**



## Requirements

To install requirements for audio experiments:

```bash
pip install -r code_examples/audio-requirements.txt
```

To install requirements for image experiments:

```bash
pip install -r code_examples/image-requirements.txt
```

## Running Audio Experiments

To generate audio with custom hooks and reproduce the supplementary material:

```bash
python audio-generation-demo.py
```

in `code_examples/`. You can modify the script to use your own prompts and parameter settings.

## Running Image Experiments

To generate images and spectrograms:

```bash
python image-generation-demo.py
```

in `code_examples/`. You can modify the script to use your own prompts and parameter settings.

## Contents

- `code_examples/` — Example scripts and demos for running and modifying the models
- `generated_audio/` — Example audio outputs (WAV)
- `generated_images/` — Example spectrograms and visualizations (PNG)
- `audio-requirements.txt` — Python dependencies for running the audio code
- `image-requirements.txt` — Python dependencies for running the image code

## Parameter Settings for Generated Audio

The following describes the parameter settings and sweep structure used for the audio grids in the `generated_audio/` or `audio_grids/` folder:

### Parameter Sweeps (by_param)
**Folder:** `audio_grids/{param}/by_param/`

- **Target block:** 8 (or 12)
- **Prompt:** "techno beat 100bpm"
- **Steps:** 8
- **CFG scale:** 1.0
- **Sampler:** pingpong
- **Audio duration:** 15 seconds
- **Parameter values:**
    - self_attn: [0.5, 1.0, 2.0, 3.0]
    - cross_attn: [0.5, 1.0, 2.0, 3.0]
    - cross_q: [0.5, 1.0, 2.0, 3.0]
    - cross_kv: [0.5, 1.0, 2.0, 4.0]
    - ff: [0.5, 1.0, 2.0, 3.0]
- **Noise values:** [0.0, 0.5, 1.0, 1.5]
- **Each grid cell:** unique (parameter_value, noise_value) pair for the given parameter at block 8.

### Block Sweeps (by_layer)
**Folder:** `audio_grids/{param}/by_layer/`

- **Blocks:** 0 to 15 (all transformer layers)
- **Parameter value:** 2.0
- **Noise value:** 0.5
- **Other settings:** as above
- **Each file:** one block, fixed parameter and noise value for the given parameter.

### All-Hooks Combos
**Folder:** `audio_grids/combos/`

- **All hooks active** (self_attn, cross_attn, cross_q, cross_kv, ff)
- **Block:** 8 (or 12)
- **Parameter values:** [1.0, 2.0]
- **Noise values:** [0.0, 1.0]
- **Other settings:** as above

## Parameter Settings for Generated Images

The following describes the parameter settings used for each image grid in the `generated_images/` folder:


### Combined Scaling Grids

<p align="center">
  <img src="generated_images/k_hook_combined_scaling_grid.png" width="400" alt="k_hook_combined_scaling_grid">
</p>
<p align="center"><b>k_hook_combined_scaling_grid.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: k, Parameter scales (rows): [1.0, 0.5, 1.5, 2.5], Noise scales (columns): [0.0, 0.5, 1.0, 1.5]</p>

<p align="center">
  <img src="generated_images/v_hook_combined_scaling_grid.png" width="400" alt="v_hook_combined_scaling_grid">
</p>
<p align="center"><b>v_hook_combined_scaling_grid.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: v, Parameter scales (rows): [1.0, 0.5, 1.5, 2.5], Noise scales (columns): [0.0, 0.5, 1.0, 1.5]</p>

<p align="center">
  <img src="generated_images/q_hook_combined_scaling_grid.png" width="400" alt="q_hook_combined_scaling_grid">
</p>
<p align="center"><b>q_hook_combined_scaling_grid.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: q, Parameter scales (rows): [1.0, 0.5, 1.5, 2.5], Noise scales (columns): [0.0, 0.5, 1.0, 1.5]</p>

<p align="center">
  <img src="generated_images/ff_hook_combined_scaling_grid.png" width="400" alt="ff_hook_combined_scaling_grid">
</p>
<p align="center"><b>ff_hook_combined_scaling_grid.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: ff, Parameter scales (rows): [1.0, 0.5, 1.5, 2.5], Noise scales (columns): [0.0, 0.5, 1.0, 1.5]</p>

<p align="center">
  <img src="generated_images/all_hooks_combined_scaling_grid.png" width="400" alt="all_hooks_combined_scaling_grid">
</p>
<p align="center"><b>all_hooks_combined_scaling_grid.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameters: all hooks, Parameter scales (rows): [1.0, 0.5, 1.5, 2.5], Noise scales (columns): [0.0, 0.5, 1.0, 1.5]</p>

### Paper Figure 2 (Hook Comparison Grid)

<p align="center">
  <img src="generated_images/hook_comparison.png" width="600" alt="hook_comparison">
</p>
<p align="center"><b>hook_comparison.png</b><br>
Target block: 12, Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter scale: 1.0, Noise scale: 1.5 (except first image: base), Hooks: base, k, v, q, ff, all (left to right)</p>

### Block Comparison Rows

<p align="center">
  <img src="generated_images/k_hook_block_comparison_row.png" width="600" alt="k_hook_block_comparison_row">
</p>
<p align="center"><b>k_hook_block_comparison_row.png</b><br>
Target blocks: 4, 8, 12, 18 (left to right), Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: k, Parameter scale: 2.0, Noise scale: 0.0</p>

<p align="center">
  <img src="generated_images/v_hook_block_comparison_row.png" width="600" alt="v_hook_block_comparison_row">
</p>
<p align="center"><b>v_hook_block_comparison_row.png</b><br>
Target blocks: 4, 8, 12, 18 (left to right), Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: v, Parameter scale: 2.0, Noise scale: 0.0</p>

<p align="center">
  <img src="generated_images/q_hook_block_comparison_row.png" width="600" alt="q_hook_block_comparison_row">
</p>
<p align="center"><b>q_hook_block_comparison_row.png</b><br>
Target blocks: 4, 8, 12, 18 (left to right), Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: q, Parameter scale: 2.0, Noise scale: 0.0</p>

<p align="center">
  <img src="generated_images/ff_hook_block_comparison_row.png" width="600" alt="ff_hook_block_comparison_row">
</p>
<p align="center"><b>ff_hook_block_comparison_row.png</b><br>
Target blocks: 4, 8, 12, 18 (left to right), Prompt: "A portrait photograph of a person smiling", Guidance scale: 4.0, Steps: 20, Parameter: ff, Parameter scale: 2.0, Noise scale: 0.0</p>


## Audio Examples

Below are audio grids for each parameter sweep (by_param) and all-hooks combos. Each cell is an audio player with a caption describing the parameters applied.

### Parameter Sweeps (by_param)

#### self_attn

<table>
  <tr>
    <th></th><th>noise 0.0</th><th>noise 0.5</th><th>noise 1.0</th><th>noise 1.5</th>
  </tr>
  <tr>
    <td>param 0.5</td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param0.5_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param0.5_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param0.5_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param0.5_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 1.0</td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param1.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param1.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param1.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 2.0</td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param2.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param2.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param2.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 10.0</td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param10.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param10.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param10.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/self_attn/by_param/block8_param10.0_noise1.5.wav"></audio></td>
  </tr>
</table>

#### cross_attn

<table>
  <tr>
    <th></th><th>noise 0.0</th><th>noise 0.5</th><th>noise 1.0</th><th>noise 1.5</th>
  </tr>
  <tr>
    <td>param 0.5</td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param0.5_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param0.5_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param0.5_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param0.5_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 1.0</td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param1.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param1.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param1.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 2.0</td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param2.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param2.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param2.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 10.0</td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param10.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param10.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param10.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_attn/by_param/block8_param10.0_noise1.5.wav"></audio></td>
  </tr>
</table>

#### cross_q

<table>
  <tr>
    <th></th><th>noise 0.0</th><th>noise 0.5</th><th>noise 1.0</th><th>noise 1.5</th>
  </tr>
  <tr>
    <td>param 0.5</td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param0.5_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param0.5_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param0.5_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param0.5_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 1.0</td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param1.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param1.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param1.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 2.0</td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param2.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param2.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param2.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 10.0</td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param10.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param10.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param10.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_q/by_param/block8_param10.0_noise1.5.wav"></audio></td>
  </tr>
</table>

#### cross_kv

<table>
  <tr>
    <th></th><th>noise 0.0</th><th>noise 0.5</th><th>noise 1.0</th><th>noise 1.5</th>
  </tr>
  <tr>
    <td>param 0.5</td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param0.5_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param0.5_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param0.5_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param0.5_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 1.0</td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param1.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param1.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param1.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 2.0</td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param2.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param2.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param2.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 4.0</td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param4.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param4.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param4.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/cross_kv/by_param/block8_param4.0_noise1.5.wav"></audio></td>
  </tr>
</table>

#### ff

<table>
  <tr>
    <th></th><th>noise 0.0</th><th>noise 0.5</th><th>noise 1.0</th><th>noise 1.5</th>
  </tr>
  <tr>
    <td>param 0.5</td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param0.5_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param0.5_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param0.5_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param0.5_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 1.0</td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param1.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param1.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param1.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 2.0</td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param2.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param2.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param2.0_noise1.5.wav"></audio></td>
  </tr>
  <tr>
    <td>param 3.0</td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param3.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param3.0_noise0.5.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param3.0_noise1.0.wav"></audio></td>
    <td><audio controls src="generated_audio/ff/by_param/block8_param3.0_noise1.5.wav"></audio></td>
  </tr>
</table>

### All-Hooks Combo

<table>
  <tr>
    <th>param \ noise</th><th>0.0</th><th>1.0</th>
  </tr>
  <tr>
    <td>1.0</td>
    <td><audio controls src="generated_audio/combos/allhooks_block8_param1.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/combos/allhooks_block8_param1.0_noise1.0.wav"></audio></td>
  </tr>
  <tr>
    <td>2.0</td>
    <td><audio controls src="generated_audio/combos/allhooks_block8_param2.0_noise0.0.wav"></audio></td>
    <td><audio controls src="generated_audio/combos/allhooks_block8_param2.0_noise1.0.wav"></audio></td>
  </tr>
</table>

## Pre-trained Models

Stable Diffusion 3.0 Medium

Stable Audio Small
