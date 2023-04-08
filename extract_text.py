import newspaper
from newspaper import Article
from trafilatura import fetch_url, extract
def extract_text(html):
    # article = Article('')
    # article.set_html(html)
    # article.parse()
    # return article.text
    print(extract(html))

