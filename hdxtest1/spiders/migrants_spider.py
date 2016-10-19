import scrapy

class MigrantSpider(scrapy.Spider):
    name = "migrants"

    def start_requests(self):
        urls = [
            'http://missingmigrants.iom.int/latest-global-figures',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        migrant = MigrantItem()
        table2 = response.xpath('//table')[1]
        table2_body = table2.xpath('//tbody/tr')
        print(table2_body)
        for row in table2_body:
            print(row)


class MigrantItem(scrapy.Item):
    mediterranean = scrapy.Field()
    europe = scrapy.Field()
    middle_east = scrapy.Field()
    north_africa = scrapy.Field()
    horn_africa = scrapy.Field()
    sub_saharan_africa = scrapy.Field()
    east_asia = scrapy.Field()
    southeast_asia = scrapy.Field()
    us_mexico_border = scrapy.Field()
    central_america = scrapy.Field()
    carribean = scrapy.Field()
    total = scrapy.Field()
