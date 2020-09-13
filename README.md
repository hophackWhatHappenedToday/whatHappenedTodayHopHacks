# What Happened Today

Have you ever been overwhelmed by millions of news generated on various news platforms every day? We understand that this is a fast pacing world. People would like a quick and straightforward way to view the big events that are going on recently. Our project provides a word cloud based on trending news and user preference. Users can see the important events that are happening at the moment and only search or view articles for those that interest them

![Main Page](https://raw.githubusercontent.com/YuqiZ2020/PicBed/master/img/20200913094939.png)

## Key Features

### In a Rush? A Word Cloud 

### Interested? Search or See Related News

Users can click on any word in the word cloud to search for this word in google news. There will also be a list containing all words in the word cloud that can take users to a compiled list of articles related to each word.  

### Only Interested in Some News? Edit Preference

Users can select their preference to only view certain news sources or certain types of news. There are 11 news sources to (multi-)select from (We will add more!). Sorting can be based on Keywords, High Frequency Words, or Sentiment. Users might only be interested in the news within 24hr, 48hr, or 72hr. The amount of words listed can be in a range from 0-60. There are also 25 different news categories for users to choose from.  

## Set Up and Run

Clone this Repo and use a web browser to open ```mainPage.html``` (Google Chrome is recommended). 

Feel free to edit your preference for selecting certain proportions of the news. Then click "See What Happened" to view a word cloud and a keyword list generated based on recent trending news and your preference. Click on any word that you are interested in to search for it. We also provide a list of news related to a keyword.    

## Technical Details

### Web Scraper

### Data Storage

### Natural Language Processing

All natural language processing features in this project are implemented using the [Google Natural Language API](https://cloud.google.com/natural-language/). We implemented word extraction and sentiment analysis. 

### Word Cloud

The word cloud is generated using the [tag chart](https://docs.anychart.com/Basic_Charts/Tag_Cloud) feature in [AnyChart](https://www.anychart.com/) library of JavaScript. 