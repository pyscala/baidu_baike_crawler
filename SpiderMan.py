# coding : utf-8

from UrlManager.UrlManager import UrlManager
from Downloader.HtmlDownloader import Downloader
from Parser.Parser import Parser
from DataManager.DataManager import DataManager
from DBUtils.MongoUtils import MongoUtils


class SpiderMan(object):
    def __init__(self):
        self.number=100
        self.urlManager = UrlManager()
        self.downloader = Downloader()
        self.parser = Parser()
        self.dataManager = DataManager()
        self.dbManager = MongoUtils()

    def set_crawler_number(self,num):
        if num is None or int(num) <0 :
            return
        self.number=int(num)


    def crawler(self, root_url):
        self.urlManager.add_new_url(root_url)
        while (self.urlManager.has_new_url() and self.urlManager.old_urls_size() < self.number):
            try:
                new_url = self.urlManager.get_new_url()
                html = self.downloader.download(new_url)
                result = self.parser.parser(new_url, html)
                self.urlManager.add_new_urls(result[0])
                self.dataManager.store_data(result[1])
            except Exception as err:
                print("crawl failed" + err)

        self.dataManager.output_data()
        datas = self.dataManager.get_data()
        self.dbManager.insert_baike_many(datas)



if __name__ == "__main__":
    spider_man = SpiderMan()
    # 所需要的百度百科的数量
    number=500
    spider_man.set_crawler_number(number)
    #入口url
    url ="https://baike.baidu.com/item/网络爬虫/5162711"

    spider_man.crawler(url)
