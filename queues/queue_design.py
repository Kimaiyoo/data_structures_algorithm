#from linked_lists.remove_duplicates import print_list

# using singly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class QueueLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)

        if self.size == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node


        self.size += 1
        return self.size

    def dequeue(self):
        if self.size == 0:
            return None

        temp = self.first
        self.first = self.first.next
        temp.next = None

        self.size -= 1

        if self.first == 0:
            self.first = None

        return temp.value

def print_queue(first):
    current = first
    while current:
        print(current.value, end="->")
        current = current.next
    print("None")

queue = QueueLinkedList()
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(10)

print_queue(queue.first)
queue.dequeue()
print_queue(queue.first)
print(queue.first.value)
