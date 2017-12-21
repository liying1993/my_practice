import os
# FONT_PATH = os.environ.get("FONT_PATH", os.path.join(os.path.dirname(__file__),
#                                                      "DroidSansMono.ttf"))

# frequencies = sorted(frequencies.items(), key=item1, reverse=True)

# frequencies = frequencies[:self.max_words]

# noo = mask == 255#先做前面的赋值操作，再做后面的比较操作

# >>> inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
# >>> getcount = itemgetter(1)
# >>> list(map(getcount, inventory))
# [3, 2, 5, 1]
# >>> sorted(inventory, key=getcount)
# [('orange', 1), ('banana', 2), ('apple', 3), ('pear', 5)]

# x = [1, 2, 3]
# y = [4, 5, 6]
# z = [7, 8, 9]
# xyz = zip(x, y, z)
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# flags = (re.UNICODE if sys.version < '3' and type(text) is unicode
#                  else 0)

# words = [word[:-2] if word.lower().endswith("'s") else word
#                  for word in words]


# raise ValueError("WordCloud has not been calculated, call generate"
#                              " first.")

# bb = dict.fromkeys(aa,True)#将list转换成字典

# def open_txt(filename):
#     with open(filename, 'r+') as f:
#         line = f.readlines()
#         while line:
#             yield line
#             line = f.readline()
# for text in open_txt('constitution.txt'):
#     print(text)//读大文件减少读入时间

# with open('constitution.txt', 'r') as f:
#     line = f.readlines()
#     print(line)

# packetData = ''.join((c if 32 <= ord(c) <= 126 else '.' )for c in s)

# alist1 = alist[:]

# ("la","cd")[True]  ["la","cd"][True]

# sys.exc_info() 可以显示 Exception 的信息，返回一个 (type, value, traceback) 组成的三元组，可以与 try/catch 块一起使用：

# sys.exit(arg=0) 用于退出 Python。0 或者 None 表示正常退出，其他值表示异常

# new = {}
# for (key, value) in data:
#     group = new.setdefault(key, []) # key might exist already
#     group.append( value )

# new = defaultdict(list)
# for (key, value) in data:
#     new[key].append( value ) # all keys have a default already