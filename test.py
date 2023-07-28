from newspaper import Article

url = 'https://time.com/6297539/how-india-economy-will-surpass-us/'

article = Article(url)

article.download()

article.parse()

print(article.text)