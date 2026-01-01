""""Exercise 27: Count Vowels
```
Ask user for a string.
Count how many vowels (a, e, i, o, u) it contains.
Case insensitive (count both 'A' and 'a').

Example:
Enter a string: Hello World
Vowels: 3

Hint: Create vowels = "aeiouAEIOU" and check if char in vowels
"""
initial = input("Enter your string: ")
vowel = "aeiouAEIOU"
count = 0
for char in initial:
    for chars in vowel:
        if char == chars:
            count += 1
print(f"Vowels: {count}")
