'''

Coding Exercise - Python: Design a Stack (with Linked List)
Question :Construct Stack (using Linked List)

(you can do it with either SLL or DLL. Here let's try to do it with SLL)

Implement a Stack:

1.Using an Array

2.with a Stack class using a Linked list

One should be able to add to the stack and remove from the stack following the LIFO property.

Note-

Remove - after removing , return the value of the removed node
'''

# using a Singly Linked List
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add_to_stack(self, value):
        new_node = Node(value)

        if self.first is None:
            self.first = new_node
            self.last = new_node

        else:
            new_node.next = self.first
            self.first = new_node

        self.size += 1
        return self.size

    def remove_from_stack(self):

        if self.size == 0:
            return None

        temp = self.first
        self.first = self.first.next
        temp.next = None

        self.size -= 1

        if self.first is None:
            self.last = None

        return temp.value

    # get top value
    def peek_from_stack(self):
        if self.size == 0:
            return None

        return self.first.value

    # check if empty
    def is_empty(self):
        if self.size == 0:
            return True
        return False

# test
# print helper
def print_stack(first):
    current = first
    while current:
        print(current.value, end="->")
        current = current.next
    print("None")



stack = Stack()
stack.add_to_stack(5) # bottom
stack.add_to_stack(6)
stack.add_to_stack(10) # top

print_stack(stack.first)
print(stack.first.value)
# first = top

stack.remove_from_stack()
print_stack(stack.first)

# peek
peek = stack.peek_from_stack()
print(peek)

# empty check
print(stack.is_empty())