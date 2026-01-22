from remove_duplicates import print_list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_tail(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self

def add_2_numbers(l1, l2):
        # Time Complexity Explanation:
        # The while loop runs at most 'max(n, m)' times where 'n' and 'm' are the lengths of l1 and l2 respectively.
        # Thus, the time complexity is O(max(n, m)).

        carry_forward = 0
        results = LinkedList()
        while l1 or l2 or carry_forward:
            l1_value = l1.value if l1 else 0
            l2_value = l2.value if l2 else 0
            total = (l1_value + l2_value + carry_forward)
            node_value_in_result = total % 10
            results.add_at_tail(node_value_in_result)
            carry_forward = total // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return results

    # The time complexity: O(max(m,n))

# tests
def build_linked_list(values):
    ll = LinkedList()
    for val in values:
        ll.add_at_tail(val)
    return ll.head


def test_add_2_numbers(l1_vals, l2_vals, expected_vals):
    l1_head = build_linked_list(l1_vals)
    l2_head = build_linked_list(l2_vals)

    result_ll =         add_2_numbers(l1_head, l2_head)

    # Convert result linked list to Python list for easy comparison
    result_list = []
    current = result_ll.head
    while current:
        result_list.append(current.value)
        current = current.next

    print("Input 1:", l1_vals)
    print("Input 2:", l2_vals)
    print("Output :", result_list)
    print("Expected:", expected_vals)
    print("Test Pass:", result_list == expected_vals)
    print("------------")

# Example: 342 + 465 = 807
test_add_2_numbers([2, 4, 3], [5, 6, 4], [7, 0, 8])

# Another example: 99 + 1 = 100
test_add_2_numbers([9, 9], [1], [0, 0, 1])


