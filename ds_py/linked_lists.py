# information about LinkedList in python and its implementation
# a linkedlis is a ds that conatins a sequence of elements, where each element pointing to the next element in the sequence
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 1

    def append(self, value):
        # given a value
        new_value = Node(value)
        if self.head == None:
            self.head = new_value
            return
        # add next value
# TODO add append, insert, delete

new_linked_list = LinkedList()
print(new_linked_list.length)
