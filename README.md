# News-virality
## Crawling news & information websites & anticipating the likelihood of its virality.

This repo aims at predicting the virality of news scraped from different websites using random forest regression model.

NewsScraper.py is used to scrape the article from any given website.
test_news_scraper.py tests if NewsScraper.py is working properly based on certain unittests.

<img width="591" alt="a" src="https://user-images.githubusercontent.com/43816262/80425800-011f7480-8902-11ea-8ce4-54f24f9ad963.png">

News crawled from times of india website. (full data at crawled_news.csv)

<img width="692" alt="b" src="https://user-images.githubusercontent.com/43816262/80426212-e6013480-8902-11ea-9595-b78b3e4f62b2.png">


The dataset used for training the model is Online News Popularity dataset available at uci.edu. This dataset has a total of 61 attributes its description is available in the dataset_attribtes.txt file.


The file preprocess.py has necessary functions for preprocessing the raw scraped data and converting it to a form similar to the original dataset.

The file train_and_save_model.py trains a random forest regression model on the Online News popularity Dataset certain columns have been dropped while training since those columns were not available for the newly crawled data. The file trains and save the model in .pkl form. The feature importance given to the different features by the model is as follows-
![feature_importance](https://user-images.githubusercontent.com/43816262/80426848-388f2080-8904-11ea-8ecf-c01397659284.png)

Finally the notebook test_and_visualize_times_of_india_site.ipynb contains the predictions on the crawled data, it uses the above mentioned files for crawling, preprocessing and loding the model and predicts the virality of the news. The final title of the news along with the predicted virality is saved as predicted_virality.csv and sort_by_virality.csv (sorted in descending order).
Here are a few of the predictions (sorted in descending order of virality)-

<img width="627" alt="c" src="https://user-images.githubusercontent.com/43816262/80427189-d1be3700-8904-11ea-99c9-065bbdb447ea.png">



