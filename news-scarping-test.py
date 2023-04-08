import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


# set API endpoint URL and API key
URL = "https://newsapi.org/v2/top-headlines"
api_key = os.getenv("API-KEY")

# set search parameters
COUNTRY = "us"
TOPIC = "israel"

# construct request URL with parameters
request_url = f"{URL}?pageSize=1\
    &apiKey={api_key}&q={TOPIC}\
        &sortBy=Popularity\
            &from=2023-04-07&to=2023-04-07\
                &country={COUNTRY}"

# make HTTP request and parse response as JSON
response = requests.get(request_url, timeout=None)
articles = json.loads(response.text)["articles"]

# print out article titles and sour ces
for article in articles:
    print(article["title"])
    print(article["source"]["name"])
    
    print(article["url"])
import extract_text
print(extract_text.extract_text(requests.get(article["url"]).text))