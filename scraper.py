import urllib.request
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, site):
        self.site = site
        print(self.site)

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if 'http' in url:
                print("\n " + url)


Scraper('https://news.google.com/').scrape()

Scraper('https://www.pravda.com.ua').scrape()
