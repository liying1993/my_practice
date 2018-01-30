origin_list = []
min_list = []

def find_min_in_stack(info):
    '''
    首先判断是不是栈里的第一个元素，如果是就把该位置的下标放进另外一个栈，
    然后继续往里面输入元素，输入的元素先跟已有的最小值进行比较，如果大于的话，不做操作，如果等于或者小于的话，就要将新插入得数的下标放进
    另一个栈
    当把栈里的元素移除的时候，顺带把他在另外一个栈里面的元素也移除
    :return: 
    '''

    if not len(origin_list):
        origin_list.append(info)
        min_list.append(0)
    else:
        origin_list.append(info)
        index = min_list[-1]
        if origin_list[index] >= info:
            min_list.append(origin_list.index(info))
    return

def remove_min_num():
    if min_list[-1] == origin_list.index(origin_list[-1]):
        origin_list.pop()
        min_list.pop()
    else:
        origin_list.pop()

