class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    # insert value
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            else:
                if current.right:
                    current = current.right

                else :
                    current.right = Node(value)
                    return

    # find a value
    def find(self, value):
        current = self.root
        while current:
            if value == current.value:
                return current
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    # remove value
    def remove(self, value):
        self.root = self._remove(self.root, value)

    def _remove(self, node, value):
        if not node:
            return None

        if value < node.value:
            node.left = self._remove(node.left, value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
            # Case 1: no child
            if not node.left and not node.right:
                return None

            # Case 2: one child
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            # Case 3: two children
            successor = self._min_value(node.right)
            node.value = successor.value
            node.right = self._remove(node.right, successor.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left:
            current = current.left
        return current


# test
bst = BinarySearchTree()
values= [10, 5, 15, 2, 7, 12, 20]
for val in values:
    bst.insert(val)

print(values)

print(bst.root.value)
print(bst.root.left.left.value)

# Find
print("Find 7:", bst.find(7).value if bst.find(7) else False)
print("Find 1:", bst.find(1).value if bst.find(1) else False)

bst.remove(12)
print(values)

print("Find 12:", bst.find(12).value if bst.find(12) else False)
