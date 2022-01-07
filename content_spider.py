import scrapy


class ContentSpider(scrapy.Spider):
    name = 'content'
    start_urls = [
        'https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp',
    ]
    # ihbo

    def parse(self, response):
        for content in response.css('div.soom'):
            yield {
                'title': content.xpath('div/div/div/a/span/text()').get(),
                'ratings': content.xpath('div/div/div/div/span/text()').get(),
                'location': content.css('span.soom-neighborhood::text').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
