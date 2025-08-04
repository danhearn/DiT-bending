# Surfacing Control: Targeted Interventions in DiT Models for Creative Expression in Multiple Domains

This repository contains the official supplementary code for:

**Surfacing Control: Targeted Interventions in DiT Models for Creative Expression in Multiple Domains**

## Links
- [Supplementary Images & Audio](https://danhearn.github.io/DiT-bending/) (GitHub Pages)
- [Stable Diffusion 3.0 Medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium)
- [Stable Audio Open Small](https://huggingface.co/stabilityai/stable-audio-open-small)

## Running Audio Experiments
To install requirements for audio experiments:

```bash
pip install -r code_examples/audio-requirements.txt
```

To generate audio with custom hooks and reproduce the supplementary material:

```bash
python audio-generation-demo.py
```

in `code_examples/`. You can modify the script to use your own prompts and parameter settings.

## Running Image Experiments
1. Install requirements for image experiments:

```bash
pip install -r code_examples/image-requirements.txt
```

2. Run gradio demo:

```bash
python image-generation-demo.py
```

in `code_examples/`. You can modify the script to use your own prompts and parameter settings.

## Repo Contents

- `code_examples/` — Example scripts and demos for running and modifying the models
- `generated_audio/` — Example audio outputs generated with Stable Audio Small (WAV)
- `generated_images/` — Example images generated with SD-3-medium (PNG)
- `audio-requirements.txt` — Python dependencies for running the audio code
- `image-requirements.txt` — Python dependencies for running the image code
- `index.html` & `_config.yml` - html file and configuration for GitHub Pages.

