import unittest
import os
from os import path
import NewsScraper as ns
class TestNewsScraper(unittest.TestCase):

    def test(self):
        obj = ns.ScrapeArticle()
        obj.get_news_from_url("https://timesofindia.indiatimes.com/world")
        articles = obj.get_article()
        self.assertEqual(path.exists('crawled_news.csv'), True)


if __name__ == '__main__':

    unittest.main()