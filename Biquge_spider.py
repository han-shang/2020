"""
笔趣阁小说抓取
"""
import requests
import re
import time
import random
import pymysql


class BiqugeSpider:
    def __init__(self):
        """定义常量"""
        self.url = 'https://www.biqukan.cc/fenlei1/{}.html'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
        self.db = pymysql.connect("localhost","root",'123456',"biqugedb",charset="utf8")
        self.cur = self.db.cursor()

    def get_html(self, url1):
        """发请求获取响应内容"""
        html = requests.get(url=url1, headers = self.headers).text

        self.parse_html(html)

    def parse_html(self,html):
        """解析提取函数"""
        regex = '<div class="caption">.*?href="(.*?)" title="(.*?)">.*?<small.*?>(.*?)</small><p class=".*?">(.*?)</p>'
        re_list = re.findall(regex, html, re.S)
        self.save_html(re_list)

    def save_html(self,re_list):
        """数据处理函数"""
        for r in re_list:
            item = {}
            item["title"] = r[1]
            item['href'] = r[0]
            item['author'] = r[2]
            item['comment'] = r[3]
            sql = 'insert into novel values(%s,%s,%s,%s);'
            self.cur.execute(sql,r)
            self.db.commit()
            print(item)

    def crawl(self):
        """爬虫逻辑函数"""
        for page in range(1,3):
            page_url = self.url.format(page)
            self.get_html(url1=page_url)
            #控制频率
            time.sleep(random.randint(1,3))


if __name__ == '__main__':
    s = BiqugeSpider()
    s.crawl()
