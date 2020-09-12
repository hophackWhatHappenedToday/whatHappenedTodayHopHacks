#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ["id", "url", "date", "source", "title", "keywords", "category", "sentiment"]
# (id - int, source - int, sentiment - floating numbers, keywords - list, category - list, date - dateformat(not datetime), others - string)
# source = {0: "bbc", 1: "cnbc", 2: "cnn", 3: "forbes", 4: "fox", 5: "guardian", 6: "nbc", 7: "npr", 8: "nytimes", 9: "wsj", 10: "yahoo"}


# In[130]:


import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
import pytz


# In[135]:


# filename = "news_test.pkl"
def calulate_frequency(filename):
    raw_data = pd.read_pickle(filename)
    data_to_expand = raw_data.loc[:, ['date', 'source', 'keywords', 'category', 'sentiment']]
    
    for expand_col in ['keywords', 'category']:
        data_to_expand = pd.DataFrame({
            col:np.repeat(data_to_expand[col].values, data_to_expand[expand_col].str.len())
            for col in data_to_expand.columns.drop(expand_col)}
            ).assign(**{expand_col:np.concatenate(data_to_expand[expand_col].values)})[data_to_expand.columns]
    
    data_with_freq = data_to_expand.groupby(['date', 'source', 'category', 'sentiment', 'keywords']).size().reset_index(name='frequency')
    data_with_freq = data_with_freq.sort_values(by=['date', 'sentiment'], ignore_index=True)
    
    return data_with_freq


# In[196]:


# return an array of type [[keyword1, freq1], [keyword2, freq2], ..., [keywordn, freqn]]
# return an empty array [] if no keywords remained after filtering
def filter(time_elapse, source_input_list, category_list, sentiment_min, sentiment_max, return_list_size):
    # filename to be changed
    filename = "news_with_freq_test.pkl"
    data = pd.read_pickle(filename)
    
    date_list = []
    today = datetime.datetime.now(pytz.timezone('EST')).date()
    if time_elapse >= 24:
        date_list.append(str(today))
    if time_elapse >= 48:
        date_list.append(str(today + timedelta(days=-1)))
    if time_elapse >= 72:
        date_list.append(str(today + timedelta(days=-2)))
    
    source_list = []
    source_data = [[0, "bbc"], [1, "cnbc"], [2, "cnn"], [3, "forbes"], [4, "fox"], [5, "guardian"], [6, "nbc"], [7, "npr"], [8, "nytimes"], [9, "wsj"], [10, "yahoo"]]
    for i in source_data:
        if i[1] in source_input_list:
            source_list.append(i[0])
    
    filtered_data = data.loc[(data.loc[:, 'date'].isin(date_list)) & (data.loc[:, 'source'].isin(source_list)) 
                             & (data.loc[:, 'category'].isin(source_list)) & (data.loc[:, 'sentiment']>=sentiment_min) 
                             & (data.loc[:, 'sentiment']<=sentiment_max)].groupby('keywords')['frequency'].sum().reset_index(name = 'frequency')
    filtered_data = filtered_data.sort_values(by=['frequency'], ascending=False, ignore_index=True)
    
    row_num = len(filtered_data.index)
    if row_num == 0:
        return []  # return an empty array if no keyword remained after filtering
    if row_num < return_list_size:
        return_list_size = row_num
    result_data = filtered_data[0:return_list_size]
    return result_data.values.tolist()    


# In[194]:


# test
data_with_freq = calulate_frequency("news_test.pkl")
data_with_freq.to_pickle("news_with_freq_test.pkl")


# In[197]:


# test - has bug
result = filter(72, ["bbc", "cnbc"], ["business"], -1, 1, 2)


# In[139]:





# In[193]:


# .pkl file for testing
data = []
data.append([1, cnn_paper.articles[3].url, str(cnn_paper.articles[3].publish_date.date()), 0, "hi", ["a", "b"], ["business", "sports"], 1])
data.append([2, "urlx", str(datetime.date(2020, 9, 10)), 0, "title", ["a", "b"], ["business", "sports"], 2.5])
data.append([3, "urlx", str(datetime.date(2020, 9, 10)), 1, "title", ["a", "b"], ["business", "arts"], 3])
data.append([4, "urlx", str(datetime.date(2020, 9, 10)), 1, "title", ["f", "b"], ["business", "sports"], -0.1])
data.append([5, "urlx", str(datetime.date(2020, 9, 10)), 2, "title", ["f", "b"], ["business"], -2])
data.append([6, "urlx", str(datetime.date(2020, 9, 10)), 2, "title", ["a", "c"], ["business"], -2.3])
data.append([7, "urlx", str(datetime.date(2020, 9, 10)), 2, "title", ["e"], ["sports"], -2.1])
data.append([8, "urlx", str(datetime.date(2020, 9, 10)), 3, "title", ["d", "b"], ["arts", "sports"], 1.3])
data.append([9, "urlx", str(datetime.date(2020, 9, 10)), 2, "title", ["a", "c"], ["arts"], -1.5])
data.append([10, "urlx", str(datetime.date(2020, 9, 10)), 1, "title", ["a"], ["arts", "science"], 1.6])

news_data = pd.DataFrame(columns=["id", "url", "date", "source", "title", "keywords", "category", "sentiment"])
for i in data:
    news_data = news_data.append({"id": i[0], "url": i[1], "date": i[2], "source": i[3], "title": i[4], "keywords": i[5], "category": i[6], "sentiment": i[7]}, ignore_index=True)
    
news_data.to_pickle("news_test.pkl")

