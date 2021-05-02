# Mission-to-Mars

## Overview 
The purpose of this project was to create a web app that displays Mars facts.  To do this, we used Beautiful Soups and Splinter to scrape full resolution images of Mar's hemispheres and the titles of those images, store them in MongoDB database, and use a web app to display the data.

## Mars Facts 

![image](https://github.com/snkty8/Mission-to-Mars/blob/main/screenshot_Mission_to_Mars.png)

This is the original app created to display Mars facts.  In order to get the most recent Mars news, we scraped data from:
https://data-class-mars.s3.amazonaws.com/Mars/index.html

To get the displayed surface picture and facts table, we used:
https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html

## Mars Hemispheres

![image](https://github.com/snkty8/Mission-to-Mars/blob/main/Mission_to_Mars_Site_pic.png)

To make the web app more informative, we added full HD images of Mars hemispheres.  This was done by scraping data from:
https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars

Using python code jupyter notebook, a function was created to parse through the website, and find the image titles and urls. This information was then put into a python dictionary.  The dictionary was then loaded into MongoDB.  Using a flask app, we were able to load all the information into a local web app. THe app was paired with an index.html file.  This file was then updated to change the scrape button, image size, and background color. Also checked to see if the app was mobile responsive.



