from requests_oauthlib import OAuth1Session
import re
import tweepy
import os
from dotenv import load_dotenv
import json
from artgen import genArtFromHeadline

# Stage the keys from the environment variables
load_dotenv()
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)


def post_tweet(headline):

    # Generate art from headline
    genArtFromHeadline(headline)

    # Post generated image and text headline to Twitter
    payload = upload_media(headline["text"])
    response = oauth.post("https://api.twitter.com/2/tweets", json=payload)
    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    # print("Response code: {}".format(response.status_code))
    json_response = response.json()
    # print(json.dumps(json_response, indent=4, sort_keys=True))


def upload_media(headline):
    tweepy_auth = tweepy.OAuth1UserHandler(
        "{}".format(os.getenv("CONSUMER_KEY")),
        "{}".format(os.getenv("CONSUMER_SECRET")),
        "{}".format(os.getenv("ACCESS_TOKEN")),
        "{}".format(os.getenv("ACCESS_TOKEN_SECRET")),
    )
    tweepy_api = tweepy.API(tweepy_auth)
    post = tweepy_api.simple_upload("./images/v1_txt2img_0.png")
    text = str(post)
    media_id = re.search("media_id=(.+?),", text).group(1)
    payload = {"text": headline, "media": {"media_ids": ["{}".format(media_id)]}}
    return payload
