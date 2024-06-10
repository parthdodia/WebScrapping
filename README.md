# WebScrapping

This project is done to perform webscrapping from a news website using scrapy

1. Install Scrapy:
   First, install Scrapy using the command:
   
   pip install scrapy

3. Setup Scrapy Environment:
   Add Scrapy to your environment path variable.

4. Create Project Folder:
   Navigate to your desired location and create a project folder. Initialize a new Scrapy project with:
   
   scrapy startproject WebScrapping

6. Create a Spider:
   Open your project in a code editor (I used VSCode) and create a spider for scraping:
   
   scrapy genspider articles https://www.bbc.com/news

8. Inspect and Scrape the Website:
   Use Scrapy’s shell to inspect the webpage:
   
   scrapy shell https://www.bbc.com/news

   Identify the HTML classes or tags from which you want to extract information. For instance, to scrape article headlines:
   
   response.css('h2.sc-4fedabc7-3.zTZri::text').get()

10. Adjust and Execute the Spider:
   Modify your spider to scrape the desired data, such as headlines and summaries. Run your spider to start scraping!


11. Run the Spider:
   Execute your spider with:
   scrapy crawl articles

You can change the name of project, spider, website accordingly.
