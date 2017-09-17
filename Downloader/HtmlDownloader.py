# coding : utf-8

import requests
import time
class Downloader(object):

    def __init__(self):
        self.sleep=2;

    def download(self,url):
        if url is None:
            return None
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        time.sleep(self.sleep)
        r=requests.get(url,headers=headers);
        if r.status_code==200:
            return r.content.decode("utf-8")
        return None;