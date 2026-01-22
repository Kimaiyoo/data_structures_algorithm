# stack implementation with arrays
class Stack:
    def __init__(self):
        self.stack = []

    def add_to_stack(self, item):
        self.stack.append(item)

    def remove_from_stack(self):
        self.stack.pop()

    def peek_from_stack(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


# test

stack_2 = Stack()
stack_2.add_to_stack(5)
stack_2.add_to_stack(6)
# print stack
print(stack_2.stack)
# peek
print(stack_2.peek_from_stack())
# empty check
print(stack_2.is_empty())
# check size
print(stack_2.size())
#pop
stack_2.remove_from_stack()

print(stack_2.stack)
print(stack_2.is_empty())


