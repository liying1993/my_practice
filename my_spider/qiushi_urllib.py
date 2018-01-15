import urllib.request
import re

page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5;Windows NT)'
headers = {'User-Agent': user_agent}

# 获取发布人、发布日期、段子内容、以及点赞的个数
try:
    request = urllib.request.Request(url, headers=headers)
    # print(request)
    response = urllib.request.urlopen(request)
    content = str(response.read(), encoding="utf-8")
    pattern = re.compile(
        '<div class="author clearfix">.*</div>')
    items = re.findall(pattern, content)
    print(items)
except Exception as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)
