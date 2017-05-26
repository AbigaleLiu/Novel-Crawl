from scrapy import Spider
from NovelCrawlScrapy.items import NovelcrawlscrapyItem


class NovelCrawl(Spider):
    name = "NovelCrawl"  # 设置爬虫名
    allowed_domains = ["fushuwang.com"]  # 域名
    start_urls = ["http://www.fushuwang.com/2017/65554.html"]  # 爬虫起始地址

    # 爬取方法
    def parse(self, response):
        text = []
        item = NovelcrawlscrapyItem()  # 实例化一个容器保存爬取到的数据
        # extract(): 返回xpath选择器（列表）对应的节点的字符串（列表）
        item["file_name"] = response.xpath("/html/body/table[4]/tr/td[1]/table[2]/tr/td/table[1]/tr[1]/td/h1/text()").extract()
        file_path = "D:\PyWork\\NovelCrawlScrapy\\Novels\%s.txt" % item["file_name"][0]
        print((file_path))
        for sel in response.xpath("//*[@id='text']"):
            item["text"] = sel.xpath("p/text()").extract()
        with open(file_path, "a", encoding="utf-8") as f:
            for text in item["text"]:
                f.write(text)


        yield item  # 返回数据
        