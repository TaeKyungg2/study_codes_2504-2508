# 2024-06-13 Cursor Chat Study Notes

## C++ Concepts and Q&A

---

### 1. Class vs Struct Member Initialization
- **Class and struct are almost the same in C++** (only difference: default access specifier).
- **In-class member initialization** (C++11+):
  - You can assign default values to member variables directly in the class/struct body, but only for simple assignments (not constructor calls).
  - Example:
    ```cpp
    struct Node {
        int data = 0; // OK
        bool color = true; // OK
    };
    ```
- **Constructor calls** for member variables must be done in the constructor's initializer list, not in the class/struct body.

---

### 2. Temporary Objects and Lifetime
- **Temporary objects** (e.g., `Node(NULL, false)`) are destroyed at the end of the full expression (the statement).
- **Pointers to temporaries** become dangling pointers after the statement.
- **Local variables** live until the end of their scope (function/block).
- **Member variables** live as long as the object exists.
- **C++ does not have a garbage collector**; memory management is manual or via smart pointers.

---

### 3. Getting the Median (Middle Value) of Three Values
- No built-in function, but easy to implement:
    ```cpp
    int median_of_three(int a, int b, int c) {
        return a + b + c - std::max({a, b, c}) - std::min({a, b, c});
    }
    ```

---

### 4. Ranking Values
- To get the rank (1 = largest, 2 = middle, 3 = smallest) of three values:
    ```cpp
    std::array<int, 3> get_ranks(int a, int b, int c) {
        std::array<int, 3> ranks;
        ranks[0] = 1 + (a < b) + (a < c);
        ranks[1] = 1 + (b < a) + (b < c);
        ranks[2] = 1 + (c < a) + (c < b);
        return ranks;
    }
    ```
- **Do not return a local C array** from a function (it will be destroyed). Use `std::array` for safety.

---

### 5. Common Errors and Fixes
- **Missing `#include <array>`**: Always include the header when using `std::array`.
- **Missing `std::` namespace**: Use `std::array`, not just `array`.
- **Return type mismatch**: Make sure your function returns the correct type.
- **Pointers to temporaries**: Never store the address of a temporary object.

---

### 6. Example: Node Rank Function
```cpp
#include <array>
struct Node { int data; };
std::array<int,3> median_of_three(Node a, Node b, Node c) {
    int rank_a = 1 + (a.data < b.data) + (a.data < c.data);
    int rank_b = 1 + (b.data < a.data) + (b.data < c.data);
    int rank_c = 1 + (c.data < a.data) + (c.data < b.data);
    return {rank_a, rank_b, rank_c};
}
```

---

### 7. General Advice
- Use `std::array` for fixed-size arrays in modern C++.
- Always manage memory carefully; C++ does not have a garbage collector.
- Understand object lifetimes to avoid undefined behavior.

---

## Topic: C++ Vector Sorting and Algorithm Practice

### Questions & Answers

#### 1. **How to sort a vector in C++?**
- Use `std::sort` from `<algorithm>`.
- Example:  
  ```cpp
  sort(v.begin(), v.end()); // Ascending order
  ```

#### 2. **How to sort a vector in descending order?**
- Use `std::sort` with `greater<int>()`:
  ```cpp
  sort(v.begin(), v.end(), greater<int>());
  ```

#### 3. **What does `greater<int>()` mean?**
- It is a function object (functor) from `<functional>`.
- Used as a comparator for sorting in descending order.
- Equivalent to a custom comparator that returns `a > b`.

#### 4. **What is the time complexity of `std::sort`?**
- O(n log n) for average and worst case.

#### 5. **C++ foreach grammar**
- Use range-based for loop:
  ```cpp
  for (auto x : container) { /* ... */ }
  ```
- For modifying elements:
  ```cpp
  for (auto& x : container) { /* ... */ }
  ```

---

### Code Context

You are working on a C++ program to distribute weights into trucks, trying to minimize the maximum load (P).  
You experimented with sorting, iterators, and loop constructs.

---

**End of Study Notes** 