# WebScrapping

This project is done to perform webscrapping from a news website using scrapy

1. Install scrapy in your environment using cmd
      'pip install scrapy'
2. Add scrapy to the environment path variable
3. Go to your desired location and create a project folder
   'scrapy startproject WebScrapping'
4. Open the project folder in a code editor of your choice. I used VSCode.
5. Open the terminal and create a spider for scrapping
   'scrapy genspider articles https://www.bbc.com/news'
   A .py file(spider) will be created in the environment. This is your main file and used to perform scrapping.
6. Execute the following code to perform and adjust precise scrapping in the terminal
   'scrapy shell https://www.bbc.com/news'
7. Inspect the page to find the class
8. Execute the following code to scrap the information from the class
   'response.css('h2.sc-4fedabc7-3.zTZri::text').get()'
   This will scrap out the first value from the mentioned class.
9. Similarly, you can scrap different information of your choice. I scraped headings and summary.
10. Make adjustments to your spider and run the file.
