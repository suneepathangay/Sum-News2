

from newsapi import NewsApiClient


def get_articles(query):
    newsapi = NewsApiClient(api_key='44c53f2380904d4ca100e9e2daf30cbb')

    
    all_articles = newsapi.get_everything(q=query,
                                    #   sources='bbc-news,the-verge',
                                    #   domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    return all_articles

print(get_articles("hello"))


