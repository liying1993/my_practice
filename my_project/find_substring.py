def lengthOfLongestSubstring(s):
    start = maxLength = 0
    usedChar = {}
    for i, v in enumerate(s):
        if v in usedChar and start <= usedChar[v]:
            start = usedChar[v] + 1
        else:
            maxLength = max(maxLength, i - start +1)
        usedChar[v] = i
    return maxLength


if __name__ == '__main__':
    result = lengthOfLongestSubstring("pwwsdsdp")
    print(result)

# trace_list = []
# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     trace = SingleLinkedList()
#
#     for i in range(len(s)):
#         node = ListNode(s[i])
#         if i+1 == len(s):
#             node.flag = True
#         trace.add_list_item(node)
#     # print(len(trace_list))
#     count = max(trace_list)
#     return count
#
#
# class ListNode:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.flag = False
#         return
#
#
# class SingleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_list_item(self, item):
#         if not isinstance(item, ListNode):
#             item = ListNode(item)
#         if self.head is None:
#             self.head = item
#         else:
#             is_repeated_value = self.search_value_result(item)
#             if not is_repeated_value:
#                 if self.tail == None:
#                     self.head.next = item
#                     self.tail = item
#                 else:
#                     self.tail.next = item
#                     self.tail = self.tail.next
#             else:
#                 trace_list.append(self.list_length())
#                 self.head = item
#                 self.tail = None
#                 if item.flag == True:
#                     trace_list.append(1)
#
#     def search_value_result(self, key):
#         current_node = self.head
#         while current_node is not None:
#             if current_node.data == key.data:
#                 return True
#             current_node = current_node.next
#         return False
#
#     def list_length(self):
#         count = 0
#         current_node = self.head
#         while current_node is not None:
#             count = count + 1
#             current_node = current_node.next
#         return count
#
# if __name__ == '__main__':
#
#     result = lengthOfLongestSubstring("bbbbb")
#     print(result)