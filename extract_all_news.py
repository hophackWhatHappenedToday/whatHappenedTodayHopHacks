import newspaper
from newspaper import news_pool
import datetime
from datetime import timezone
import csv

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

    # write first row of the csv file
    with open('news.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["#", "url", "date", "title", "keywords", "summary", "text"])

    i = 1

    for paper in papers:
        for article in paper.articles:
            article.download()
            article.parse()

            # if article.publish_date != None:
            #     # check if the article is new
            #     now = datetime.datetime.now(timezone.est)
            #     time_elapsed = now - article.publish_date
            #     if time_elapsed.total_seconds() > 172800:
            #         continue

            # store the information of this article
            res = []
            res.append(i)
            i+=1

            res.append(article.url)
            res.append(article.publish_date)
            res.append(article.keywords)
            res.append(article.summary)
            # res.append(article.html)
            res.append(article.text)

            with open('news.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(res)

    print("Done")

extract_news()



    

