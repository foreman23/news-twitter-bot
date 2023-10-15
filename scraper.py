from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import json

import time


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

    # Download article image temporarily
    image_tag = article.find('img', attrs={'class': 'rms_img'})
    image_link = 'https://th.bing.com' + image_tag.get('src')

    urlretrieve(image_link, "./images/source.jpg")

    # Convert headerText string to json
    data = {
        "text": f"{header}\n{link}",
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj
