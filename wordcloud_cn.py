import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba.analyse, jieba
import numpy as np
from PIL import Image


def get_stopwords():
    stopwords = {}
    f = open('stopwords.txt', encoding='utf-8')
    line = f.readlines()
    stopwords = set([i.rstrip() for i in line])
    f.close()
    return stopwords


def seg_text():
    with open("userdict.txt", encoding='utf-8') as f:
        # content = f.read()
        # try:
        #     jieba.analyse.set_stop_words('useless_word.txt')
        #     tags = jieba.analyse.extract_tags(content, topK=100, withWeight=True)
        #     print(tags)
        # for v, n in tags:
        #         print(v+'\t'+str(int(n*10000)))
        # finally:
        #        f.close()
        text = f.readlines()
        text = r' '.join(text)
        seg_generator = jieba.cut(text)
        seg_list = [
            i for i in seg_generator if i not in get_stopwords()]
        seg_list = [i for i in seg_list if i != u' ']
        seg_list = r' '.join(seg_list)
    return seg_list


if __name__ == '__main__':
    image_mask = np.array(Image.open('alice_mask.png'))
    word_list = seg_text()
    my_wordcloud = WordCloud(background_color='white',width=800, height=800, mask=image_mask, stopwords=get_stopwords(),
                             font_path='simkai.ttf', max_font_size=100).generate(word_list)
    # image_color = ImageColorGenerator(image_mask)
    # my_wordcloud.recolor(color_func=image_color)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
