

from newsapi import NewsApiClient
import requests
import bs4
from algo import return_summary
from newspaper import Article


# def get_html(response):
  
#     parsed_article = bs4.BeautifulSoup(response.text,'lxml')

#     paragraphs = parsed_article.find_all('p')


#     article_text = ""

#     for p in paragraphs:
#         article_text += p.text
#     return article_text
  


def get_articles(query):
    newsapi = NewsApiClient(api_key='44c53f2380904d4ca100e9e2daf30cbb')

    
    all_articles = newsapi.get_everything(q=query,
                                    #   sources='bbc-news,the-verge',
                                    #   domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    
    # return all_articles["articles"][:4]
    
    
  
    url=all_articles["articles"][0]["url"]
    
    url='https://time.com/6297539/how-india-economy-will-surpass-us/'
    
    article=Article(url)
    
    article.download()
    article.parse()
    
    summary=return_summary(article.text)
    
    return summary
    
    

  
  
  


