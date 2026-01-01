"""Exercise 24: Count Occurrences⭐
```
Given: numbers = [1, 2, 3, 2, 4, 2, 5]

Ask user for a number to search.
Count how many times it appears in the list.
DON'T use .count() method - use a loop!

Example:
Search for: 2
The number 2 appears 3 times"""

numbers = [1, 2, 3, 2, 4, 2, 5]
search = int(input("Enter your number: "))
count = 0
for num in numbers:
    if num == search:
        count = count + 1

print(f"The number {search} appears {count} times")
