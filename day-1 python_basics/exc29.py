"""Exercise 29: Count Each Character⭐⭐
```
Ask user for a string.
Count how many times EACH unique character appears.
Print each character with its count.

Example:
Enter a string: hello
h: 1
e: 1
l: 2
o: 1

Hint: Loop through string, for each character count how many times it appears
"""

initial = input("Enter your string: ")
printed = ""

for char in initial:
    if char not in printed:
        count = 0
        for chars in initial:
            if char == chars:
                count += 1
        print(f"{char}: {count}")
        printed += char  