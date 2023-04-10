import os
from django.shortcuts import render
from django.http import HttpResponse
from . import api
from dotenv import load_dotenv
load_dotenv()
def index(request):
    scraper = api.NewsScraper("top", os.getenv("NEWS-KEY"), how_many=3, sort_by='Popularity')
    articles = scraper.scrape()
    title_list = []
    for article in articles:
        title_list.append(api.NewsArticle(article).title)
    return HttpResponse('<br>'.join(title_list))