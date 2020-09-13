from mysql_engine import get_mysql_eng
import pandas as pd
import numpy as np
import datetime
from datetime import timedelta
import pytz

# run a mysql statement
def run_sql(sql):
    engine = get_mysql_eng()
    conn = engine.connect()
    try:
        res = pd.read_sql(sql, conn)
        return res
    except Exception as err:
        print("fail")
        print(err)
    finally:
        conn.close()



# sort_type in ['date', 'rdate', 'sentiment', 'rsentiment']
# return None if no such keywords or return size <= 0
# return [{keyword: k, frequencny:n (int), average sentiment score:s (float), title:[t,t,t,t],url:[u,u,u,u], date[d,d,d,d](string), source[s,s,s,s], sentiment[s,s,s,s]}]
def search_keywords(return_size, source_input = [], category_input = [], date_input = str(72), sort_type="rdate"):
    if type(return_size) == type("abc"):
        return_size = int(return_size)
    if return_size <= 0:
        return None
    
    # get sort_type
    if sort_type == 'date':
        sort1 = 'date'
        sort2 = 'sentiment'
        ascend = ''
    elif sort_type == 'rdate':
        sort1 = 'date'
        sort2 = 'sentiment'
        ascend = 'DESC'
    elif sort_type == 'sentiment':
        sort1 = 'sentiment'
        sort2 = 'date'
        ascend = ''
    elif sort_type == 'rsentiment':
        sort1 = 'sentiment'
        sort2 = 'date'
        ascend = 'DESC'

    # get source, source = '' if source_input = []
    source = "'"
    source = source + " ', '".join(source_input)
    source = source + "'"

    source_sql = """
                SELECT id
                FROM source_index
                WHERE source_name IN ({source_list})
                   OR '' IN ({source_list});
                """.format(source_list=source)
    source_list = run_sql(source_sql).id.values.tolist()
    
    source = "'"
    source = source + " ', '".join(source_list)
    source = source + "'"  # source is not-empty now
    
    # get date_list (a list of string in format '2020-09-12'), not-empty
    date_list = []
    if type(date_input) == type("abd"):
        date_input = int(date_input)
    today = datetime.datetime.now(pytz.timezone('EST')).date()
    if date_input >= 24:
        date_list.append(str(today))
    if date_input >= 48:
        date_list.append(str(today + timedelta(days=-1)))
    if date_input >= 72:
        date_list.append(str(today + timedelta(days=-2)))
    date = "'"
    date = date + " ', '".join(date_list)
    date = date + "'"    
    
    # get category, category = '' if category_input = []
    category = "'"
    category = category + " ', '".join(category_input)
    category = category + "'"
    
    keywords_freq_sql = """
                    SELECT keywords, sum(frequency) AS freq
                    FROM news_frequency
                    WHERE date IN ({date_list})
                      AND source IN({source_list})
                      AND (category IN ({category_list}) OR '' IN ({category_list}))
                    GROUP BY keywords
                    ORDER BY sum(frequency) DESC
                    LIMIT {size};
                    """.format(date_list=date, source_list=source, category_list=category, size=return_size)
    keywords_freq = run_sql(keywords_freq_sql)

    keywords_list = keywords_freq.keywords.values.tolist()  # a list of keywords
    if len(keywords_list) == 0:
        return None
    
    freq_list = keywords_freq.freq.values.tolist()  # a list of frequency
    
    result = {}
    for index in range(len(keywords_list)):
        keyword = keywords_list[index]
        
        keywords_detail_sql = """
                            SELECT date, source, title, url, sentiment
                            FROM news_details
                            WHERE date IN ({date_list})
                              AND source IN({source_list})
                              AND (category IN ({category_list}) OR '' IN ({category_list}))
                              AND keywords = '{keywords}'
                            GROUP BY date, source, news_id, title, url, sentiment
                            ORDER BY {order1} {ascend}, {order2} {ascend};
                            """.format(date_list=date, source_list=source, category_list=category, keywords=keyword, order1=sort1, order2=sort2, ascend=ascend)
        detail = run_sql(keywords_detail_sql)
        date_result = detail.date.values.tolist()
        title_result = detail.title.values.tolist()
        url_result = detail.url.values.tolist()
        sentiment_result = detail.sentiment.values.tolist()
        source_result_temp = detail.source.values.tolist()
        source_result = []
        
        for i in source_result_temp:
            source_name_sql = """
                                SELECT source_name
                                FROM source_index
                                WHERE id = '{id}';
                                """.format(id=i)
            source_name = run_sql(source_name_sql).source_name.values.tolist()[0]
            source_result.append(source_name)
        
        value = [freq_list[index], np.mean(sentiment_result), title_result, url_result, date_result, source_result, sentiment_result]
        result[keyword] = value
    
    return result




# gcloud config set project whathappendtoday
# gcloud sql connect myinstance --user=root

# create table news_details to store all data
# sorted by date, source
# CREATE TABLE IF NOT EXISTS news_details
#     (news_id INT NOT NULL,
#      url VARCHAR(255) DEFAULT '',
#      date VARCHAR(20) DEFAULT '',
#      source VARCHAR(20) DEFAULT '',
#      title VARCHAR(255) DEFAULT '',
#      keywords VARCHAR(50) DEFAULT '',
#      category VARCHAR(50) DEFAULT '',
#      sentiment FLOAT NOT NULL
#      );

# create table news_frequency for filtering
# sorted by date, source
# CREATE TABLE IF NOT EXISTS news_frequency
#     (keywords VARCHAR(50) DEFAULT '',
#      source VARCHAR(20) DEFAULT '',
#      date VARCHAR(20) DEFAULT '',
#      category VARCHAR(50) DEFAULT '',
#      frequency INT NOT NULL
#     );

# create table source_index to store source names and their corresponding index
#
# CREATE TABLE source_index
#     (id VARCHAR(20), 
#      source_name VARCHAR(20) DEFAULT '',
#      PRIMARY KEY(id)
#     );

# insert values into source_index
# INSERT INTO source_index (id, source_name) VALUES('0','bbc'), ('1', 'cnbc'), ('2', 'cnn'), ('3', 'forbes'), ('4', 'fox'), ('5', 'guardian'), ('6', 'nbc'), ('7', 'npr'), ('8', 'nytimes'), ('9', 'wsj'), ('10', 'yahoo');

