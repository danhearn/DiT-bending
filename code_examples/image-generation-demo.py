import torch
import gradio as gr
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained("stabilityai/stable-diffusion-3-medium-diffusers", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

generator = torch.Generator(device="cuda").manual_seed(42)

transformer = pipe.transformer 

max_blocks = len(transformer.transformer_blocks)

def register_hooks(block_idx, q_scale, k_scale, v_scale, ff_scale, noise, noise_scale):
    handles = []

    def make_hook(scale):
        def hook(module, input, output):
            out = output * scale
            if noise:
                out = out + torch.randn_like(output) * noise_scale
            return out
        return hook

    blk = transformer.transformer_blocks[block_idx]
    handles.append(blk.attn.add_q_proj.register_forward_hook(make_hook(q_scale)))
    handles.append(blk.attn.add_k_proj.register_forward_hook(make_hook(k_scale)))
    handles.append(blk.attn.add_v_proj.register_forward_hook(make_hook(v_scale)))
    handles.append(blk.ff.register_forward_hook(make_hook(ff_scale)))

    return handles

def generate_image(prompt, block, q_scale, k_scale, v_scale, ff_scale, noise_toggle, noise_amount):
    handles = register_hooks(
        block_idx=block,
        q_scale=q_scale,
        k_scale=k_scale,
        v_scale=v_scale,
        ff_scale=ff_scale,
        noise=noise_toggle,
        noise_scale=noise_amount
    )

    generator = torch.Generator(device="cuda").manual_seed(42)

    image = pipe(
        prompt,
        negative_prompt="anthropomorphic, cartoon, anime, low quality, blurry, bad anatomy, bad hands, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality",
        num_inference_steps=20,
        guidance_scale=8.0,
        width=512,
        height=512,
        generator=generator,
    ).images[0]
    
    for h in handles:
        h.remove()

    return image

with gr.Blocks() as demo:
    gr.Markdown("## Stable Diffusion Transformer Hook Playground")

    with gr.Row():
        prompt = gr.Textbox(label="Prompt", value="A futuristic cityscape at night")

    with gr.Row():
        block = gr.Slider(0, 23, value=5, step=1, label="Transformer Block")

    with gr.Row():
        q_scale = gr.Slider(0.0, 5.0, value=1.0, step=0.1, label="Q Scale")
        k_scale = gr.Slider(0.0, 5.0, value=1.0, step=0.1, label="K Scale")
        v_scale = gr.Slider(0.0, 5.0, value=1.0, step=0.1, label="V Scale")
        ff_scale = gr.Slider(0.0, 5.0, value=1.0, step=0.1, label="FeedForward Scale")

    with gr.Row():
        noise_toggle = gr.Checkbox(label="Add Noise?")
        noise_amount = gr.Slider(0.0, 3.0, value=1.5, step=0.1, label="Noise Amount")

    with gr.Row():
        generate_btn = gr.Button("Generate")

    image_output = gr.Image(label="Generated Image", type="pil")

    generate_btn.click(
        fn=generate_image,
        inputs=[prompt, block, q_scale, k_scale, v_scale, ff_scale, noise_toggle, noise_amount],
        outputs=image_output
    )

demo.launch(share=True, inbrowser=True)