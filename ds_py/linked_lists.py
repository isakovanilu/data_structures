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
        self.length = 0
        
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        # given a value
        new_value = Node(value)
        if self.head == None:
            self.head = new_value
            self.tail = new_value
        else:
            self.tail.next = new_value
            self.tail = new_value
        self.length += 1
        # add next value
# TODO add append, insert, delete

new_linked_list = LinkedList()
new_linked_list.append(50)
new_linked_list.append(10)
new_linked_list.append(60)
print('head', new_linked_list)
print('tail', new_linked_list)

