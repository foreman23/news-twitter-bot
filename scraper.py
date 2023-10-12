from bs4 import BeautifulSoup
from urllib.request import urlopen


def scrapeHeadline():
    """
    Scrapes NBC News site for most recent headline.
    """
    quote_page = 'https://www.nbcnews.com/'
    page = urlopen(quote_page)

    soup = BeautifulSoup(page, 'html.parser')

    subheader = soup.find('div', attrs={'class': 'layout-grid-container'}).find('a')
    subtext = subheader.text.strip()
    return subtext


print(scrapeHeadline())
