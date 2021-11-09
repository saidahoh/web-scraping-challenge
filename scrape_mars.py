from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import pymongo

def scrape ():
    mars_dict = {}
    
    
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
   
    #News
    news_url = "https://redplanetscience.com/"
    browser.visit(news_url)
    
    newshtml = browser.html
    news_soup = BeautifulSoup(newshtml, "html.parser")
    
    slide_element = news_soup.find("div", class_="list_text")
    news_title = slide_element.find("div", class_ ="content_title").get_text()
    news_paragraph = slide_element.find("div", class_="article_teaser_body").get_text()
    
    
    #Featured Photo
    feature_url = 'https://spaceimages-mars.com/'
    browser.visit(feature_url)
    
    imghtml = browser.html
    img_soup = BeautifulSoup(imghtml, "html.parser")
    
    img_url = img_soup.find_all('img')[1]["src"]
    featured_image_url = feature_url + img_url
    
    
    #Mars Facts
    mars_facts = pd.read_html("https://galaxyfacts-mars.com/")[1]
    mars_facts.columns = ['Description', 'Value']
    facts_html = mars_facts.to_html(table_id="html_tbl_css",justify='left',index=False)
     
      
    
    #Mars Hemisphere
    mh_url = 'https://marshemispheres.com/'
    browser.visit(mh_url)

    mhtml = browser.html
    mh_soup = BeautifulSoup(mhtml,"html.parser")
    
    results = mh_soup.find_all("div",class_='item')
    hemisphere_image_urls = []
    for result in results:
        product_dict = {}
        titles = result.find('h3').text
        end_link = result.find("a")["href"]
        image_link = "https://marshemispheres.com/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup= BeautifulSoup(html, "html.parser")
        image_prt= soup.find("div", class_="wide-image-wrapper")
        image = image_prt.find("img", class_="wide-image")["src"]
        image_url = mh_url +image
        #print(titles)
        #print(image_url)
        product_dict={"title": titles, "image_url":image_url}
        hemisphere_image_urls.append(product_dict)
        
    #close browser
    browser.quit()    

    #add to dict
    mars_dict = {"news_title":news_title,"news_text":news_paragraph,"featured_image":featured_image_url,
    "facts_table":facts_html,"hemisphere_img":hemisphere_image_urls}
    
    return mars_dict

    
   