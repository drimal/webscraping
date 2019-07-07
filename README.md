# Scraping web using scrapy

In this webscraping project, I used scrapy to scrap apt/housing data from the city of Chicago. In the second project, I scraped short news from the inshorts.com, a news website that shortens the news to 60-words. 

# Starting a project:
Before scraping, we will have to set up a new Scrapy project. Enter a directory where you’d like to store your code and run:

`scrapy startproject MYPROJECT`

This will create MYPROJECT directory with following content:

         MYPROJECT/
         
         -scrapy.cfg   #deploy config file
         
         -__init__.py  #python module for imports
        
        -items.py    #project items
         
         middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where to put my spiders
            __init__.py
  
  
Now go to MYPROJECT directory and create a spider. 
# Generating Spider

`scrapy genspider craiglistscraper https://chicago.craigslist.org/search/see/apa?`

This will create a new spider “craiglistscraper.py” in /spiders folder with a basic template. Details on craiglistscraper/spiders/craiglistscrapper.py

# Running Spider

`scrapy crawl craiglistscraper`



