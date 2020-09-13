import newspaper
from newspaper import news_pool
from newspaper import Article
import datetime
from datetime import timezone
import pandas as pd
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums

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

    papers = [bbc_paper, cnbc_paper, cnn_paper, forbes_paper, fox_paper, guardian_paper, nbc_paper, npr_paper, nytimes_paper, wsj_paper, yahoo_paper]

    source = {0: "bbc", 1: "cnbc", 2: "cnn", 3: "forbes", 4: "fox", 5: "guardian", 6: "nbc", 7: "npr", 8: "nytimes",
           9: "wsj", 10: "yahoo"}
    
    news_data = pd.DataFrame(columns=["news_id","url", "date", "source", "title", "keywords", "category", "sentiment"])
    
    num = 0

    for j in range(0, len(papers)):
        paper = papers[j]
        
        for article in paper.articles:
            try:
                article.download()
                article.parse()

                if article.publish_date == None:
                    continue
                if article.title == None:
                    continue

                # Analysis with google api
                client = language_v1.LanguageServiceClient()
                type_ = enums.Document.Type.PLAIN_TEXT
                language = "en"
                encoding_type = enums.EncodingType.UTF8

                index = 1
                for data in file:
                    url = choose the url from data

                    article = Article(url)
                    article.download()
                    article.parse()

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

                news_data = news_data.append({"news_id":num+=1, "url": article.url, "date": str(article.publish_date.date()), "source": str(j), "title": article.title, "keyword":key_words, "category":categories[0], "sentiment":sentiment_score}, ignore_index=True)
            except newspaper.article.ArticleException:
                print("Failed to scrape some websites.")
                
    news_data.to_pickle("news.pkl")

    print("Done")  

if __name__=="__main__":
    extract_news()








