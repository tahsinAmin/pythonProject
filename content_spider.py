import scrapy


class ContentSpider(scrapy.Spider):
    name = 'content'
    start_urls = [
        'https://www.kayak.co.in/Hyderabad-Hotels.7297.hotel.ksp',
    ]
    # ihbo

    def parse(self, response):
        counter=1
        for content in response.css('div.soom'):
            # amen = content.css('span.yRv1-text').extract()
            if counter < 11:
                list1 = content.css('span.yRv1-text::text').extract()
                list_to_string = ",".join(list1)
                demo = content.xpath('a/img/@src').get()
                if demo is None:
                    demo = content.xpath('a/span/text()').get()
                    print(demo)
                else:
                    print(demo)
                # ,
                # 'image_link': content.xpath('//a[@class="soom-photo-wrapper"]').css('img::attr(src)').get(),
                yield {
                    'image_link': content.xpath('a/img/@src').get(),
                    'title': content.xpath('div/div/div/a/span/text()').get(),
                    'ratings': content.xpath('div/div/div/div/span/text()').get(),
                    'location': content.css('span.soom-neighborhood::text').get(),
                    'amenities': list_to_string,
                    'price': content.css('span.soom-price::text').get(),
                }
                counter += 1
            else:
                break



        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
