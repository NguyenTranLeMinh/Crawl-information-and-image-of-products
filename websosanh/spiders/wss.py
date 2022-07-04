
from distutils.util import execute
import scrapy
from scrapy_splash import SplashRequest
from utils.download_imgs import download_image 
from websosanh.items import WebsosanhItem

class WebsosanhSpider(scrapy.Spider):
    name = 'wss'
    allowed_domains = ['websosanh.vn']
    start_urls = ['https://websosanh.vn/dan-organ/cat-2022.htm']


    custom_settings = {
        "DUPEFILTER_DEBUG": True,
        "LOG_FILE": "log.txt"}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        products = response.xpath("//li[@class='product-item']")
        current_page = int(response.css("ul.pagination > li > a.active::attr(data-page)").get())
        total_pages = int(response.css("ul.pagination > li > a.last::attr(data-page)").get())

        item = WebsosanhItem()
        for product in products:
            
            item['name'] = product.xpath(".//a/h3/text()").get()
            #item['price'] = product.xpath(".//a/span[3]/span/text()").get().split()[2]
            #print(type(price))
            lst = [i for i in product.xpath(".//a/span[3]/span/text()").get() if i.isdigit()]
            item['price'] = int(''.join(lst))
            if product.xpath(".//a/span[1]/img/@data-src"):
                item['image'] = product.xpath(".//a/span[1]/img/@data-src").get()
            else:
                item['image'] = product.xpath(".//a/span[1]/img/@src").get()
            yield item
            download_image(url=item['image'], file_name=item['name'])

        #if current_page != total_pages:
        yield from response.follow_all(css='.pagination a',
                                callback=self.parse)


        

