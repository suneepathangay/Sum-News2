##using the news library we need to process the url and extract the article text

from newspaper import Article


def get_html(url):
    article=Article(url=url)
    
    article.download()
    article.parse()
    
    print(article.text)
    
    


  


text=get_html('https://www.cnn.com/2023/07/29/europe/wagner-poland-suwalki-intl/index.html')  


print(text)