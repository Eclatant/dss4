# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import redis
from bs4 import BeautifulSoup
#import newsdao
from newsdao import NewsDAO

def find_a(tags):
    return tags.name == 'a' and not tags.has_attr('class') and tags.has_attr('href')

class NaverNewsCrawler(object):
    def __init__(self, newsdao, urls):
        self.newsdao = newsdao
        self.urls = urls

    def crawl_link(self):
        for url in self.urls:
            res = requests.get(url)
            content = res.content

            soup = BeautifulSoup(content)

            table = soup.find('table', attrs = {'class' : 'container'})
            for a in table.find_all(find_a):
                link = a['href']
                self.crawl_title_content(link)

    def crawl_title_content(self, link):
        res = requests.get(link)
        content = res.text

        soup = BeautifulSoup(content)

        # soup 에서 javascript 제거
        for script in soup(["script", "style"]):
            script.extract()

        # title 추출
        title = soup.find('h3', attrs = {'id' : 'articleTitle'})
        if title == None or title == '':
            return
        title = title.text

        # 본문 추출
        content = soup.find('div', attrs = {'id' : 'articleBodyContents'})
        if content == None or content == '':
            return
        content = content.text.strip()

        print link
        print title

        try:
            # 한번에 쓰도록 수정해야함
            self.newsdao.save_news(link, str(title), str(content))
        except Exception, e:
            print e

r = redis.Redis(host='localhost', port=6379)
urls = r.lrange('urls', 0, -1)

newsdao = NewsDAO()
crawler = NaverNewsCrawler(newsdao, urls)

import time 
start = time.time()
crawler.crawl_link()
end = time.time()

print '{} seconds took to finish'.format(end - start)
