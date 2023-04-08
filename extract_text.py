import newspaper
from newspaper import Article

def extract_text(url):
    article = Article('', language='en')
    article.download(url)
    article.parse()
    return article.text
