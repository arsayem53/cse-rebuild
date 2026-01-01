"""Exercise 23: Find Max & Min (Manual) ⭐
```
Ask user: "How many numbers?"
Let them enter that many numbers into a list.

Find and print BOTH maximum and minimum values.
DON'T use max() or min() functions - use loops and comparisons!

Example:
How many numbers? 5
Enter number: 23
Enter number: 5
Enter number: 89
Enter number: 12
Enter number: 67
Maximum: 89
Minimum: 5
"""
new = int(input("Enter how many number do you want: "))
numbers = []
for i in range(new):
    num = int(input("Enter your number:"))
    numbers.append(num)

max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
for num in numbers:
    if num < min_num:
        min_num = num
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")
