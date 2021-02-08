#!/usr/bin/env python
# coding: utf-8

# In[78]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[79]:


# Set the executable path and initialize the chrome browser in splinter
#executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
#browser = Browser('chrome', **executable_path)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[80]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[81]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[82]:


# ### Pull Article Headline & Summary
slide_elem.find("div", class_='content_title')


# ### Article Headline & Summary

# In[83]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[84]:


article_summary = slide_elem.find("div", class_='article_teaser_body').get_text()
article_summary


# ### Featured Images
# 

# In[85]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[86]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[87]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[88]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[89]:


# Use the base URL to create an absolute URL
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# ### Mars Facts Table

# In[90]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[91]:


df.to_html()


# ### Mars Weather

# In[92]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[93]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[94]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# In[95]:


# ### Scrape Mars' Hempispheres High Resolution Images & Titles
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[96]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []


# In[97]:


# 3. Write code to retrieve the image urls and titles for each hemisphere.

#establish for loop
#Create dictionary file
#identify hemisphere link and click through
#find the JPEG URL associated with the text "Sample"
#store url value
#identify hemisphere title and add it to the hemisphere url list
#add url & title values from hemisphere dictionary into the hemisphere image url list created above
#have browser go back to the page and repeat the for loop

for i in range(4):
    hemisphere_url = {}
    browser.find_by_css('a.product-item h3')[i].click()
    jpeg_url = browser.links.find_by_text('Sample')
    hemisphere_url['url']=jpeg_url['href']
    hemisphere_url['title']=browser.find_by_css('h2.title').text
    hemisphere_image_urls.append(hemisphere_url)
    browser.back()


# In[98]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[99]:


browser.quit()


# In[ ]:




