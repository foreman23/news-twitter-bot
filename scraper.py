from bs4 import BeautifulSoup
from urllib.request import urlopen
import json


def scrapeHeadline():
    """
    Scrapes Fox News site for most recent headline
    """
    quote_page = 'https://www.reddit.com/r/worldnews/top/?t=hour'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    headers = soup.find_all('div', attrs={'class': 'text-18'})
    headerText = None
    for header in headers:
        if "Live Thread" not in header.text.strip():
            headerText = header.text.strip()
            break

    # Convert headerText string to json
    data = {
        "text": headerText,
    }
    jsonString = json.dumps(data)
    jsonObj = json.loads(jsonString)

    return jsonObj
