import newspaper
from newspaper import Article

def extract_text(html):
    article = Article('', language='en')
    article.set_html(html)
    article.parse()
    return article.text
