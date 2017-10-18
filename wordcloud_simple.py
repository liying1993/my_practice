from os import path
from wordcloud import WordCloud, STOPWORDS
import jieba.analyse
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
'''
jieba用来分词,matplotlib用来画图,wordcloud用来生成词云
'''

# txt_path = 'userdict.txt'
# file_in = open(txt_path, encoding="utf-8")
#
# content = file_in.read()
# try:
#     jieba.analyse.set_stop_words('useless_word.txt')
#     tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
#     print(tags)
#     for v, n in tags:
#         print(v+'\t'+str(int(n*10000)))
# finally:
#     file_in.close()

print(STOPWORDS)
d = path.dirname(__file__)
print(d)

text = open(path.join(d, 'userdict.txt'), encoding="utf-8").read()
# print(text)
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))
stopwords = set(STOPWORDS)
# stopwords.add("said")
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask, stopwords=stopwords)
wc.generate(text)
wc.to_file(path.join(d, "alice.png"))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")


# wordcloud = WordCloud().generate(text)
# print(wordcloud)


# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis("off")

# wordcloud = WordCloud(max_font_size=40).generate(text)
# plt.figure()#定义图形之后就可以作图了
# plt.imshow(wordcloud, interpolation='bicubic')
# plt.axis('off')
plt.show()