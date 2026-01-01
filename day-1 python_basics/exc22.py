"""Exercise 22: Sum of List (Manual)
```
Given: numbers = [5, 12, 8, 3, 20]

Calculate the sum WITHOUT using sum() function.
Use a loop to add each number.

Print: "Sum: 48"
"""
numbers = [5, 12, 8, 3, 20]
long = len(numbers)
sum = 0
for i in range(long):
    sum = sum + numbers[i]
print(f"Sum: {sum}")
