from aip import AipOcr
import time
import requests
from bs4 import BeautifulSoup
import urllib.parse, urllib.request
import _thread

'''
1、首先是获取图片关键词
2、然后得到百度页面
3、然后根据搜索引擎获得每一个页面问题答案出现的次数，统计最多的，以最多的为最终答案
'''
config = {
    "appId": "10778787",
    "apiKey": "sizuhfENuir0VkDszacrIz0K",
    "secretKey": "AjH9S8kAQyzP5vsUmXYX17NIc9bxXbpt",
}

client = AipOcr(**config)
__url = "http://www.baidu.com/s?wd=" #根据关键词搜索百度

"""读取图片"""
def get_file_content(filepath):
    with open(filepath, 'rb') as fp:
        return fp.read()

def img_to_str(image_path):
    start = time.time()
    image = get_file_content(image_path)
    result = client.basicGeneral(image)
    titles = result["words_result"]
    keyword = []
    for title in titles:
        try:
            index = title["words"].index(".")
            title = title["words"][index+1:]
            keyword.append(title)
        except Exception:
            question = title["words"]

    return question, keyword


class Engine(object):
    def __init__(self, issue, answer):
        self.start = time.time()
        self.issue = issue
        self.answer = answer
        self.answer1_num = 0
        self.answer2_num = 0
        self.answer3_num = 0
        self.count = 0

    def gethtml(self, url):
        headers = ('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')

        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        date = opener.open(url).read()

        if "zhidao.baidu.com" in url:
            str1 = date.decode('gbk').encode('utf-8').decode('utf-8')
        else:
            str1 = str(date, "utf-8")

        self.count += 1
        self.a += str1.count(self.answer[0].replace('A', ''))
        self.b += str1.count(self.answer[1].replace('B', ''))
        self.c += str1.count(self.answer[2].replace('C', ''))



    def threhtml(self, url):
        _thread.start_new_thread(self.gethtml, (url,))

    def biggest(self,a,b,c):  #获取出现次数最多的答案
         if a>b:
             maxnum = a
         else:
             maxnum = b
         if c>maxnum:
             maxnum=c
         return maxnum

    def baidu(self,query_url):
        '''
        搜索关键字得到关于所提问题的全部页面，目前只分析第一页
        :param keyword:
        :return:
        '''
        result = requests.get(query_url)
        if result.status_code == 200:
            return result.text
        else:
            print(result.status_code)
            pass
    def filter_links(self, text):
        '''
        筛选结果页面里面的链接
        :param text: 
        :return: 
        '''
        soup = BeautifulSoup(text, "lxml")
        ans_urls = soup.select(".ti")
        urls = [i.get("href") for i in ans_urls]
        for i in urls:
            child_text = self.baidu(i)
            child_soup = BeautifulSoup(child_text, 'lxml')
            strs = child_soup.select(".best-text")[0].text.encode("ascii").decode("utf-8")
            print(1)



    def search(self):
        baidu = "https://zhidao.baidu.com/search?lm=0&rn=10&pn=0&fr=search&ie=gbk&word=" + self.issue

        sousou = "http://wenwen.sogou.com/s/?w=" + urllib.parse.quote(self.issue) + "&ch=ww.header.ssda"

        iask = "https://iask.sina.com.cn/search?searchWord=" + urllib.parse.quote(self.issue) + "&record=1"

        so360 = "https://wenda.so.com/search/?q=" + urllib.parse.quote(self.issue)

        urls = [baidu, sousou, iask, so360]

        for url in urls:
            text = self.baidu(url)
            self.filter_links(text)

if __name__ == '__main__':
    question, ans = img_to_str("lala.jpg")
    engine = Engine(question, ans)
    engine.search()



# def baidu(keyword):
#     '''
#     搜索关键字得到关于所提问题的全部页面，目前只分析第一页
#     :param keyword:
#     :return:
#     '''
#     result = requests.get(__url+keyword)
#     if result.status_code == 200:
#         return result.text
#     else:
#         print(result.status_code)
#         pass






