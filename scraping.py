from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)
    #hemispheres = hemisphere(browser)


    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

def hemisphere(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # 2. Create a list to hold the images and titles.
    # HTML Object
    html_hemispheres = browser.html

    # Parse HTML with Beautiful Soup
    image_soup = soup(html_hemispheres, 'html.parser')

    # Retreive all items that contain mars hemispheres information
    #results = image_soup.find_all('div', class_='collapsible results')

    prac = image_soup.body.find_all('h3')

    title = []

    for pr in prac:
        title.append(pr.text)

    #title

    # Create empty list for hemisphere urls 
    #hemisphere_image_urls = []

    thumbnail_results = image_soup.body.find_all('a', class_ = 'itemLink product-item')
    thumbnail_links = []

    for thumbnail in thumbnail_results:
    
        # If the thumbnail element has an image...
        if (thumbnail.img):
        
        # then grab the attached link
            thumbnail_url = 'https://astrogeology.usgs.gov' + thumbnail['href']
        
        # Append list with links
            thumbnail_links.append(thumbnail_url)

    #thumbnail_links

    # Store the main_ul 
    #hemisphere_url = 'https://astrogeology.usgs.gov'

    # Loop through the items previously stored
    #for result in results: 
    
    
    
    # Store link that leads to full image website
    
    img_url = []    
    
    # Visit the link that contains the full image website 
    for urls in thumbnail_links:
        
        browser.visit(urls)
    
        # HTML Object of individual hemisphere information website 
        partial_img_html = browser.html
    
        # Parse HTML with Beautiful Soup for every individual hemisphere information website 
        parse = soup(partial_img_html, 'html.parser')
            
        # Retrieve full image source 
        img_urls = parse.body.find('a', text = 'Sample')['href']
        img_url.append(img_urls)
        
    mars_hemi_zip = zip(title, img_url)

    hemispheres = []

        # Iterate through the zipped object
    for titles, img in mars_hemi_zip:
    
        mars_hemi_dict = {}
    
            # Add hemisphere title to dictionary
        mars_hemi_dict['title'] = titles
    
            # Add image url to dictionary
        mars_hemi_dict['img_url'] = img
    
            # Append the list with dictionaries
        hemispheres.append(mars_hemi_dict)
        
    
    return hemispheres

# 5. Quit the browser
    #browser.quit()    


if __name__ == "__main__":
    print(scrape_all())