import newspaper
from newspaper import news_pool
import datetime
import csv

class News:
    papers = []
    valid_articles = []
    result = []

    def __init__(self):
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

        self.papers = [bbc_paper, cnbc_paper, cnn_paper, forbes_paper, fox_paper, guardian_paper, nbc_paper, npr_paper, nytimes_paper, wsj_paper, yahoo_paper]

        # write first row of the csv file
        with open('news.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([["#", "date","title", "keywords", "summary", "HTML", "text"])

        i = 1

        for paper in self.papers:
            for article in paper.articles:
                article.download()
                article.parse()

                # check if the article is new
                now = datetime.datetime.now()
                time_elapsed = now - article.publish_date
                if time_elapsed.total_seconds() > 172800:
                    continue

                # store the information of this article
                res = []
                res.append(i)
                i+=1
                



        

    def extract_info():
        # TODO: Subset news publish times within 48 hrs
        # TODO: Extract info for the given website link
        for paper in self.papers:
            for ariticle in paper.articles:
                article.download()
                article.parse()

    def 
        
        



    main_url_list = ["https://www.cnn.com/", "https://www.dailymail.co.uk/"]

    def extract_info_for_list(main_url_list):
        # TODO: extract info for the given list
    
