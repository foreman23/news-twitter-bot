import time
# from scraper import scrapeBingNews
from scraper import scrapeYahooNBA
from tweet import post_tweet


def checkForUpdates():
    """
    Checks for headline updates every X seconds
    """
    prevHeadline = None
    timeLastUpdated = None
    initialCheckFlag = True
    while True:
        print("\n---------------------")
        print(time.ctime())
        print("Last Update:", timeLastUpdated)
        print("Scraping headline...\n")
        headline = scrapeYahooNBA()
        if headline["text"] != prevHeadline:
            try:
                headline["text"].encode("latin-1")
                if prevHeadline is not None:
                    print("Old headline:", prevHeadline)
                    print("New headline:", headline["text"])
                    prevHeadline = headline["text"]
                    print("POSTING TWEET")
                    post_tweet(headline)
                    timeLastUpdated = time.ctime()

                if headline["text"] is None:
                    print("ERROR scraping headline")

                elif initialCheckFlag and prevHeadline is None:
                    print("Old headline:", prevHeadline)
                    print("New headline:", headline["text"])
                    prevHeadline = headline["text"]
                    print("\nPOSTING TWEET")
                    post_tweet(headline)
                    initialCheckFlag = False
                    timeLastUpdated = time.ctime()
                else:
                    print("Old headline:", prevHeadline)
                    print("New headline:", headline["text"])
                    prevHeadline = headline["text"]

            except:
                print("ERROR headline contains bad character(s)")

        else:
            print("Headline has not changed")
        time.sleep(3600)


if __name__ == "__main__":
    checkForUpdates()
