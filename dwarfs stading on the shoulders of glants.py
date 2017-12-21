# n = int(input())
# # influences = [input().split() for i in range(n)]
# influences = [['1', '2'], ['1', '3'], ['3', '4'], ['2', '4'], ['2', '5'], ['10', '11'], ['10', '1'], ['10', '3'],['11','8'],['8','9']]
#
# length = 0
# # Create a set containing all people names:
# people_left = set(x for inf in influences for x in inf)
# print(people_left)
#
# # In each iteration, discard all of the people that are not influenced by others:
# while (len(people_left) > 0):
#     people_left = set(inf[1] for inf in influences if inf[0] in people_left)
#     length += 1
#
# print(length)

# connection = {}
# connection = {1: [2, 3], 3: [4], 2: [4, 5], 10: [3, 1, 11], 11: [8], 8: [9]}
# def depth(num):
#     relation_depth = 0
#     if len(connection[num]) == 0:
#         return 0
#     for child in connection[num]:
#         relation_depth = max(relation_depth, 1+depth(child))
#     return relation_depth
#
# for item in connection:
#     # print(item)
#     temp = depth(item)

# from collections import deque
#
# data_list = []#存放的全是deque
# index = 0
# data_collection = [['1', '2'], ['1', '3'], ['3', '4'], ['2', '4'], ['2', '5'], ['10', '11'], ['10', '1'], ['10', '3'],['11','8'],['8','9']]
# for data in data_collection:
#
#     for i in data_list:
#         if i[0] == data[-1]:
#             index += 1
#             i.appendleft(data[0])
#         elif i[-1] == data[0]:
#             index += 1
#             i.append(data[1])
#     if not index:
#         q = deque()
#         q.append(data[0])
#         q.append(data[1])
#         data_list.append(q)
#     index = 0
# print(max([len(i) for i in data_list]))



# connection = {}
def letsCount(number):
    global connection
    max = 0
    get_array = connection.get(number, [])
    if len(get_array) == 0:
        return 0
    else:
        for item in get_array:
            temp = letsCount(item)
            if max < temp:
                max = temp
    return max + 1


# n = int(input())  # the number of relationships of influence
# for i in range(n):
#     # x: a relationship of influence between two people (x influences y)
#     x, y = [int(j) for j in input().split()]
#     connection.setdefault(x, []).append(y)
# print(connection)
connection = {10: [3, 11,1],1: [2, 3], 3: [4], 2: [4, 5], 11: [8], 8: [9], 9: [12]}
my_max = 0
for item in connection:
    # print(item)
    my_temp = letsCount(item)
    if my_max < my_temp:
        my_max = my_temp
print(my_max + 1)
