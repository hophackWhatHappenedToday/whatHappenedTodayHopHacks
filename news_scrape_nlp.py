import newspaper
from newspaper import news_pool
from newspaper import Article
import datetime
from datetime import timezone
import pandas as pd
import numpy as np
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from mysql_engine import get_mysql_eng

def extract_news():
    # build all newspaper source
    bbc_paper = newspaper.build('https://www.bbc.com')
    cnbc_paper = newspaper.build('https://www.cnbc.com/')
    cnn_paper = newspaper.build('https://edition.cnn.com')
    forbes_paper = newspaper.build('https://www.forbes.com')
    fox_paper = newspaper.build('https://www.foxnews.com')
    guardian_paper = newspaper.build('https://www.theguardian.com')
    nbc_paper = newspaper.build('https://www.nbc.com')
    npr_paper = newspaper.build('https://www.npr.org')
    nytimes_paper = newspaper.build('https://www.nytimes.com')
    wsj_paper = newspaper.build('https://www.wsj.com')
    yahoo_paper = newspaper.build('https://www.yahoo.com')

    papers = [bbc_paper, cnbc_paper, cnn_paper, forbes_paper, fox_paper, 
              guardian_paper, nbc_paper, npr_paper, nytimes_paper, wsj_paper, yahoo_paper]

    source = {0: "bbc", 1: "cnbc", 2: "cnn", 
              3: "forbes", 4: "fox", 5: "guardian", 
              6: "nbc", 7: "npr", 8: "nytimes", 
              9: "wsj", 10: "yahoo"}
    
    news_data = pd.DataFrame(columns=["news_id","url", "date", "source", "title", "keywords", "category", "sentiment"])
    
    num = 0

    for j in range(0, len(papers)):
        paper = papers[j]
        
        for article in paper.articles:
            try:
                article.download()
                article.parse()
                print(article.title)

                if article.publish_date == None:
                    continue
                if article.title == None:
                    continue

                # Analysis with google api
                client = language_v1.LanguageServiceClient()
                type_ = enums.Document.Type.PLAIN_TEXT
                language = "en"
                encoding_type = enums.EncodingType.UTF8

                document = {"content": article.text, "type": type_, "language": language}

                sen_response = client.analyze_sentiment(document, encoding_type=encoding_type)
                
                sentiment_score = response.document_sentiment.score
                
                cat_response = client.classify_text(document, encoding_type=encoding_type)

                categories = []
                for category in cat_response.categories:
                    categories.append(category.name)

                ent_response = client.analyze_entities(document, encoding_type=encoding_type)
                keywords={}
                for entity in ent_response.entities:
                    keywords.Add(entity.name, entity.salience)
                
                sorted(keywords, key=keywords.get, reverse=True)
                
                i=1
                key_words = []
                for key in keywords.keys():
                    key_words.append(key)
                    i+=1
                    if i>5:
                        break

                if article.publish_date==None or len(article.title)==0 or len(key_words)==0 or len(categories)==0 or sentiment_score==None:
                    continue

                news_data = news_data.append({
                    "news_id":num, "url": article.url, "date": str(article.publish_date.date()), 
                    "source": str(j), "title": article.title, "keywords":key_words, 
                    "category":categories[0], "sentiment":sentiment_score}, ignore_index=True)

                num+=1

            except newspaper.article.ArticleException:
                print("Failed to scrape some websites.")
                
    news_data_final = pd.DataFrame({
        col:np.repeat(news_data[col].values, news_data['keywords'].str.len())
        for col in news_data.columns.drop('keywords')}
        ).assign(**{'keywords':np.concatenate(news_data['keywords'].values)})[news_data.columns]

    data_with_freq = news_data_final.groupby(['keywords', 'source', 'date', 'category']).size().reset_index(name='frequency')
    data_with_freq = data_with_freq.sort_values(by=['date', 'source'], ignore_index=True)
    
    print("Done") 
    return [news_data_final, data_with_freq]
    
     

    
def write_to_table(data, table_name):    
    engine = get_mysql_eng()
    conn = engine.connect()
    try:
        data.to_sql(table_name, conn, index=False, if_exists='append')
    except Exception as err: 
        print("fail!")
        print(err)
    else:
        print("Table %s created successfully."%table_name);   
    finally:
        conn.close()

        
if __name__=="__main__":
    [news_data_final, data_with_freq] = extract_news()
    write_to_table(news_data_final, "news_details")
    write_to_table(data_with_freq, "news_frequency")

