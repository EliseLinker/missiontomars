import time 
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# selenium 
def scrape_news():
    browser = webdriver.Chrome('chromedriver.exe')
    news = {}
    url = 'https://mars.nasa.gov/news/'
    browser.get(url)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "html.parser")
    
    # print(soup.prettify())
    
    
    news["news_title"] = soup.find("div", class_="content_title").get_text()
    news["news_p"] = soup.find("div", class_="article_teaser_body").get_text()

    return news

#scrape_news()
