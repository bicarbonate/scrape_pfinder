import scrapy

class Find_bhart(scrapy.Spider):
    name = "find_bhart"
    start_urls = ['http://www.peoplefinder.com/people-search/MT-Jefferson%20City-Benjamin-Hart/']

    def parse(self, response):
        for url in response.css('ul li a::attr("href")').re(r'.*/\d\d\d\d/\d\d/$'):
            yield scrapy.Request(response.urljoin(url), self.parse_titles)

    def parse_titles(selfself, response):
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}
