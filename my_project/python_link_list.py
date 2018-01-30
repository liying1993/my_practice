class ListNode:
    def __init__(self, data):
        "constructor to initiate this object"
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
        return

    def has_value(self, value):
        "method to compare the value with the node data"
        if self.data == value:
            return True
        else:
            return False

# node1 = ListNode(15)
# node2 = ListNode(8.2)
# node3 = ListNode("Berlin")

class SingleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        self.head = None
        self.tail = None
        return

    def add_list_item(self, item):
        "add an item ad the end of the list"
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item
        return

    def list_length(self):
        "return the number of list items"
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        "search the linked list for the node that has this value"

        #define current_node
        current_node = self.head

        # define position
        node_id = 1

        # define list of results
        results = []

        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            #jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def search_value_result(self, key):
        current_node = self.head
        while current_node is not None:
            dd = current_node.data.keys()
            try:
                if current_node.data[key]:
                    global result
                    result = current_node.data[key]
                    return result
                else:
                    pass
            except Exception:
                pass
            current_node = current_node.next

    def remove_list_item_by_id(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    return
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1

class ListNode1:
    def __init__(self, data):
        "constructor to initiate this object"
        # store data
        self.data = data
        # store reference (next item)
        self.next = None
        self.previous = None
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False

class DoubleLinkedList:
    def __init__(self):
        "constructor to initiate this object"
        self.head = None
        self.tail = None
        return

    def list_length(self):
        "return the number of list items"
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output_list(self):
        "output the list (the value of the Node,actually)"
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    def unordered_search(self, value):
        "search the linked list for the node that has this value"
        current_node = self.head
        node_id = 1
        results = []
        while current_node is not None:
            if current_node.has_value(value):
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def add_list_item(self,item):
        "add an item at the end of the list"
        if isinstance(item, ListNode1):
            if self.head is None:
                self.head = item
                item.previous = None
                item.next = None
                self.tail = item
            else:
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
            return

    def remove_list_item_by_id(self, item_id):
        "remove the list item with the item_id"
        current_id = 1
        current_node = self.head
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            if current_id == item_id:
                if previous_node is not None:
                    previous_node.next = next_node
                    if next_node is not None:
                        next_node.previous = previous_node
                else:
                    self.head = next_node
                    if next_node is not None:
                        next_node.previous = None
                return
            current_node = next_node
            current_id = current_id + 1
        return

# create four single nodes
# node1 = ListNode(15)
# node2 = ListNode(8.2)
# item3 = "Berlin"
# node4 = ListNode(15)
# track = SingleLinkedList()
# print("track length: %i" % track.list_length())
# for current_item in [node1, node2, item3, node4]:
#     track.add_list_item(current_item)
#     print("track length: %i" % track.list_length())
#     track.output_list()
#
# node1 = ListNode1(15)
# node2 = ListNode1(8.2)
# node3 = ListNode1("Berlin")
# node4 = ListNode1(15)
# track = DoubleLinkedList()
# print("track length: %i" % track.list_length())
# for current_node in [node1, node2, node3, node4]:
#     track.add_list_item(current_node)
#     print("track length: %i" % track.list_length())
#     track.output_list()
# results = track.unordered_search(15)
# print(results)
# track.remove_list_item_by_id(4)
# track.output_list()

# from collections import deque
#
# class ListNode2:
#     def __init__(self, data):
#         self.data = data
# track = deque([node1,node2,node3])
# for item in track:
#     print(item.data)
# node4 = ListNode2(15)
# track.appendleft(node4)
