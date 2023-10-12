import base64
import os
import requests
from dotenv import load_dotenv
from scraper import scrapeHeadline

load_dotenv()


def genArtFromHeadline(headline):
    engine_id = "stable-diffusion-512-v2-1"
    api_host = os.getenv('API_HOST')
    api_key = os.getenv("STABILITY_API_KEY")

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": "A lighthouse on a cliff"
                }
            ],
            "cfg_scale": 7,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 20,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(f"./images/v1_txt2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))


genArtFromHeadline(scrapeHeadline())
