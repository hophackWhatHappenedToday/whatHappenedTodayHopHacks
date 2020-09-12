import newspaper
from newspaper import news_pool
import datetime
from datetime import timezone
import csv

def extract_news():
    # build all newspaper source
    bbc_paper = newspaper.build('https://www.bbc.com', memorize_articles=False)
    cnbc_paper = newspaper.build('https://www.cnbc.com/', memorize_articles=False)
    cnn_paper = newspaper.build('https://edition.cnn.com', memorize_articles=False)
    forbes_paper = newspaper.build('https://www.forbes.com', memorize_articles=False)
    fox_paper = newspaper.build('https://www.foxnews.com', memorize_articles=False)
    guardian_paper = newspaper.build('https://www.theguardian.com', memorize_articles=False)
    nbc_paper = newspaper.build('https://www.nbc.com', memorize_articles=False)
    npr_paper = newspaper.build('https://www.npr.org', memorize_articles=False)
    nytimes_paper = newspaper.build('https://www.nytimes.com', memorize_articles=False)
    wsj_paper = newspaper.build('https://www.wsj.com', memorize_articles=False)
    yahoo_paper = newspaper.build('https://www.yahoo.com', memorize_articles=False)

    papers = [bbc_paper, cnbc_paper, cnn_paper, forbes_paper, fox_paper, guardian_paper, nbc_paper, npr_paper, nytimes_paper, wsj_paper, yahoo_paper]

    # write first row of the csv file
    with open('news.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["#", "url", "date", "title", "keywords", "summary", "text"])

    i = 1

    for paper in papers:
        for article in paper.articles:
            try:
                article.download()
            except newspaper.article.ArticleException:
                print("Failed to scrape some websites.")
            article.parse()

            if article.publish_date != None:
                # check if the article is new
                now = datetime.datetime.now()
                time_elapsed = now - article.publish_date
                if time_elapsed.total_seconds() > 172800:
                    continue

            # store the information of this article
            res = []
            res.append(i)
            i+=1

            res.append(article.url)
            res.append(str(article.publish_date))

            res.append(' '.join(article.keywords))
            res.append(article.summary)
            # res.append(article.html)
            res.append(article.text)

            with open('news.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(res)

    print("Done")

extract_news()



    

