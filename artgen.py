import base64
import os
import requests
from dotenv import load_dotenv
import math
# from scraper import scrapeBingNBA
from scraper import scrapeYahooNBA
from PIL import Image

load_dotenv()


def genArtFromHeadline(headline):
    """
    Generates text-to-image from a news headline
    """
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
                    "text": f"{headline}, (art by Hayao Miyazaki), good anatomy"
                }
            ],
            "cfg_scale": 4.5,
            "height": 512,
            "width": 512,
            "samples": 1,
            "steps": 20,
            "style_preset": "anime",
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


def genArtFromImageNBA(headline):
    """
    Generates image-to-image from NBA news headline & thumbnail
    """
    headline = headline["text"]
    engine_id = "stable-diffusion-512-v2-1"
    api_host = os.getenv("API_HOST")
    api_key = os.getenv("STABILITY_API_KEY")

    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/image-to-image",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        files={
            "init_image": open("./images/source.jpg", "rb")
        },
        data={
            "image_strength": 0.6,
            "init_image_mode": "IMAGE_STRENGTH",
            "text_prompts[0][text]": f"{headline}, ((anime))",
            "cfg_scale": 7,
            "samples": 1,
            "steps": 20,
        }
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for i, image in enumerate(data["artifacts"]):
        with open(f"./images/v1_img2img_{i}.png", "wb") as f:
            f.write(base64.b64decode(image["base64"]))

    # Resize image to crop black edges (512x296)
    image_to_upscale = Image.open('./images/v1_img2img_0.png')
    target_size = (512, 286)
    original_width, original_height = image_to_upscale.size
    crop_x = 0  # Left edge
    crop_y = (original_height - target_size[1]) // 2  # Center vertically
    crop_width = target_size[0]
    crop_height = target_size[1]
    cropped_image = image_to_upscale.crop((crop_x, crop_y, crop_x + crop_width, crop_y + crop_height))
    cropped_image.save('./images/v1_img2img_0.png')
    image_to_upscale.close()

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


genArtFromHeadline(scrapeYahooNBA())
