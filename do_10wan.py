import numpy as np
from itertools import *
from operator import *
from collections import deque

aa = "00100101"
index = 0

one_str = ""
for i, v in enumerate(aa):
    if (i+1) != len(aa) and aa[i] == aa[i + 1]:
        index += 1
    else:
        index += 1
        if aa[i] == '1':
            one = aa[i+1-index:i+1]
            one_str = one_str+" 0 "+ "0"*len(one)
            # list_one.append(aa[i+1-index:i+1])
        else:
            two = aa[i+1-index:i+1]
            one_str = one_str+" 00 "+ "0"*len(two)
            # list_zero.append(aa[i+1-index:i+1])
        index = 0
one_str = one_str.lstrip()
print(one_str)

# import sys
# import math
#
# # Auto-generated code below aims at helping you parse
# # the standard input according to the problem statement.
# 
# message = input()
# origin_str = ""
# origin_list = []
# index = 0
# one_str = ""
# # Write an action using print
# # To debug: print("Debug messages...", file=sys.stderr)
# # print(message)
# for msg in message:
#     msg_binary = bin(ord(msg))[2:]
#     if len(msg_binary) == 6:
#         msg_binary = "0"+msg_binary
#     # print(msg_binary)
#     origin_list.append(msg_binary)
#     origin_str = "".join(origin_list)
# # print(origin_str)
#
# for i, v in enumerate(origin_str):
#     if (i+1) != len(origin_str) and origin_str[i] == origin_str[i + 1]:
#         index += 1
#     else:
#         index += 1
#         if origin_str[i] == '1':
#             one = origin_str[i+1-index:i+1]
#             one_str = one_str+" 0 "+ "0"*len(one)
#             # list_one.append(aa[i+1-index:i+1])
#         else:
#             two = origin_str[i+1-index:i+1]
#             one_str = one_str+" 00 "+ "0"*len(two)
#             # list_zero.append(aa[i+1-index:i+1])
#         index = 0
# one_str = one_str.lstrip()
# print(one_str)
