import os
import uuid
import requests
import time
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
import base64

load_dotenv()

def generate_images_from_keywords(keywords):

    images_dir = Path("images")

    results = {}
    total_keywords = len(keywords)

    client = OpenAI(
        base_url="https://api.studio.nebius.com/v1/",
        api_key=os.environ.get("NEBIUS_API_KEY"), 
    )


    for idx, keyword in enumerate(keywords, start=1):
        prompt = keyword 

        response = client.images.generate(
            model="black-forest-labs/flux-dev",
            prompt=prompt,
            n=1,
            response_format="b64_json",
            extra_body={
                "response_extension": "png",
                "width": 1080,
                "height": 1920,
                "num_inference_steps": 16,
                "negative_prompt": "",
                "seed": -1
            }
        )

        image_b64 = response.data[0].b64_json

        image_data = base64.b64decode(image_b64)
        filename = f"{idx:02d}.png"
        img_path = images_dir / filename
        with open(img_path, "wb") as f:
            f.write(image_data)
        results[keyword] = str(img_path)

    return results


if __name__ == "__main__":
    keywords = ['Man leaving everything behind, faith in God, serene path', 'Abraham standing on the mountainside, divine promise, faith journey']
    generate_images_from_keywords(keywords)