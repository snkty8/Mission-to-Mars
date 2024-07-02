# Mission-to-Mars

## Overview 
The purpose of this project was to create a web app that displays Mars facts.  To do this, we used Beautiful Soup and Splinter to scrape headlines, facts, full resolution images of Mar's hemispheres, and the titles of those images.  Then, store them in MongoDB database, and use a web app to display the data.

## Mars Facts 

![image](https://github.com/snkty8/Mission-to-Mars/blob/main/screenshot_Mission_to_Mars.png)

This is the original app created to display Mars facts.  In order to get the most recent Mars news, we scraped data from:
[Mars](https://data-class-mars.s3.amazonaws.com/Mars/index.html)

To get the displayed surface picture and facts table, we used:
[Mars Facts](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html)

## Mars Hemispheres

![image](https://github.com/snkty8/Mission-to-Mars/blob/main/Mission_to_Mars_Site_pic.png)

To make the web app more informative, we added full HD images of Mars hemispheres.  This was done by scraping data from:
[Mars Images](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)

Using python code in jupyter notebook, a function was created to parse through the website, and find the image titles and urls. This information was then put into a python dictionary.  The dictionary was then loaded into MongoDB.  Using a flask app, we were able to load all the information into a local web app. The app was paired with an index.html file.  This file was then updated to change the scrape button, image size, and background color. Also checked to see if the app was mobile responsive.



## Problems and Issues

In order to get the Mars hemisphere images, I scraped the specified URLs above. The images and URLs needed to placed into a dictionary ready for MongoDB to read.  I initially had an issue with my dictionary. The dictionary I created was not in the correct formart.  This caused MongoDB to bring up all the URLs and titles at one time, instead of one after the next.  In short, my web app did not work.  Once I fixed this problem, my web app work perfectly fine. 

Secondly, I am not well versed in html.  I feel as if my app looks basic, but I was able to tweek a few things.  I was able to change the color and the scrape button.  I was also able to change the background color.  This just lets me know what I need to work on in the future.  All in all, I am proud of my progress and more than willing to work to make my work more visually appealing.  I am far from an expert in this area, but more the willing work to get there. 

Tried updating the web app, but the Latest ChromeDriverManager has not been updated for the latest version on Chrome. Will have to update at a later date. 
