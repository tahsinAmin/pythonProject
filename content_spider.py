import scrapy
import json


class ContentSpider(scrapy.Spider):
    name = 'content'
    start_urls = [
        'https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp',
    ]

    # ihbo

    def parse(self, response):

        counter = 1
        for content in response.css('div.soom'):
            if counter < 11:
                title = content.xpath('div/div/div/a/span/text()').get()
                list1 = content.css('span.yRv1-text::text').extract()
                list_to_string = ",".join(list1)
                demo = content.xpath('a/img/@src').get()

                if demo == None:
                    try1 = response.xpath(f"(//script[contains(text(),'{title}')])/text()").getall()
                    data = json.loads(try1[0])
                    demo = data.get('image')

                    if demo:
                        yield {
                            'image_link': demo,
                            'title': title,
                            'ratings': content.xpath('div/div/div/div/span/text()').get(),
                            'location': content.css('span.soom-neighborhood::text').get(),
                            'amenities': list_to_string,
                            'price': content.css('span.soom-price::text').get(),
                        }
                        counter += 1
                    else:
                        print("Skipped an element")
            else:
                break

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
