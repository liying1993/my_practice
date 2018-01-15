import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import LianjiaItem
import json




class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    query_url = "https://bj.lianjia.com/ershoufang/"

    def start_requests(self):
        yield Request(self.query_url, self.parse)

    def parse(self, response):
        max_num = BeautifulSoup(response.text, 'lxml').find("div", class_='house-lst-page-box')["page-data"]
        max_num = json.loads(max_num)["totalPage"]
        item = LianjiaItem()
        lis = BeautifulSoup(response.text, 'lxml').find_all("li", class_='clear')
        # print("==========max_num", lis)
        for li in lis:
            pattern = re.compile('\d+')
            houseInfo = li.select(".houseInfo")[0].get_text()
            info_arr = houseInfo.split("|")
            final_info_arr = [i.strip() for i in info_arr if i!=""]
            print(final_info_arr[0].encode('utf8'))
            item["house_fitmend"] = final_info_arr[4]
            house_area = final_info_arr[2]
            item["house_area"] = re.search(pattern,house_area).group()
            item["total_price"] = li.contents[1].contents[5].contents[0].contents[0].string
            # item["total_price"] = re.search(pattern,total_price).group()
            item['house_name'] = li.contents[1].contents[1].contents[0].contents[1].string
            item["house_located"] = li.contents[1].contents[2].contents[0].contents[2].string
            unit_price = li.contents[1].contents[5].contents[1].contents[0].string
            item["unit_price"] = re.search(pattern, unit_price).group()
            item["house_room"] = final_info_arr[1]
            item["house_towards"] = final_info_arr[3]
            yield item

        for i in range(max_num):
            per_url = self.query_url + "pg" + str(i)
            yield Request(per_url, callback=self.parse)





