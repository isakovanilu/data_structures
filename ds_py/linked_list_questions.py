# remove duplicates in list
from linked_lists import LinkedList

def remove_duplicates(ll):
    if ll.head is None:
        return
    
    current_node = ll.head
    prev_node = None
    
    while current_node:
        runner = current_node
        while runner.next:
            if runner.next.value == current_node.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        prev_node = current_node
        current_node = current_node.next
 
    ll.tail = prev_node
    return ll.head


# lc q75
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = None
        current = head
        while current:
            next_node = current.next
            current.next = new_list
            new_list = current
            current = next_node
        return new_list
