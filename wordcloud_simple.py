from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)
print(d)

text = open(path.join(d, 'constitution.txt')).read()

wordcloud = WordCloud().generate(text)
print(wordcloud)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation='bicubic')
plt.axis('off')
plt.show()