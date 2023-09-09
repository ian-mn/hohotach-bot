import scrapy


class OdnoklassnikiParserItem(scrapy.Item):
    hashsum = scrapy.Field()
    image_url = scrapy.Field()
    description = scrapy.Field()
    group_url = scrapy.Field()
