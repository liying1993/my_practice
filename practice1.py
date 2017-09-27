


#找到一串数中最接近0的数字，这些数中有正数和负数，如果有一个正数和负数同时接近0，则选择正数，如果没有给数，就打印0

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526
# print(type(temps))
# print(temps)
input_list = temps.split(" ")
# print(type(input_list))
# print(input_list)
if len(temps) == 0:
    # print("==============")
    print(0)
else:
    result = min([abs(int(i))for i in input_list])
    # print(result)
    if str(result) in input_list:
        print(result)
    else:
        # print("==")
        print(-result)
# Write an action using print