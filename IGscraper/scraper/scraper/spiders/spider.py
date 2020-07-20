import scrapy
import regex as re
import json
from datetime import datetime
# scrapy crawl ig

class IGSpider(scrapy.Spider):
    name = "recipes"
    data = {}

    start_urls = [
        'https://www.loveandlemons.com/recipes/main-dish-recipes/'
        # 'https://en.wikipedia.org/wiki/Ibn_Arabi#Legacy'
        # 'https://www.instagram.com/explore/tags/food/',
        # 'https://www.tiktok.com/discover?lang=en'
            # 'https://www.instagram.com/explore/tags/cook/'
            # 'http://quotes.toscrape.com/page/2/',
    ]

    def parserecipe(self, response):
        date = response.xpath(f'/html/head//meta[@property="article:published_time"]/@content')[0].extract()        
        print(f"date is {date}")        
        month = int(date[5:7])
        if (datetime.today().month != month):
            return
        else:
            index=1
            try:
                # while True:
                #     text = response.xpath(f'//*[@id="wprm-recipe-container-49475"]/div/div[12]/div/ul/li[{index}]/text()').extract()
                #     print(text)
                #     index+=1
                # //*[@id="wprm-recipe-container-49475"]/div/div[12]/div/ul/li[1]//text()
                text= response.xpath('//*[@id="wprm-recipe-container-49475"]/div/div[12]/div/ul/li[1]/span[1]').extract()
                
                print(text)
            except IndexError:
                return

    def parse(self, response):
        wordlist = ["How"]
        i=1
        
        
        while True:

            if (i == 3):
                return

            ERROR=False
            title = response.xpath(f'//*[@id="recipeindex"]/li[{i}]/a/div[3]/div[1]/text()').get()    
            # check if title contains how to etc.
            for word in wordlist:
                if word in title:
                    print("ERROR")
                    ERROR = True
                    break
            # check number
            if (re.search(r'\d', title)):
                print("NUMBER ERROR")
                ERROR = True
            
            if ERROR:
                i+=1
                continue
            

            nextpage = response.xpath(f'//*[@id="recipeindex"]/li[{i}]/a/@href').get()
            if nextpage is not None:
                nextpage = response.urljoin(nextpage)
                yield scrapy.Request(nextpage, callback=self.parserecipe)
            i+=1
        # i=0
        # while True:
        #     nextpage = response.xpath(f'//*[@id="recipeindex"]/li[{i}]/a/@href').get()
        #     if nextpage is not None:
        #         nextpage = response.urljoin(nextpage)
        #         yield scrapy.Request(nextpage, callback=self.parserecipe)
        #     print(value)
        #     i+=1
      
        # value = response.xpath('//*[@id="mw-content-text"]/div/p[1]')
        # value = response.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]')
        # value = response.xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/text()')
        # value = response.selector.xpath('//*[@id="main"]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div[1]/div/a[2]/div/strong[1]/text()').extract_first()
        # print(value)
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)