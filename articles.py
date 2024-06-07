import scrapy


class ArticlesSpider(scrapy.Spider):
    name = "articles"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news",
                  "https://www.bbc.com/news/war-in-ukraine",
                  "https://www.bbc.com/news/topics/c2vdnvdg6xxt",
                  "https://www.bbc.com/news/us-canada"]

    def parse(self, response):
        
        for x in response.css("div.sc-b8778340-3.gxEarx"):
            headline = x.css("h2.sc-4fedabc7-3.zTZri::text").get()
            summary = x.css("p.sc-b8778340-4.kYtujW::text").get()

            yield{
                'Headline' : headline,
                'Summary' : summary
            }