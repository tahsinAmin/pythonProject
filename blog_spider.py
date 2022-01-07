import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'blogs'
    start_urls = [
        'https://www.zyte.com/blog/',
    ]
    # 'title_c': blog.css('span.text::text').get(),
    def parse(self, response):
        for blog in response.css('div.oxy-post'):
            print(blog.xpath('div/div/a/text()').get())
            yield {
                'title_p': blog.xpath('div/div/a/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)