#     convey = 'n'
#
#     if convey == 'y' or convey == 'Y':
#         global results
#         results = search(keyword, convey=True)
#     elif convey == 'n' or convey == 'N' or not convey:
#         results = search(keyword)
#     else:
#         # print('输入错误')
#         exit(0)
#     count = 0
#     for result in results:
#         # print("{0}".format(result.abstract))
#         count = count + 1
#         if (count == 2):
#             break
#     end = time.time()
#     # print('程序用时：' + str(end - start) + '秒')
#
# __url = 'http://www.baidu.com/s?wd='  # 搜索请求网址


def spage(word):
    r = requests.get(__url + word)
    if r.status_code == 200:  # 请求错误（不是200）处理
        return r.text
    else:
        # print(r.status_code)
        return False

def url(r_url):
    return requests.get(r_url).url


# 获取title和c_url，这俩货恰好可以一起
def __get_title_and_c_url(result_div):
    r_from = result_div.find('a')  # 先获取第一个<a>，r refers to result
    if not r_from:
        return [None, None]
    for em in r_from.find_all('em'):  # 移除title中的em标签
        em.unwrap()
    return [r_from.get_text(), r_from['href']]


# 获取abstract
def __get_abstract(result_div):
    if 'result-op' not in result_div['class']:  # 不是软广
        r_from = result_div.find(class_='c-abstract')
        if not r_from:
            return None
        for em in r_from.find_all('em'):  # 移除abstract中的em标签
            em.unwrap()
        return r_from.get_text()
    else:
        return '百度软广，当前代码版本不予摘要'  # 其实是因为太麻烦


# 获取show_url
def __get_show_url(result_div):
    show = result_div.find(class_='c-showurl')
    if not show or show == '<span class="c-showurl"> </span>':  # 有些软广class不一样
        show = result_div.find(class_='c-showurl-color')
    if not show:  # 要是还不一样。。
        return '此结果未能如期获取到show url，提交issue帮助我们做的更好'
    return show.get_text()[:-2]  # 去除末尾/

class Result(object):

    def __init__(self, r_index, r_title, r_abstract, show_url, r_url):  # id似乎占用了内部名称，那就用index来代替吧
        self.__index = r_index
        self.__title = r_title
        self.__abstract = r_abstract
        self.__show_url = show_url
        self.__url = r_url

    @property
    def index(self):
        return self.__index

    @property
    def title(self):
        return self.__title

    @property
    def abstract(self):
        return self.__abstract

    @property
    def show_url(self):
        return self.__show_url

    @property
    def url(self):
        return self.__url

    def convey_url(self):
        self.__url = url(self.__url)

def ppage(html):
    # 初始化
    soup = BeautifulSoup(html, 'lxml')
    results = []

    # 获取结果来源
    result_set = soup.find(id='content_left')  # 结果全显示在页面左边
    result_set = result_set.find_all('div', class_='c-container')  # 结果class固定，其余为硬广

    for i in range(len(result_set)):  # 因为要index所以就用range来
        result = result_set[i]  # 其实就是result_div

        t_and_u = __get_title_and_c_url(result)
        c_title = t_and_u[0]  # 这个c_title就是title了
        c_url = t_and_u[1]  # c_url是百度的url，需要转换
        c_abstract = __get_abstract(result)  # 同title
        c_show_url = __get_show_url(result)

        result = Result(i + 1, c_title, c_abstract, c_show_url, c_url)
        results.append(result)

    return results

def search(keyword, **kwargs):
    kwargs.setdefault('convey', False)
    page = spage(keyword)
    results = ppage(page)
    if kwargs['convey']:
        for result in results:
            result.convey_url()
    return results



if __name__ == '__main__':
    img_to_str("lala.jpg")


