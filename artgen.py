import base64
import os
import requests
from dotenv import load_dotenv
from scraper import scrapeHeadline
import math

load_dotenv()


def genArtFromHeadline(headline):
    headline = headline["text"]
    engine_id = "stable-diffusion-512-v2-1"
    api_host = os.getenv('API_HOST')
    api_key = os.getenv("STABILITY_API_KEY")

    if api_key is None:
        raise Exception("Missing Stability API key.")

    # Generate art
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
                    "text": headline
                }
            ],
            "cfg_scale": 7,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 20,
            "style_preset": "digital-art",
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(f"./images/v1_txt2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))

    # Check remaining credit balance after operation
    url = f"{api_host}/v1/user/balance"
    balance = requests.get(url, headers={
        "Authorization": f"Bearer {api_key}"
    })

    if balance.status_code != 200:
        raise Exception("Non-200 response: " + str(balance.text))

    currentBalance = balance.json()
    print("Credits remaining:", currentBalance["credits"])
    print("~", math.floor(float(currentBalance["credits"] * 5)), "images")
