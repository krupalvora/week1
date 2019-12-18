import scrapy
import json
class t(scrapy.Spider):
    name='abc'

    def start_requests(self) :part
         urls=["https://communityrecmag.com/stronger-member-staff-relationships-crucial-success/"]
         for url in urls :
            yield scrapy.Request(url = url,callback = self.parse)
 
    def parse(self,response):

        a=response.xpath('//*[@id="content-wrapper"]/div[2]/@style').extract()
        b= response.xpath('//div[@class="tt-blog-category text-center"]/a/text()').extract()
        c= response.xpath('//div[@class="tt-blog-category text-center"]/a/@href').extract()
        d=response.xpath("//h1[@class='c-h1 text-center']/text()").extract()
        e=response.xpath("//span[@class='tt-post-author-single']/a/text()").extract()
        v= response.xpath("//span[@class='tt-post-date-single']/text()").extract()
        k=response.xpath("//div[@class='col-md-8']/div[3]//text()").extract()
        i= response.xpath("//ul[@class='tt-tags']/li/a/text()").extract()
        l= response.xpath('//div[@class="col-md-8"]/div[3]//img/@src').extract()




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
        with open("dict.json",'w') as f :
            json.dump(dict,f)
        