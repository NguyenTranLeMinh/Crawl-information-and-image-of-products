from distutils.util import execute
import scrapy
from scrapy_splash import SplashRequest

from utils.download_imgs import download_image 
from shopee_crawl.items import ShopeeCrawlItem

class ShopeeSpider(scrapy.Spider):
    name = 'shopee'
    allowed_domains = ['websosanh.vn']
    start_urls = ['https://websosanh.vn/dan-organ/cat-2022.htm']

    scripts = '''
        function main(splash)
            local url = splash.args.url
            assert(splash:go(url))
            assert(splash:wait(0.5))
            assert(splash:runjs("$('ul.pagination > li > a.next').click();"))
            assert(splash:wait(0.5))
            return {
                html = splash:html(),
                url = splash:url(),
            }
        end
    '''

    def start_requests(self):
        #yield scrapy.Request(url=self.start_urls[0], callback=self.parse, dont_filter=True)

        # yield SplashRequest(url=self.start_urls[0],
        #                     callback=self.parse,
        #                     endpoint='execute',
        #                     args={'lua_source': self.scripts})

        for url in self.start_urls:
            yield SplashRequest(url, endpoint="render.html", callback=self.parse)


    def parse(self, response):
        products = response.xpath("//li[@class='product-item']")
        item = ShopeeCrawlItem()
        for product in products:
            item['name'] = product.xpath(".//a/h3/text()").get()
            item['price'] = product.xpath(".//a/span[3]/span/text()").get().split()[2]
            #print(type(price))
            item['image'] = product.xpath(".//a/span[1]/img/@src").get()
            yield item
            download_image(url=item['image'], file_name=item['name'])


        yield SplashRequest(url=response.url,
                            callback=self.parse,
                            endpoint="execute", 
                            args={"lua_source": self.scripts})



        
        # yield SplashRequest(url=response.url,
        #                     callback=self.parse,
        #                     meta={
        #                         "splash": {"endpoint": "execute", "args": {"lua_source": self.scripts}}
        #                     })

        

