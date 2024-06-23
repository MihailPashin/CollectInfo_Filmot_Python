import scrapy
import json
import time

class FilmotSpider(scrapy.Spider):

    name = "filmot"
    with open('urls.json') as f:
        data = json.load(f)
        start_urls=[item['url'] for item in data]

    AUTOTHROTTLE_ENABLED = True
    AUTOTHROTTLE_START_DELAY = 2
    AUTOTHROTTLE_MAX_DELAY = 4
    AUTOTHROTTLE_TARGET_CONCURRENCY = 1.5
    def parse(self, response):
    
        time.sleep(4)
        for card in response.css('div[id^="vcard"]'):
            title = card.xpath('.//a/following-sibling::text()[normalize-space(.)!= ""]').get()
            picture_url = card.css('img.thumb-image::attr(src)').get()
            link = card.css('a::attr(href)')[1].get()
            count_of_views = card.css('span.badge::text').get()
            print(count_of_views)
            description = card.css('div.scroll-box ::text').getall()
            desc = [text.strip().lower() for text in description if text.strip()]
            time.sleep(0.8)

            yield {
                    "picture_url": picture_url,
                    "title": title.strip().replace(',', ''),
                    "link": link,
                    "count_of_views": count_of_views,
                    "description":desc
            }


