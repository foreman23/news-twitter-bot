from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def scrapeHeadline():
    """
    Scrapes NBC News site for most recent headline
    """
    quote_page = 'https://www.nbcnews.com/'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    header = soup.find('div', attrs={'class': 'layout-grid-container'}).find('a')
    headerText = header.text.strip()

    # Convert headerText string to json
    data = {
        "text": headerText,
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj
