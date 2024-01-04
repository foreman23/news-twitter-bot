from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import json
from PIL import Image
from gethashtag import getHashtagFromHeaderNBA


def scrapeFox():
    """
    Scrapes Fox News site for most recent headline
    """
    quote_page = 'https://www.foxnews.com/'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # Find Header text
    header = soup.find('h3', attrs={'class': 'title'}).find('a')
    headerText = header.text.strip()

    # Find link to article
    href = header.get('href')

    # Convert headerText string to json
    data = {
        "text": f"{headerText}\n{href}",
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj


def scrapeBingNews():
    """
    Scrapes Bing news site for most recent headline
    """
    quote_page = 'https://www.bing.com/news'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # Find Header Text
    article = soup.find('div', attrs={'class': 'news-card'})
    header = article.get('data-title')
    link = article.get('data-url')

    # Convert headerText string to json
    data = {
        "text": f"{header}\n{link}",
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj


def scrapeBingNBA():
    """
    Scrapes Bing news for nba related articles
    """
    quote_page = 'https://www.bing.com/news/search?q=NBA+News&qft=interval%3d%224%22&form=YFNR'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # Find Header Text
    article = soup.find('div', attrs={'class': 'news-card'})
    header = article.get('data-title')
    link = article.get('data-url')

    # Download article image as source
    image_tag = article.find('img', attrs={'class': 'rms_img'})
    image_link = 'https://th.bing.com' + image_tag.get('src')

    urlretrieve(image_link, "./images/source.jpg")

    # Resize image to square (512x512)
    image_to_upscale = Image.open('./images/source.jpg')
    target_size = (512, 512)
    original_width, original_height = image_to_upscale.size
    width_ratio = target_size[0] / original_width
    heigh_ratio = target_size[1] / original_height
    resize_ratio = min(width_ratio, heigh_ratio)
    new_width = int(original_width * resize_ratio)
    new_height = int(original_height * resize_ratio)
    resized_image = image_to_upscale.resize((new_width, new_height))
    background = Image.new("RGB", target_size)
    paste_x = (target_size[0] - new_width) // 2
    paste_y = (target_size[1] - new_height) // 2
    background.paste(resized_image, (paste_x, paste_y))
    background.save('./images/source.jpg')
    image_to_upscale.close()

    # Convert headerText string to json
    data = {
        "text": f"{header}\n{link}",
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj


def scrapeYahooNBA():
    """
    Scrapes yahoo news for nba related articles
    """
    quote_page = 'https://sports.yahoo.com/nba/'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    # Find Header Text
    article = soup.find('div', attrs={'class': 'Cf'}).find('a')
    header = article.text.strip()
    link = article.get('href')
    # print(header)
    # print(link)

    # Download article image as source
    image_tag = soup.find('img', attrs={'class': 'W(100%)'})
    image_link = image_tag.get('src')
    # print(image_link)

    urlretrieve(image_link, "./images/source.jpg")

    # Resize image to square (512x512)
    image_to_upscale = Image.open('./images/source.jpg')
    target_size = (512, 512)
    original_width, original_height = image_to_upscale.size
    width_ratio = target_size[0] / original_width
    heigh_ratio = target_size[1] / original_height
    resize_ratio = min(width_ratio, heigh_ratio)
    new_width = int(original_width * resize_ratio)
    new_height = int(original_height * resize_ratio)
    resized_image = image_to_upscale.resize((new_width, new_height))
    background = Image.new("RGB", target_size)
    paste_x = (target_size[0] - new_width) // 2
    paste_y = (target_size[1] - new_height) // 2
    background.paste(resized_image, (paste_x, paste_y))
    background.save('./images/source.jpg')
    image_to_upscale.close()

    # Generate Hashtag from headline if possible
    hashtagArr = getHashtagFromHeaderNBA(header)
    hashtag1 = "#NBA"

    # Convert headerText string to json
    data = {
        "text": f"{header}\n{hashtag1}\n{link}",
    }
    if len(hashtagArr) == 1:
        hashtag2 = hashtagArr[0]
        data = {
            "text": f"{header}\n{hashtag1} {hashtag2}\n{link}",
        }
    if len(hashtagArr) >= 2:
        hashtag2 = hashtagArr[0]
        hashtag3 = hashtagArr[1]
        data = {
            "text": f"{header}\n{hashtag1} {hashtag2} {hashtag3}\n{link}",
        }

    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj
