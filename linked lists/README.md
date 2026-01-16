# Linked Lists

A *linked list* is a linear data structure made up of **nodes**, where each node
stores a value and a reference to the next node.

Unlike arrays, linked lists are not stored contiguously in memory and must be
traversed sequentially.

---

## Why Use Linked Lists?

- Dynamic size (no fixed memory allocation)
- Efficient insertions and deletions
- No shifting of elements in memory
- Useful when frequent updates are required

---

## Time & Space Complexity

| Operation  | Complexity |
|-----------|------------|
| Traversal | O(n)       |
| Search    | O(n)       |
| Insert    | O(1)*      |
| Delete    | O(1)*      |

\* When the node position is already known.

---

## Types of Linked Lists

- **Singly Linked List** – each node points to the next node
- **Doubly Linked List** – nodes point to both previous and next
- **Circular Linked List** – tail connects back to the head

---

## Common Linked List Patterns

### 1. Traversal
Used to access or process each node.

**Examples:**
- Printing values
- Searching for a value
- Finding min/max

---

### 2. Pointer Rewiring
Used for insertion and deletion.

**Pattern:**
- Update `next` references carefully
- Handle edge cases (head insertion/deletion)

---

## Problems Implemented

| Problem             | Key Concept            |
|---------------------|------------------------|
| Reverse Linked List | Pointer manipulation  |
| Delete a Node       | Pointer rewiring      |
| Insert at Position | List traversal        |

---

## Notes

- No random access (must traverse from head)
- Requires careful pointer management
- Trades access speed for update efficiency
- Good for understanding low-level data structure behavior
