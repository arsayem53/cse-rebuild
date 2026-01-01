"""Exercise 25: Reverse a List (Manual) ⭐⭐
```
Given: numbers = [1, 2, 3, 4, 5]

Create a NEW list with elements in reverse order.
DON'T use .reverse() or [::-1] - use a loop!

Print: [5, 4, 3, 2, 1]

Hint: Loop through original list backwards, or
      loop forward and insert at beginning of new list
"""
numbers = [1, 2, 3, 4, 5]
rev_num = []

for i in range(len(numbers)):
    current = numbers.pop()
    rev_num.append(current)

print(f"Reverse: {rev_num}")