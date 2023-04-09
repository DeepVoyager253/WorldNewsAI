from newsapi import NewsApiClient
import os
import requests
import json
from trafilatura import extract
from dotenv import load_dotenv
load_dotenv()
class NewsScraper:
    def __init__(self, search_mode, topic=None, dntf=None, dntt=None, country=None, how_many=None, sort_by=None):
        if search_mode == "everything":
            self.search_mode = search_mode
        elif search_mode == "top":
            self.search_mode = "top-headlines"
        else:
            raise Exception("Invalid search mode Please insert \"top\" or \"everything\"")
        
        self.topic = topic
        self.dateAndTimeFrom = dntf
        self.dateAndTimeTo = dntt
        self.country = country
        self.pageAmount = how_many
        self.sort_by = sort_by
    def scrape(self):
        scraper = NewsApiClient(api_key=os.getenv('API-KEY'))
        if self.search_mode == "everything":
            scraped = scraper.get_everything(q=self.topic\
                                             , language='en'\
                                                , from_param=self.dateAndTimeFrom\
                                                , sort_by=self.sort_by\
                                                , to=self.dateAndTimeTo\
                                                , page_size=self.pageAmount\
                                             )
        else:
            # articles sorted by release date
            scraped = scraper.get_top_headlines(q=self.topic\
                                    , language='en'\
                                    , page_size=self.pageAmount\
                                    , country=self.country
                                    )
        return scraped['articles']

class NewsArticle:
    def __init__(self, article):
        self.article_json = article
    @property
    def full_content(self):
        url = self.article_json['url']        
        article_html = requests.get(url, timeout=None).text
        return extract(article_html)
    @property
    def source(self):
        return self.article_json["source"]['name']
    @property
    def title(self):
        return self.article_json['title']
    @property
    def description(self):
        return self.article_json['description']
if __name__ == "__main__":
    scraper = NewsScraper('top', how_many=1)
    article = NewsArticle(scraper.scrape()[0])
    print(article.source)        
