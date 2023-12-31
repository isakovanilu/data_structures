
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is successfully created"
    
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted into the list")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                    
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    def reverse(self):
        if self.head is Node:
            print("There is no any element to reverse.")   
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                         
    def reverseTraversalDLL(self):
        if self.head is Node:
            print("There is no any element to traversal.")
            
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    def searchDLL(self, nodeValue):
        if self.head is None:
            print("There is no value to search")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node do not exist in this list"
     
    def deleteNode(self, location):
        if self.head is None:
            print("There is not element to delete")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    
            else:
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
                
                
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
doublyLL.insertNode(0,0)
doublyLL.insertNode(2,1)
doublyLL.insertNode(6,2)
print([node.value for node in doublyLL])
# doublyLL.reverse()
doublyLL.deleteNode(2)
print([node.value for node in doublyLL])
# doublyLL.reverseTraversalDLL()
# print(doublyLL.searchDLL(6))    


        
            
        
        
        
