import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import DingdianItem


class MySpider(scrapy.Spider):
    name = "dingdian"
    allowed_domains = ["23us.so"]
    bash_url = "http://www.23us.so/list/"
    bashurl = ".html"

    def start_requests(self):
        for i in range(1,10):
            url = self.bash_url + str(i) + '_1' +self.bashurl
            yield Request(url, self.parse)
        yield Request("http://www.23us.so/full.html", self.parse)

    def parse(self, response):
        # print((response.text).encode("utf-8"))
        per_page_basic_url = response.url[:-7]
        max_num = BeautifulSoup(response.text, 'lxml').find("div", class_="pagelink").find_all("a")[-1].get_text()
        for i in range(1, int(max_num)+1):
            per_page_url = per_page_basic_url + "_" + str(i) + self.bashurl
            yield Request(per_page_url, callback=self.get_name)

    def get_name(self, response):
        trs = BeautifulSoup(response.text, "lxml").find_all("tr", bgcolor="#FFFFFF")
        for tr in trs:
            novelname = tr.find("a").get_text()
            print(novelname)
            novelurl = tr.find("a")["href"]
            yield Request(novelurl, callback=self.get_chapterurl, meta={"name": novelname, "url": novelurl})

    def get_chapterurl(self, response):
        item = DingdianItem()
        item["name"] = str(response.meta["name"]).replace("\xa0", '')
        item["novelurl"] = response.meta["url"]
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').get_text()
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].get_text()
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_="btnlinks").find("a", class_="read")["href"]
        name_id = str(bash_url)[-6:-1].replace('/', "")
        item["category"] = str(category).replace("/", "")
        item["author"] = str(author).replace("/", "")
        item["name_id"] = name_id
        item["serialstatus"] = BeautifulSoup(response.text, "lxml").find_all("tr")[0].find_all("td")[2].get_text()
        item["serialnumber"] = BeautifulSoup(response.text, "lxml").find_all("tr")[1].find_all("td")[1].get_text()
        # return item

