# WebScrapping

This project is done to perform webscrapping from a news website using scrapy

1. Install Scrapy:
   First, install Scrapy using the command:
   ``` bash
   pip install scrapy
   ```

2. Setup Scrapy Environment:
   Add Scrapy to your environment path variable.

3. Create Project Folder:
   Navigate to your desired location and create a project folder. Initialize a new Scrapy project with:
   ``` bash
   scrapy startproject WebScrapping
   ```

4. Create a Spider:
   Open your project in a code editor (I used VSCode) and create a spider for scraping:
   ``` bash
   scrapy genspider articles https://www.bbc.com/news
   ```

5. Inspect and Scrape the Website:
   Use Scrapy’s shell to inspect the webpage:
   ``` bash
   scrapy shell https://www.bbc.com/news
   ```

6. Identify the HTML classes or tags from which you want to extract information. For instance, to scrape article headlines:
   ``` bash
   response.css('h2.sc-4fedabc7-3.zTZri::text').get()
   ```

7. Adjust and Execute the Spider:<br>
   Modify your spider to scrape the desired data, such as headlines and summaries. Run your spider to start scraping!


8. Run the Spider:
   Execute your spider with:
   ``` bash
   scrapy crawl articles
   ```

You can change the name of project, spider, website accordingly.
