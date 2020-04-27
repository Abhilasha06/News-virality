import NewsScraper as ns
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from textblob import TextBlob
import datefinder
import datetime  
from datetime import date 
import numpy as np
class PreprocessData():
    def __init__(self):
        
        self.articles = []
        self.stopwords=set(stopwords.words('english'))
    
    def preprocessor(self, data):
        self.articles = data

   

    def rate_unique(self, words):
        '''to find n_unique_tokens: Rate of unique words in the content'''
        words = word_tokenize(words)
        no_order = list(set(words))
        rate_unique=len(no_order)/len(words)
        return rate_unique
    
    def rate_nonstop(self, words):
        '''to find n_non_stop_words: Rate of non-stop words in the content'''
        words = word_tokenize(words)
        filtered_sentence = [w for w in words if not w in self.stopwords]
        rate_nonstop=len(filtered_sentence)/len(words)
        no_order = list(set(filtered_sentence))
        rate_unique_nonstop=len(no_order)/len(words)
        return rate_nonstop,rate_unique_nonstop
    
    def avg_token(self, words):
        '''to find average_token_length: Average length of the words in the content'''
        words = word_tokenize(words)
        length=[]
        for i in words:
            length.append(len(i))
        return np.average(length)
    
    def day(self, article_text):
        ''' to find the day article was published'''
        article = article_text
        if len(list(datefinder.find_dates(article)))>0:
            date=str(list(datefinder.find_dates(article))[0])
            date=date.split()
            date=date[0]
            year, month, day = date.split('-')     
            day_name = datetime.date(int(year), int(month), int(day)) 
            return day_name.strftime("%A")
        return "Monday"

    
    def polar(self, words):
        '''to find the polarity of words - positive/negative and 
            store the positive and negative words separately'''
        pos_words=[]
        neg_words=[]
        all_tokens = word_tokenize(words)
        for i in all_tokens:
            analysis=TextBlob(i)
            polarity=analysis.sentiment.polarity
            if polarity>0:
                pos_words.append(i)
            if polarity<0:
                neg_words.append(i)
        return pos_words,neg_words

    def rates(self, words):
        '''
        to find 
        global_rate_positive_words: Rate of positive words in the content
        global_rate_negative_words: Rate of negative words in the content
        avg_positive_polarity: Avg. polarity of positive words
        min_positive_polarity: Min. polarity of positive words
        max_positive_polarity: Max. polarity of positive words
        avg_negative_polarity: Avg. polarity of negative words
        min_negative_polarity: Min. polarity of negative words
        max_negative_polarity: Max. polarity of negative words
        '''
        words = self.polar(words)
        pos=words[0]
        neg=words[1]
        all_words=words
        global_rate_positive_words=(len(pos)/len(all_words))/100
        global_rate_negative_words=(len(neg)/len(all_words))/100
        pol_pos=[]
        pol_neg=[]
        for i in pos:
            analysis=TextBlob(i)
            pol_pos.append(analysis.sentiment.polarity)
            avg_positive_polarity=analysis.sentiment.polarity
        for j in neg:
            analysis2=TextBlob(j)
            pol_neg.append(analysis2.sentiment.polarity)
            avg_negative_polarity=analysis2.sentiment.polarity
        if(len(pol_pos)==0):
            pol_pos.append(0)
        if(len(pol_neg)==0):
            pol_neg.append(0)
        
        min_positive_polarity=min(pol_pos)
        max_positive_polarity=max(pol_pos)
        min_negative_polarity=min(pol_neg)
        max_negative_polarity=max(pol_neg)
        avg_positive_polarity=np.average(pol_pos)
        avg_negative_polarity=np.average(pol_neg)
        return global_rate_positive_words,global_rate_negative_words,avg_positive_polarity,min_positive_polarity,max_positive_polarity,avg_negative_polarity,min_negative_polarity,max_negative_polarity
    
    
