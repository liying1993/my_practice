import urllib.request, sys,base64,json,os,time
from .baiduSearch import search
from PIL import Image
from aip import AipOcr
start = time.time()
os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png ./screenshot.png")
'''
汉王ocr 涨价涨价了。。
host = 'http://text.aliapi.hanvon.com'
path = '/rt/ws/v1/ocr/text/recg'
method = 'POST'
appcode = 'a962e94260ee4043b824d2f40c126d8e'    #汉王识别appcode（填你自己的）
querys = 'code=74e51a88-41ec-413e-b162-bd031fe0407e'
bodys = {}
url = host + path + '?' + querys
'''
""" （百度ocr）你的 APPID AK SK """
APP_ID = '10778787'
API_KEY = 'sizuhfENuir0VkDszacrIz0K'
SECRET_KEY = 'AjH9S8kAQyzP5vsUmXYX17NIc9bxXbpt'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



im = Image.open(r"./screenshot.png")   

img_size = im.size
w = im.size[0]
h = im.size[1]
print("xx:{}".format(img_size))

region = im.crop((70,200, w-70,700))    #裁剪的区域
region.save(r"./crop_test1.png")



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content(r"./crop_test1.png")
respon = client.basicGeneral(image)   #用完500次后可改respon = client.basicAccurate(image) 
titles = respon['words_result']          #获取问题
ans = ''
for title in titles:
      ans = ans +title['words']

tissue = ans[1:2]
if str.isdigit(tissue):            #去掉题目索引
     ans = ans[3:]   
else:
     ans = ans[2:]

print(ans)       #打印问题

keyword = ans    #识别的问题文本

convey = 'n'

if convey == 'y' or convey == 'Y':
    global results
    results = search(keyword, convey=True)
elif convey == 'n' or convey == 'N' or not convey:
    results = search(keyword)
else:
    print('输入错误')
    exit(0)
count = 0
for result in results:
    print("{0}".format(result.abstract))
    count = count+1
    if (count==2):
        break
end = time.time()
print('程序用时：'+str(end-start)+'秒')
