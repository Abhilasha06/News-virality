import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import pickle
class TrainModel():

    def __init__(self):
        self.feature_list=[]
    

    def clean_cols(self, data):
        """converting to lowercase and stripping"""
        clean_col_map = {x: x.lower().strip() for x in list(data)}
        return data.rename(index=str, columns=clean_col_map)

    def split_data(self, path):
        """splitting test train data"""
        full_data = self.clean_cols(pd.read_csv(path))
        train_set, test_set = train_test_split(full_data, test_size=0.20, random_state=42)

        x_train = train_set.drop(['url','shares', 'timedelta', 'lda_00','lda_01','lda_02','lda_03','lda_04','num_self_hrefs', 'kw_min_min', 'kw_max_min', 'kw_avg_min','kw_min_max','kw_max_max','kw_avg_max','kw_min_avg','kw_max_avg','kw_avg_avg','self_reference_min_shares','self_reference_max_shares','self_reference_avg_sharess','rate_positive_words','rate_negative_words','abs_title_subjectivity','abs_title_sentiment_polarity'], axis=1)
        y_train = train_set['shares']

        x_test = test_set.drop(['url','shares', 'timedelta', 'lda_00','lda_01','lda_02','lda_03','lda_04','num_self_hrefs', 'kw_min_min', 'kw_max_min', 'kw_avg_min','kw_min_max','kw_max_max','kw_avg_max','kw_min_avg','kw_max_avg','kw_avg_avg','self_reference_min_shares','self_reference_max_shares','self_reference_avg_sharess','rate_positive_words','rate_negative_words','abs_title_subjectivity','abs_title_sentiment_polarity'], axis=1)
        y_test = test_set['shares']
        self.feature_list = list(x_train.columns)
        return x_train, y_train, x_test, y_test
    
    def train_and_save_the_model(self, path):
        '''training and testing the model'''
        x_train, y_train, x_test, y_test = self.split_data(path)
        
            
        clf = RandomForestRegressor(n_estimators= 50, random_state=42)
        clf.fit(x_train, y_train)

        Pkl_Filename = "saved_model.pkl"  

        with open(Pkl_Filename, 'wb') as file:  
            pickle.dump(clf, file)
        
        res = clf.predict(x_test)
        importances = clf.feature_importances_
        print(importances)

        x_values = list(range(len(importances)))
        plt.bar(x_values, importances, orientation = 'vertical', color = 'b', edgecolor = 'k', linewidth = 1.2)
        plt.xticks(x_values, self.feature_list, rotation='vertical')
        plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances')
        plt.tight_layout()

        plt.show()      
            
        
if __name__ == '__main__':
    obj = TrainModel()
    obj.train_and_save_the_model('OnlineNewsPopularity.csv')