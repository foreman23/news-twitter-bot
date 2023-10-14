import time
from scraper import scrapeBingNews
from tweet import post_tweet


def checkForUpdates():
    """
    Checks for Fox News headline updates every 60 minutes
    """
    prevHeadline = None
    timeLastUpdated = None
    initialCheckFlag = True
    while True:
        print("\n---------------------")
        print(time.ctime())
        print("Last Update:", timeLastUpdated)
        print("Scraping headline...\n")
        headline = scrapeBingNews()
        if headline["text"] != prevHeadline:
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

        else:
            print("Headline has not changed")
        time.sleep(5200)


if __name__ == "__main__":
    checkForUpdates()
