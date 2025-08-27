import requests
from utils.config import HF_API_KEY

def generate_image(prompt, save_path="ai_post.jpg"):
    url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    response = requests.post(url, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        return save_path
    else:
        print("Image generation failed:", response.text)
        return None
