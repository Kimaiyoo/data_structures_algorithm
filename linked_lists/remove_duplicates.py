'''
delete duplicates - You are given the head of a Sorted Singly Linked list.
Write a function that will take the given head as input, delete all nodes that have a value that is already the value of
another node so that each value appears 1 time only and return the linked list, which is still to be a sorted linked list.
'''
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

    def remove_dupes(self, head):
        current = head

        while current and current.next:
            if current.val == current.next.val:
                #skip duplicates
                current.next = current.next.next
            else:
                current = current.next

        return head

# tests
# define a singly linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end= "->")
        current = current.next

    print("none")

# create linked list: 1 -> 1 -> 2 -> 3 -> 3
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

processed_heads= node1.remove_dupes(node1)
print_list(node1)

# expected output
# 1 -> 2 -> 3 -> none

