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
    return ll

ll = LinkedList()

ll.prepend(1)
ll.append(2)
ll.append(2)
ll.append(3)
ll.append(3)
ll.append(4)
ll.append(4)
ll.append(4)
print(ll)
ll = remove_duplicates(ll)
print(ll)