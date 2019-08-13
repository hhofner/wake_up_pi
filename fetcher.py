'''
Here are all classes that fetch data from the internet, called 'Fetchers'.
'''
import feedparser #for RSS feeds

class Fetcher():
    def __init__(self, URL):
        if not isinstance(URL, list):
            raise Exception('Expecting list of strings for URL') #TODO: check if the URLs exists
        self.URL = URL

    def fetch_and_return(self):
        '''
        Fetch stuff
        '''
        pass

class RSSFeedFetcher(Fetcher):
    def __init__(self, URL, max_feeds):
        '''
        :param count: number of headlines to fetch
        '''
        super().__init__(URL)
        self.maximum_feeds = max_feeds

        self.headlines = {}

    def _parse_feed(self):
        for url in self.URL:
            try:
                RSS = feedparser.parse(url)
            except:
                raise #TODO: return some type of error message to be spoken
            else:
                # Count how many feed titles are parsed
                parsed_feed_count = 0
                info = (RSS.feed.title, RSS.feed.language)
                self.headlines[info] = []
                for entry in RSS.entries:
                    if parsed_feed_count > self.maximum_feeds:
                        break
                    self.headlines[info].append(entry.title)
                    parsed_feed_count += 1

    def fetch_and_return(self):
        self._parse_feed()
        return self.headlines

if __name__ == "__main__":
    testFeedFetcher = RSSFeedFetcher(["http://rss.kicker.de/news/fussball", "https://rss.nytimes.com/services/xml/rss/nyt/US.xml"], 5)
    print(testFeedFetcher.fetch_and_return())
