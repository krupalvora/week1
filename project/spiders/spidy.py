from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
import scrapy 
import json
class art(CrawlSpider):
    name='article'
    allowed_domains=["communityrecmag.com"]    
    start_urls=["https://communityrecmag.com/"]
    rules=(Rule(LinkExtractor(allow=["https\:\/\/communityrecmag\.com\/.+"]),callback="parse_item",follow=True,),)
 
    def parse_item(self,response):

        a=response.xpath('//*[@id="content-wrapper"]/div[2]/@style').extract()
        b= response.xpath('//div[@class="tt-blog-category text-center"]/a/text()').extract()
        c= response.xpath('//div[@class="tt-blog-category text-center"]/a/@href').extract()
        d=response.xpath("//h1[@class='c-h1 text-center']/text()").extract()
        e=response.xpath("//span[@class='tt-post-author-single']/a/text()").extract()
        v= response.xpath("//span[@class='tt-post-date-single']/text()").extract()
        k=response.xpath("//div[@class='col-md-8']/div[3]//text()").extract()
        i= response.xpath("//ul[@class='tt-tags']/li/a/text()").extract()
        l= response.xpath('//div[@class="col-md-8"]/div[3]//img/@src').extract()
        filename=str(d)+".json"
        dict={}
        dict['image']=a
        dict['buttons']=b
        dict['but-links']=c
        dict['head']=d
        dict['author']=e
        dict['date']=v          
        dict['text']=k
        dict['tags']=i
        dict['image(ALL)']=l
        with open(filename,'w') as f :
            json.dump(dict,f)
        