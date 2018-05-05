import time 
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# 1. define a function with your boiler plate code
# def init_browser():
#      executable_path = {"executable_path": "chrome/chromedriver"}
#      return Browser("chrome", **executable_path, headless=False)

# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     executable_path = {"executable_path": "C:/Users/elise/Desktop/Bootcamp/Homework/missiontomars/chromedriver.exe"}
#     return Browser("chrome", **executable_path, headless=False)


# selenium 

# 2. Define a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.
# def scrape():
#    browser = init_browser()
def scrape():
    browser = webdriver.Chrome('C:/Users/elise/Desktop/Bootcamp/Homework/missiontomars/chromedriver.exe')
    # browser = init_browser()
    
    
    scrape_dictionary = {}


# splinter 
#executable_path = {'executable_path': 'chromedriver.exe'}
#browser = Browser('chrome', **executable_path, headless=False)

# selenium 
# def scrape_news():
    # browser = webdriver.Chrome('chromedriver.exe')
    # news = {}
    news_url = 'https://mars.nasa.gov/news/'
    browser.get(news_url)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "html.parser")
    
    # print(soup.prettify())
    
    
    scrape_dictionary["news_title"] = soup.find("div", class_="content_title").get_text()
    scrape_dictionary["news_p"] = soup.find("div", class_="article_teaser_body").get_text()

    # return scrape_dictionary



# def scrape_featuredimage():
    # browser = webdriver.Chrome('chromedriver.exe')
    # featuredimage = {}
    featured_img_url = 'https://www.jpl.nasa.gov/spaceimages'
    featured_img_url2 = 'https://www.jpl.nasa.gov'
   
    browser.get(featured_img_url)
    time.sleep(1)
        
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    mylink = soup.find("a", class_="button fancybox")
    #mylink = soup.find("a")
    # print(soup.prettify())
    print(mylink)
    
    mylink.attrs
    print(mylink.attrs['data-fancybox-href'])
    
    scrape_dictionary["featured_image_url"] = featured_img_url2 + mylink.attrs['data-fancybox-href']

    # return scrape_dictionary

# scrape_featuredimage()

# def scrape_marsweather():
    # browser = webdriver.Chrome('chromedriver.exe')
    #marsweather = {}
    weather_url = 'https://twitter.com/marswxreport?lang=en'
    
    browser.get(weather_url)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    
    # print(soup.prettify())
    
    mylink.attrs
    scrape_dictionary["mars_weather"] = soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    #soup.find("a", class_="button fancybox").get_link()
    
    # return scrape_news()

# scrape_marsweather()

# def scrape_marsdata():
    mars_data_url = 'https://space-facts.com/mars/'
    scrape_dictionary["marsdata_table"] = pd.read_html(mars_data_url)
        
    # return marsdata_table

# scrape_marsdata()

# def scrape_marshemispheres():
    # browser = webdriver.Chrome('chromedriver.exe')
    # scrape_dictionary = {'title':[],
    #                  'img_url':[]}
    hemisphere_image_url = {'title':[],
                            'img_url':[]}
    main_url = 'https://astrogeology.usgs.gov'
    
    # cerberus
    cerberus_url = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    
    browser.get(cerberus_url)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    mylink = soup.find('img', class_="wide-image")
    mylink2 = soup.find('h2', class_="title").text
    #print(soup.prettify())
    
    mylink.attrs
    scrape_dictionary["title"] = mylink2
    scrape_dictionary["img_url"] = (main_url + mylink.attrs["src"]) 

    # hemisphere_image_url["title"].append(mylink2) 
    # hemisphere_image_url["img_url"].append(main_url + mylink.attrs["src"]) 
    
    # schiaparelli
    hemisphere_image_url1 = {'title':[],
                     'img_url':[]}
    schiaparelli_url1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
    
    browser.get(schiaparelli_url1)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    mylink = soup.find('img', class_="wide-image")
    mylink2 = soup.find('h2', class_="title").text
    #print(soup.prettify())
    
    mylink.attrs
    hemisphere_image_url1["title"].append(mylink2)
    #hemisphere_image_urls["img_url"].append = mylink.attrs["src"]
    hemisphere_image_url1["img_url"].append(main_url + mylink.attrs["src"])
    
    # syrtis_major
    hemisphere_image_url2 = {'title':[],
                             'img_url':[]}
    syrtis_major_url2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    
    browser.get(syrtis_major_url2)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    mylink = soup.find('img', class_="wide-image")
    mylink2 = soup.find('h2', class_="title").text
    #print(soup.prettify())
    
    mylink.attrs
    hemisphere_image_url2["title"].append(mylink2)
    #hemisphere_image_urls["img_url"].append = mylink.attrs["src"]
    hemisphere_image_url2["img_url"].append(main_url + mylink.attrs["src"])
    
    # valles_marineris
    hemisphere_image_url3 = {'title':[],
                             'img_url':[]}
    valles_marineris_url3= 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    
    browser.get(valles_marineris_url3)
    time.sleep(1)
    
    html = browser.page_source 
    soup = BeautifulSoup(html, "lxml")
    mylink = soup.find('img', class_="wide-image")
    mylink2 = soup.find('h2', class_="title").text
    #print(soup.prettify())
    
    mylink.attrs
    hemisphere_image_url3["title"].append(mylink2)
    hemisphere_image_url3["img_url"].append(main_url + mylink.attrs["src"])
    
    # hemisphere_image_urls = []
    scrape_dictionary["img_url"] = hemisphere_image_url 
    scrape_dictionary["img_url"] = hemisphere_image_url1 
    scrape_dictionary["img_url"] = hemisphere_image_url2 
    scrape_dictionary["img_url"] = hemisphere_image_url3

    # hemisphere_image_urls = []
    # hemisphere_image_urls.append(hemisphere_image_url) 
    # hemisphere_image_urls.append(hemisphere_image_url1) 
    # hemisphere_image_urls.append(hemisphere_image_url2) 
    # hemisphere_image_urls.append(hemisphere_image_url3)
    
    # return hemisphere_image_urls

# scrape_marshemispheres()
    return scrape_dictionary

# print(scrape_dictionary)
# https://astrogeology.usgs.gov/cache/images/7cf2da4bf549ed01c17f206327be4db7_valles_marineris_enhanced.tif_full.jpg







    # listings["headline"] = soup.find("a", class_="result-title").get_text()
    # listings["price"] = soup.find("span", class_="result-price").get_text()
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()

    # return listings

# for step 2 my best advise is first create a python  file:

#    #Create an empty dict to append scraped data in step 1
#    
# 3.Copy all your code from the juniper notebook inside this function scrape .. 
# remember to add to the empty_dictionary all your data points that you previously scraped 
# 4. Create your app.py where you will set up your flask