from typing import Optional

class Node:
    def __init__(self, value):
        self.value = value
        self.next: Optional[Node]=None

def reverseLinkedList(head):
    #write code here

    prev = None
    current = head

    while current:
        nextNode = current.next   #save next
        current.next = prev       #reverse link
        prev = current            #move prev forward
        current = nextNode        #move current forward

    return prev

# tests
def printList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original list:")
printList(node1)

reversedHead = reverseLinkedList(node1)

print("Reversed list:")
printList(reversedHead)
