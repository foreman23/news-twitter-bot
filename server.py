import time
from scraper import scrapeHeadline


def checkForUpdates():
    """
    Checks for FOX news headline updates every 30 minutes
    """
    prevHeadline = None
    while True:
        print("\n" + time.ctime())
        print("Scraping headline...")
        headline = scrapeHeadline()
        print(headline["text"])
        if headline["text"] != prevHeadline:
            print("Old headline:", prevHeadline)
            print("New headline:", headline["text"])
            prevHeadline = headline["text"]
        else:
            print("Headline has not changed")
        time.sleep(1200)


if __name__ == "__main__":
    checkForUpdates()