def print_result(x, y):
    result = str(x) + " "+str(y)
    return result
'''
['00', '0.']
['0.0.0']
'''
# array_list = [['0', '0'], ['0', '.']]
# array_list = [['0', '.', '0', '.', '0']]
# result = ""
array_list = [['0'], ['0'], ['0'], ['0']]
#第几行表示y轴，第几列表示x轴
part_strs = []
for index, value in enumerate(array_list):
    cororinate_y = index#第几行
    out_length = len(array_list)#一共有几行
    for in_index, in_value in enumerate(value):
        cororinate_x = in_index
        in_length = len(value)#某一行一共有几列
        if array_list[cororinate_y][cororinate_x] == "0":
            part_strs.append(print_result(cororinate_x, cororinate_y))
            #所以在第cororinate_y行上查找有没有能量点，在第cororinate_x列上查找有没有最近的能量点
            #行上对应的长度是in_length，列上对应的长度是out_length
            #先在行上找的话，y轴的数就是一样的，再在列上找的话，x轴的数就是跟当前的x是一样的
            for i in range(in_length):
                delta_i = i+1
                # if cororinate_x+delta_i !=
                if cororinate_x+delta_i != in_length:
                    if array_list[cororinate_y][cororinate_x+delta_i] == "0":
                        part_strs.append(print_result(cororinate_x+delta_i, cororinate_y))
                        break
                else:
                    part_strs.append("-1 -1")
                    break
            for j in range(out_length):
                delta_j = j+1
                if (cororinate_y+delta_j) != out_length:
                    if array_list[cororinate_y+delta_j][cororinate_x] == "0":
                        part_strs.append(print_result(cororinate_x, cororinate_y+delta_j))
                        break
                else:
                    part_strs.append("-1 -1")
                    break
            print(part_strs)
            result = " ".join(part_strs)
            part_strs = []
            print(result)

        # right_index = 0
        # right_neignbors = False
        # down_neighbors = False
        # in_length = len(value)
        # if array_list[index][in_index] == "0":
        #     part_strs.append(print_result(index, in_index))
        #     if (in_index+1) != in_length:
        #         for i in range(in_length-1):
        #             if array_list[index][in_index+(i+1)] == "0":
        #                 right_index = in_index+(i+1)
        #                 right_neignbors = True
        #                 break
        #         print("has right neighbors")
        #     else:
        #         print("has no right neighbors")
        #     #判断当前节点有没有下面的邻居
        #     if (index+1) != out_length:
        #         for i in range(out_length-1):
        #             if array_list[index+(i+1)][in_index] == "0":
        #                 down_index = index + (i+1)
        #                 down_neighbors = True
        #                 break
        #         print("has down neighbors")
        #     else:
        #         print("has no down neighbors")
        #
        #     if right_neignbors:
        #         part_strs.append(print_result(index, right_index))
        #     else:
        #         part_strs.append("-1 -1")
        #
        #     if down_neighbors:
        #         down_index = index+1
        #         part_strs.append(print_result(down_index, index))
        #     else:
        #         part_strs.append("-1 -1")
        #     result = " ".join(part_strs)
        #     part_strs = []
        #     print(result)


            # print(array_list[index][in_index],-1,-1,array_list[index+1][in_index])
        # elif array_list[index + 1][in_index] == ".":
        #     print(array_list[index][in_index],array_list[index][in_index + 1],-1,-1)
        # elif array_list[index][in_index + 1] == "." or array_list[index + 1][in_index] == ".":
        #     print()
        # else:
        #     print(array_list[index][in_index],array_list[index][in_index + 1],array_list[index+1][in_index])
"""
先找到当前节点有没有右边的邻居，再找到当前节点有没有下面的邻居
"""