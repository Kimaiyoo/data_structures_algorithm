# Hash Tables

Hash tables (also called hash maps or dictionaries) store data as key–value pairs
and allow fast lookups, insertions and deletions.

In Python, hash tables are implemented using `dict` and `set`.

---

## Why Use Hash Tables?

- Fast lookups by key
- Efficient frequency counting
- Useful for detecting duplicates
- Helpful for mapping relationships between values

---

## Time & Space Complexity

| Operation | Average Case |
|-----------|--------------|
| Insert    | O(1)         |
| Lookup    | O(1)         |
| Delete    | O(1)         |

> Worst-case time complexity can degrade to O(n) due to collisions,
but this is rare in practice.

---

## Common Hash Table Patterns

### 1. Complement Lookup
Used when finding two values that satisfy a condition.

**Example:**
- Two Sum
- Target difference problems

**Pattern:**
- Store previously seen values in a hash map
- Check if the complement exists

---

### 2. Frequency Counting
Used when counting occurrences of elements.(use where order does not matter)

**Example:**
- Anagrams
- Character frequency problems

**Pattern:**
- Use a hash map to count elements

---

### 3. One-to-One Mapping
Used when checking if two structures follow the same pattern.

**Example:**
- Isomorphic Strings

**Pattern:**
- Maintain two hash maps to ensure consistency

---

## Problems Implemented

| Problem            | Key Concept           |
|--------------------|-----------------------|
| Two Sum            | Complement lookup     |
| Isomorphic Strings | Bidirectional mapping |

---

## Common Pitfalls

- Forgetting to handle duplicate keys
- Overwriting values unintentionally
- Using hash tables when ordering is required
- Returning incorrect results when no valid solution exists

---

## Notes

- Hash tables trade space for speed
- They are a foundational tool in many DSA problems
- Choosing the right key is critical
- If order matters -> compare positions
- If order doesn’t matter -> compare frequencies