# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PhoneItem(scrapy.Item):
    ASIN = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    brand = scrapy.Field()
    model_name = scrapy.Field()
    operating_system = scrapy.Field()
    cellular_technology = scrapy.Field()
    wireless_network_technology = scrapy.Field()
    about = scrapy.Field()
