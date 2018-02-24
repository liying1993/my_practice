import operator

'''判断2的乘方
用2的乘方本身和它减一的结果进行按位与运算，也就是N&N-1，运算结果是0
所以2的乘方都符合一个规律，即N&N-1等于0
'''

'''
找出漏掉的数，一个无序数组里有99个不重复整数，范围从1到100，唯独缺少一个整数。找到这个缺失的整数
用1到100的整数和，减去漏掉一个数的整数和，结果就是最后漏掉的数
一个无序数组里有若干个正整数，范围从1到100，其中99个整数都出现了偶数次，只有一个整数出现了奇数次（比如1,1,2,2,3,3,4,5,5），如何找到这个出现奇数次的整数？
可以用正常的数组和不正常的数组进行异或运算，剩下的就是结果
'''

'''
辗转相除法，求出两个整数的最大公约数
1、使用欧几里得算法：两个正整数a和b（a>b），它们的最大公约数等于a除以b的余数c和b之间的最大公约数
2、更相减损术：两个正整数a和b（a>b），它们的最大公约数等于a-b的差值c和较小数b的最大公约数
3、结合前两个方法，在更相减损术的基础上使用移位运算
'''

'''
1、有一座高度是10级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶，要求用程序来求出一共有多少种走法？
动态规划：是一种分阶段求解决策问题的数学思想。
最后一步可以分成走两步或者走一步
F（10） = F（8）+F（9）依次类推
F（n） = F(n-1)+F(n-2)

2、01背包问题：有一个窃贼在偷窃一家商店时返现有n件商品，第i件物品价值为vi元，重量为wi，假设vi和wi都为整数，他希望带走的东西越值钱越好，但它的背包中最多能放下W磅的东西，W为一整数
他应该带走哪几样东西
'''


def max_common_division(a, b):
    while True:
        c = a % b
        if c == 0:
            return b
        else:
            a, b = b, c


def max_common_division1(a, b):
    while True:
        c = a - b
        if b == c:
            return b
        else:
            a, b = b, c


def max_common_dicision2(a, b):
    if (a % 2 == 0) and (b % 2 == 0):
        a = operator.lshift(a, 1)
        b = operator.lshift(b, 1)
    elif (a % 2 == 0) and (b % 2 != 0):
        a = operator.lshift(a, 1)
    elif (a % 2 != 0) and (b % 2 == 0):
        b = operator.lshift(b, 1)
    elif (a % 2 != 0) and (b % 2 != 0):
        a,b = b, a-b
    if a == b:
        return a
    else:
        max_common_dicision2(a, b)

def get_best_way(n):
    if n<1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return get_best_way(n-1)+get_best_way(n-2)

def get_best_way1(n):
    cache = {}
    if n<1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    if n in cache:
        return cache[n]
    else:
        value = get_best_way1(n-1)+get_best_way1(n-2)
        cache[n] = value
        return value

def get_best_way2(n):
    if n<1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    a = 1
    b = 2
    temp = 0
    for i in range(3,n):
        temp = a+b
        a = b
        b = temp
    return temp


