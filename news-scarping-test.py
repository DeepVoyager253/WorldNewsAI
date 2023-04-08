import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


# set API endpoint URL and API key
url = "https://newsapi.org/v2/top-headlines"
api_key = os.getenv("API-KEY")

# set search parameters
country = ""
topic = "ChatGPT"

# construct request URL with parameters
request_url = f"{url}?pageSize=1&q={topic}&apiKey={api_key}&sortBy=Popularity&from=2023-04-07&to=2023-04-07"

# make HTTP request and parse response as JSON
response = requests.get(request_url)
articles = json.loads(response.text)["articles"]

# print out article titles and sour ces
for article in articles:
    print(article["title"])
    print(article["source"]["name"])
    print(article["content"])
    print()


