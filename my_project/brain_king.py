from PIL import ImageGrab, Image
import sys
import pyocr
import pyocr.builders
import pytesseract

'''
整体项目的思路就是：
1、自动截图，自动截图使用PIL
2、使用OCR识别问题和答案
3、调用搜索引擎爬虫
'''

path = "/Users/liying/Documents/images/lala.jpeg"


def screen_crop():
    image = ImageGrab.grab(bbox=(1034,500,1750,900))
    image.show()
    image = image.convert("RGB")
    image.save("lala.jpg")


def OCR_regnization():
    img = Image.open("3.jpeg")
    code = pytesseract.image_to_string(img, lang="eng")
    print(code)
    # tools = pyocr.get_available_tools()
    # if len(tools) == 0:
    #     print("No OCR tool found")
    #     sys.exit(1)
    # # The tools are returned in the recommended order of usage
    # tool = tools[0]
    # print("Will use tool '%s'" % (tool.get_name()))
    # # Ex: Will use tool 'libtesseract'
    #
    # langs = tool.get_available_languages()
    # print("Available languages: %s" % ", ".join(langs))
    # lang = langs[14]
    # print("Will use lang '%s'" % (lang))
    #
    # txt = tool.image_to_string(
    #     Image.open('lala.jpg'),
    #     lang=lang,
    #     builder=pyocr.builders.TextBuilder()
    # )

    # word_boxes = tool.image_to_string(
    #     Image.open('lala.jpg'),
    #     lang=lang,
    #     builder=pyocr.builders.WordBoxBuilder()
    # )

    # line_and_word_boxes = tool.image_to_string(
    #     Image.open('lala.jpg'), lang=lang,
    #     builder=pyocr.builders.LineBoxBuilder()
    # )

    # digits = tool.image_to_string(
    #     Image.open('lala.jpg'),
    #     lang=lang,
    #     builder=pyocr.tesseract.DigitBuilder()
    # )
    # print(txt)




def seo_engine():
    pass


if __name__ == '__main__':
    # screen_crop()
    OCR_regnization()
