# coding : utf=8
import re
from bs4 import BeautifulSoup


class Parser(object):

    def parser(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return;

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(page_url, soup)
        data = self._get_new_data(page_url, soup)
        return (new_urls, data)

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/'))
        for link in links:
            try:
                new_url = link['href']
                new_full_url = 'https://baike.baidu.com' + new_url
                new_urls.add(new_full_url)
            except:
                pass
        return new_urls

    def _get_new_data(self, page_url, soup):
        data = {}
        data['url'] = page_url
        try:
            title = soup.find('dd', attrs={'class': 'lemmaWgt-lemmaTitle-title'}).find('h1')
            data['title'] = title.get_text()
            summary = soup.find('div', attrs={'class': 'lemma-summary'})
            data['summary'] = summary.get_text()
        except:
            pass

        return data
