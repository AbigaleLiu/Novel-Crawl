from scrapy import cmdline


class Run:
    def run(self, spider_name):
        cmd = "scrapy crawl %s" % spider_name
        cmdline.execute(cmd.split())

if __name__ == '__main__':
    r = Run()
    r.run("NovelCrawl")