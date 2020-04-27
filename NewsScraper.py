import requests
from bs4 import BeautifulSoup
from newspaper import Article 
import pandas as pd
import numpy as np
class ScrapeArticle():

    def __init__(self):
        self.news = []
        self.df = []
        self.articles = []
    
    def get_news_from_url(self, url):
         
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib') 
        table = soup.findAll('a', attrs = {'class':'w_img'})
        for row in table: 
            if not row['href'].startswith('http'):
                self.news.append(url+row['href'])

    def get_article(self):
        for i in self.news:
            article = Article(i, language="en")
            article.download() 
            article.parse() 
            article.nlp() 
            data={}
            data['Title']=article.title
            data['Text']=article.text
            data['Summary']=article.summary
            data['Keywords']=article.keywords
            self.df.append(data)
            self.articles.append(article)
        dataset=pd.DataFrame(self.df)
        dataset.to_csv('crawled_news.csv')
        print(dataset.head())
        print("done")
        return self.articles
