# Arrays

Arrays are collections of elements stored in contiguous memory locations and
are accessed using indices. They allow constant-time access but can be costly
to modify when inserting or deleting elements.

In Python, arrays are typically implemented using lists.

---

## Time & Space Complexity

| Operation                | Time Complexity |
|--------------------------|-----------------|
| Access by index          | O(1)            |
| Search                   | O(n)            |
| Insert / Delete (middle) | O(n)            |
| Insert (end)             | O(1) amortized  |

---

## Common Array Patterns

### 1. Two Pointers
Used when traversing an array from both ends to reduce time complexity.

**Key idea:**
- Maintain two indices
- Move them based on conditions

**Example problems:**
- Sorted Squares
- Reverse Array

---

### 2. In-Place Array Manipulation
Used when modifying the array without extra space.

**Key idea:**
- Carefully update indices
- Avoid overwriting needed values

**Example problems:**
- Rotate Array
- Move Zeroes

---

## Problems Implemented

| Problem        | Pattern               | Notes                                        |
|----------------|-----------------------|----------------------------------------------|
| Sorted Squares | Two pointers          | Uses left/right comparison on a sorted array |
| Rotate Array   | In-place manipulation | Rotates array without using extra space      |

---

## Common Pitfalls

- Off-by-one errors
- Overwriting values before using them
- Using extra space when not required
- Forgetting edge cases (empty array, k > length)

---

## Notes

- Arrays favor fast access over flexibility
- Many array problems can be optimized using pointer techniques
