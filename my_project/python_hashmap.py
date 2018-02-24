import operator
from my_project.python_link_list import SingleLinkedList, ListNode

class MyHashMap:
    def __init__(self, length):
        #HashMap的默认长度是16
        self.length = length
        self.entry_array = [None]*self.length

    def calculate_index(self, key):
        '''
        解决一个问题，如果生成的index不在数组的长度范围内怎么解决？
        java的hashmap计算得到的索引值总是位于table数组的索引之内
        :param value: 
        :return: 
        '''
        index = operator.and_(id(key), (self.length-1))
        return index

    def insert_hashmap(self, item):
        '''
        先计算要插进hashmap的值的index，也就是计算插到数组的对应位置
        然后生成一个节点实例
        然后判断一下数组中的这个位置是不是已经有存在的链表了，如果没有就新创建一个，并且把刚刚新建的节点加到链表里面，并且把新创建的链表放进数组里面
        如果有就插到链表的头部，这里为了方便调用刚写好的链表类，先假设是把节点放在链表的尾部
        :param value: 
        :return: 
        '''
        index = self.calculate_index(item.keys())
        node = ListNode(item)
        if not self.entry_array[index]:
            singleList = SingleLinkedList()
            singleList.add_list_item(node)
            self.entry_array[index] = singleList
        else:
            pos_singleList = self.entry_array[index]
            pos_singleList.add_list_item(node)
        return self.entry_array

    def get_ele(self, key):
        """
        hashmap的get方法根据key来查找value的时候，首先把输入的key做一次hash映射，得到对应的index
        然后找到列表对应的链表，然后遍历链表，得到对应的value
        :param key: 
        :return: 
        """
        # index = self.calculate_index(key)
        index = 8
        sigle_list = self.entry_array[index]
        value = sigle_list.search_value_result(key)
        return value


if __name__ == '__main__':
    myhashmap = MyHashMap(16)
    first_data = {"lala":"banana"}
    # index = myhashmap.calculate_index(first_data)
    result = myhashmap.insert_hashmap(first_data)
    # print(result)
    myhashmap.get_ele("lala")
