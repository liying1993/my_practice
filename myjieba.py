# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator,STOPWORDS
# import jieba
# import numpy as np
# from PIL import Image
#
# abel_mask = np.array(Image.open("ly3.jpeg"))
# print(Image.open("ly3.jpeg"))
# # print(abel_mask)
# text_from_file_with_apath = open('userdict.txt', encoding='utf-8')
# wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
# print(wordlist_after_jieba)
# wl_space_split = " ".join(wordlist_after_jieba)
# my_wordcloud = WordCloud(
#             background_color='white',
#             mask = abel_mask,
#             max_words = 200,
#             stopwords = STOPWORDS,
#             font_path = 'simkai.ttf',
#             max_font_size = 50,
#             random_state = 30,
#                 scale=.5
#                 ).generate(wl_space_split)
# image_colors = ImageColorGenerator(abel_mask)
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()

import jieba.analyse

path = 'userdict.txt'
file_in = open(path, encoding="utf-8")

content = file_in.read()
try:
    jieba.analyse.set_stop_words('useless_word.txt')
    tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
    print(tags)
    for v, n in tags:
        print(v+'\t'+str(int(n*10000)))
finally:
    file_in.close()

