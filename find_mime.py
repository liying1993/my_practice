import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_resource = []
to_be_classify = []
# print(n)
# print(q)
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    input_mime = input().split()
    mime_resource.append(input_mime)
    # [for i in mime_resource]
lower_resource = [[i[0].lower(), i[1]] for i in mime_resource]
# print(mime_resource)
dict_mime_resource = dict(lower_resource)
# print(dict_mime_resource.keys())
for i in range(q):
    fname = input()  # One file name per line.
    to_be_classify.append(fname)
# print(to_be_classify)
for i in to_be_classify:
    if i.find(".") == -1 or (i[i.rfind(".")+1:]).lower() not in dict_mime_resource.keys():
       print("UNKNOWN")
    else:
        # print(i.rfind(".")+1)
        start = i.rfind(".")+1
        result = i[start:].lower()
        print(dict_mime_resource[result])
        # print(i[start:].lower())