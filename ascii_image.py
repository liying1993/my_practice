from __future__ import print_function
from PIL import Image, ImageFilter, ImageEnhance, ImageMorph
import os, sys

"""
图片转字符画的关键就是将图片的灰度值与你自己设定的字符集之间建立映射关系，不同区间的灰度值对应不同的字符，之后将图片每一个像素对应的字符打印出来就是字符画了
先将彩色图片转换为黑白图片，然后直接将每个像素点的灰度值与字符集建立映射。
获取图片的RGB值，利用公式： 
Gray = R*0.299 + G*0.587 + B*0.114 
计算可得每个像素点的灰度值，之后再建立映射即可。
"""

def acsii_image(path):
    codeLib = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''  # 生成字符
    codePic = ""
    count = len(codeLib)
    img = Image.open(path)
    width, height = img.size
    print(count)
    # img = img.convert("L")
    for h in range(0, height):
        for w in range(0, width):
            r,g,b = img.load()[w,h]
            gray = int(r*0.299+g*0.587+b*0.114)
            codePic = codePic + codeLib[int(((count-1)*gray)/256)]
        codePic = codePic+'\r\n'
    print(codePic)
    return codePic
    # img.show()
    # img_array = img.load()
    # print(img_array[0,0])


if __name__ == "__main__":
    acsii_image("/Users/liying/Documents/images/ly5.jpg")
# def ascii_image(path):
#     im = Image.open(path,"L")
#     test = ImageMorph.MorphOp()
#     aa = test.get_on_pixels(im)
#     print(aa)
    # im.seek(1)
    # try:
    #     while 1:
    #         im.seek(im.tell()+1)
    # except EOFError:
    #     pass
    # im.show()
    # enh = ImageEnhance.Contrast(im)
    # enh.enhance(1.3).show("30% more contrast")
    # im.show()
    # source = im.split()
    # R,G,B = 0,1,2
    # mask = source[R].point(lambda i:i<100 and 255)
    # # mask.show()
    # out = source[G].point(lambda i:i*0.7)
    # out.show()
    # source[G].paste(out, None, mask)
    # im = Image.merge(im.mode, source)
    # print(im)
    # out = im.convert("L")
    # out = im.filter(ImageFilter.DETAIL)
    # out = im.transpose(Image.FLIP_LEFT_RIGHT)
    # out = im.transpose(Image.FLIP_TOP_BOTTOM)
    # out = im.transpose(Image.ROTATE_90)
    # out.show()
    # out = im.resize((128,128))
    # out.show()
    # out1 = im.rotate(45)
    # out1.show()
    # r,g,b = im.split()
    # im = Image.merge("RGB", (b,g,r))
    # im.show()
    # xsize, ysize = im.size
    # print(xsize, ysize)
    # delta = delta % xsize
    # if delta == 0: return im
    #
    # part1 = im.crop((0,0,delta,ysize))
    # part2 = im.crop((delta,0,xsize,ysize))
    #
    # part1.load()
    # part2.load()
    # im.paste(part2, (0,0,xsize-delta,ysize))
    # im.paste(part1, (xsize-delta,0,xsize,ysize))
    # im.show()
    # return im
    # f ,e = os.path.splitext(path)
    # print(f+"     "+e)
    # outfile = f + ".png"
    # try:
    #     Image.open(path).save(outfile)
    # except IOError:
    #     print("cannot convert", path)
    import pdb
    # pdb.set_trace()
    # size = (128, 128)
    # outfile = os.path.splitext(path)[0] + ".thumbnail"
    # im = Image.open(path)
    # box = (100, 100, 100, 100)
    # region = im.crop(box)
    # im.thumbnail(size)
    # im.save(outfile, "JPEG")




# im = Image.open("/Users/liying/Documents/images/ly5.jpg")
# print(im.format, im.size, im.mode)
# im.show()
