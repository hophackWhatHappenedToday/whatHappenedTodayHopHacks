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
        writer.writerow(["id", "source", "url", "date", "title", "keywords", "summary"])

    i = 1
    source = {0: "bbc", 1: "cnbc", 2: "cnn", 3: "forbes", 4: "fox", 5: "guardian", 6: "nbc", 7: "npr", 8: "nytimes",
           9: "wsj", 10: "yahoo"}

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

                res = []
                res.append(i)
                i += 1

                res.append(source[j])
                res.append(article.url)
                res.append(str(article.publish_date))
                res.append(article.title)
                res.append(' '.join(article.keywords))
                res.append(article.summary)

                with open('news.csv', 'a+', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(res)
            except newspaper.article.ArticleException:
                print("Failed to scrape some websites.")

    print("Done")

extract_news()



    

