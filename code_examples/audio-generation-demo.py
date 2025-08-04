import gradio as gr
import torch
import torchaudio
from einops import rearrange
from stable_audio_tools import get_pretrained_model
from stable_audio_tools.inference.generation import generate_diffusion_cond
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"
model, model_config = get_pretrained_model("stabilityai/stable-audio-open-small")
sample_rate = model_config["sample_rate"]
sample_size = model_config["sample_size"]
model = model.to(device)
transformer = model.model.model.transformer
num_layers = len(transformer.layers)

seed = np.random.randint(0, 2**31 - 1)

def generate_audio(prompt, block, cross_attn_scale, self_attn_scale, cross_q_scale, cross_kv_scale, ff_scale, noise, noise_scale):
    handles = []
    block = int(block)
    blk = transformer.layers[block]

    # Hooks
    def cross_q_hook(module, input, output):
        out = output * cross_q_scale
        if noise:
            out = out + torch.randn_like(out) * noise_scale
        return out

    def cross_kv_hook(module, input, output):
        out = output * cross_kv_scale
        if noise:
            out = out + torch.randn_like(out) * noise_scale
        return out

    def self_attn_hook(module, input, output):
        out = output * self_attn_scale
        if noise:
            out = out + torch.randn_like(out) * noise_scale
        return out

    def cross_attn_hook(module, input, output):
        out = output * cross_attn_scale
        if noise:
            out = out + torch.randn_like(out) * noise_scale
        return out

    def ff_hook(module, input, output):
        out = output * ff_scale
        if noise:
            out = out + torch.randn_like(out) * noise_scale
        return out

    # Register hooks
    handles.append(blk.cross_attn.to_q.register_forward_hook(cross_q_hook))
    handles.append(blk.cross_attn.to_kv.register_forward_hook(cross_kv_hook))
    handles.append(blk.self_attn.register_forward_hook(self_attn_hook))
    handles.append(blk.cross_attn.register_forward_hook(cross_attn_hook))
    handles.append(blk.ff.register_forward_hook(ff_hook))

    conditioning = [{
        "prompt": prompt,
        "seconds_total": 15
    }]
    output = generate_diffusion_cond(
        model,
        steps=8,
        cfg_scale=1.0,
        seed=seed,
        conditioning=conditioning,
        sample_size=sample_size,
        sampler_type="pingpong",
        device=device
    )

    for h in handles:
        h.remove()

    output = rearrange(output, "b d n -> d (b n)")
    output = output.to(torch.float32).div(torch.max(torch.abs(output))).clamp(-1, 1).mul(32767).to(torch.int16).cpu()
    torchaudio.save("gradio_output.wav", output, sample_rate)
    return "gradio_output.wav"

with gr.Blocks() as demo:
    gr.Markdown("## Stable Audio Small - Bending Demo")

    example_prompts = [
        "techno beat 808 140bpm",
        "ambient evolving drone",
        "glitchy percussion with reverb",
        "woman laughing",
        "child laughing",
        "sparse modular synth pulses",
        "birds in the jungle at dawn",
        "raging water droplet"
    ]

    with gr.Row():
        with gr.Column():

            prompt_mode = gr.Radio(["Example", "Custom"], value="Example", label="Prompt Mode")
            example_prompt = gr.Dropdown(example_prompts, value=example_prompts[0], label="Example Prompts", interactive=True)
            custom_prompt = gr.Textbox(label="Custom Prompt", value="", interactive=True, visible=False)
            block = gr.Slider(0, num_layers - 1, step=1, value=0, label="Transformer Block")
            
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Self Attention Scaling")
                    gr.Markdown("Adjust the scaling factors for self attention output.")
                    self_attn_scale = gr.Slider(0.1, 10.0, value=1.0, step=0.01, label="Self Attn Scale")

            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Cross Attention Scaling")
                    gr.Markdown("Adjust the scaling factors for cross attention mechanisms and/or cross attention output.")
                    with gr.Column():
                        cross_q_scale = gr.Slider(0.1, 10.0, value=1.0, step=0.1, label="Cross Q Scale")
                        cross_kv_scale = gr.Slider(0.1, 4.0, value=1.0, step=0.1, label="Cross KV Scale")

                    with gr.Column():
                        cross_attn_scale = gr.Slider(0.1, 10.0, value=1.0, step=0.01, label="Cross Attn Scale")
                
            


        with gr.Column():
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Feedforward Scaling")
                    gr.Markdown("Adjust the scaling factor for feedforward output.")
                    ff_scale = gr.Slider(0.1, 3.0, value=1.0, step=0.1, label="Feedforward Scale")
            with gr.Row():
                with gr.Column():
                    gr.Markdown("### Noise Injection")
                    gr.Markdown("Noise of the same shape is added to all attention and feedforward outputs.")
                    noise = gr.Checkbox(label="Inject Noise", value=False)
                    noise_scale = gr.Slider(0.0, 2.0, value=0.5, label="Noise Scale")
            with gr.Column():
                gr.Markdown("### Output")
                out = gr.Audio(label="Generated Audio")
                btn = gr.Button("Generate")

    # Toggle visibility of prompt inputs
    def toggle_prompt_inputs(mode):
        return (
            gr.update(visible=mode == "Example"),
            gr.update(visible=mode == "Custom")
        )

    prompt_mode.change(
        toggle_prompt_inputs,
        inputs=prompt_mode,
        outputs=[example_prompt, custom_prompt]
    )

    # Choose which prompt to use
    def get_prompt(prompt_mode, example_prompt, custom_prompt):
        return example_prompt if prompt_mode == "Example" else custom_prompt

    btn.click(
        fn=lambda prompt_mode, example_prompt, custom_prompt, block, cross_attn_scale, self_attn_scale, cross_q_scale, cross_kv_scale, ff_scale, noise, noise_scale:
            generate_audio(
                get_prompt(prompt_mode, example_prompt, custom_prompt),
                block,
                cross_attn_scale,
                self_attn_scale,
                cross_q_scale,
                cross_kv_scale,
                ff_scale,
                noise,
                noise_scale
            ),
        inputs=[prompt_mode, example_prompt, custom_prompt, block, cross_attn_scale, self_attn_scale, cross_q_scale, cross_kv_scale, ff_scale, noise, noise_scale],
        outputs=out
    )

demo.launch(share=True, inbrowser=True)