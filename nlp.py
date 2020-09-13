# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import pandas as pd
import newspaper
from newspaper import Article

# Here goes the pseudocode

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

    result_dic = 
