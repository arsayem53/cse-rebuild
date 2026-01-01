"""Exercise 26: Reverse String (Manual)
```
Ask user for a string.
Print it in reverse.
DON'T use [::-1] or reversed() - use a loop!

Example:
Enter a string: Python
Reversed: nohtyP

Hint: Build a new string by prepending each character
"""
initial = input("Enter your string: ")
reveresd = ""
for char in initial:
    reveresd = char + reveresd 

print(f"Reveresed: {reveresd}")
