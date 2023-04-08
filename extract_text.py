import newspaper
from newspaper import Article

def extract_text(html):
    article = Article('')
    article.set_html(html)
    article.parse()
    return article.text

