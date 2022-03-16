# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import pymongo


# "C:\driver"
# use chrome's driver manager
executable_path = {'executable_path':'C:\\driver\\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# Section 1: NASA New
#Scrape the Mars News Site https://redplanetscience.com/
#Assign the text to variables that you can reference later.

def nasa_news(browser):
    # base url
    nasa_url = "https://redplanetscience.com/"
    # open web page
    browser.visit(nasa_url)

    #get html
    html = browser.html
    #parse with beautiful soup
    nasa_soup = BeautifulSoup(html, "html.parser")

    # assign variables
    # the newest news title 
    newest_title = nasa_soup.find("div", class_="content_title").text

    #paragraph of the newest article 
    newest_par = nasa_soup.find("div", class_="article_teaser_body").text

    # return the variables
    return newest_title, newest_par

# Section 2: Feature Images

def feature_image(browser):
    # base url
    image_url = "https://spaceimages-mars.com/"
    # open web page
    browser.visit(image_url)

    #get html
    html = browser.html
    #parse with beautiful soup
    image_soup = BeautifulSoup(html, "html.parser")

    # Use splinter to navigate the site and find the image url for the current Featured Mars Image 
    #assign the url string to a variable called featured_image_url.
    # first step in
    image_query = image_soup.find("div", class_="header")
    # second step in 
    next_query = image_query.find_all("a")
    url_list= []

    # iterate through to find the link
    for i in next_query:
        url_list.append(i.get("href"))
    url_list

    # combine the full url
    feature_image_url = image_url + url_list[2]
    return feature_image_url


# Section 3: with pandas
#use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
def mars_table():
    
    # needs 0 to catch the first set
    facts_df = pd.read_html("https://galaxyfacts-mars.com/")[0]
    facts_df.columns=facts_df.iloc[0]
    facts_df.set_index("Mars - Earth Comparison", inplace=True)
    final_df = facts_df.drop("Mars - Earth Comparison")

    #Use Pandas to convert the data to a HTML table string.
    facts_html = final_df.to_html()
    return facts_html

# Section 4: Hemispheres
# https://marshemispheres.com/
#Visit the astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

# hard coded; see activity 10 for doing this dynamically in the future
# list of all hemispheres
def hemisphere_images(browser):

    hemis=['Cerberus Hemisphere Enhanced',
        'Schiaparelli Hemisphere Enhanced',
       'Syrtis Major Hemisphere Enhanced',
       'Valles Marineris Hemisphere Enhanced']
    # list to be filled
    hemis_url=[]

    #Save both the image url string for the full resolution hemisphere image, 
    #and the Hemisphere title containing the hemisphere name. 
    #Use a Python dictionary to store the data using the keys img_url and title.
    for h in hemis: 
    
        hemi_url="https://marshemispheres.com/"
        browser.visit(hemi_url)
        browser.is_element_present_by_text(h, wait_time=1)
        link = browser.links.find_by_partial_text(h)
    
        #click into new page
        link.click()
    
        # get full image
        full_image = browser.find_by_id('wide-image-toggle')
        #select
        full_image.click()
    
        hemi_soup=BeautifulSoup(browser.html, 'html.parser')
        image = hemi_soup.body.find('img', class_='wide-image')
        image_link = image['src']
        image_url=f"{hemi_url}{image_link}"
    
        #append to list
        hemis_url.append(image_url)


    #This list will contain one dictionary for each hemisphere
    # fill in using the now completed list asw as the given names
    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": hemis_url[0]},
        {"title": "Schiaparelli Hemisphere", "img_url":hemis_url[1]},
        {"title": "Syrtis Major Hemisphere", "img_url": hemis_url[2]},
        {"title": "Valles Marineris Hemisphere", "img_url": hemis_url[3]},]

    return hemisphere_image_urls

# get for mongo
def scrape():
    executable_path = {'executable_path':'C:\\driver\\chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    newest_title, newest_par = nasa_news(browser)
    feature_img_url = feature_image(browser)
    #facts = mars_table()
    hemisphere_image_urls = hemisphere_images(browser)
    timestamp = dt.datetime.now()


    #conn = "mongodb://localhost:27017"
    #client = pymongo.MongoClient(conn)

    #db = client.mars_db
    #allows for repetition if testing multiple times
    #db.mars.drop()
    info = {
        "newest_title": newest_title,
        "newest_paragraph": newest_par,
        "feature_image": feature_img_url,
        #"facts": facts,
        "hemispheres": hemisphere_image_urls,
        "last_modified": timestamp
    }
    #db.mars.insert_one(info)
    browser.quit()
    return info

if __name__ == "__main__":
    print(scrape())



