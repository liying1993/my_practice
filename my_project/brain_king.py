from PIL import ImageGrab
'''
整体项目的思路就是：
1、自动截图，自动截图使用PIL
2、使用OCR识别问题和答案
3、调用搜索引擎爬虫
'''

def screen_crop():
    image = ImageGrab.grab()
    image.save("")

def OCR_regnization():
    pass

def seo_engine():
    pass