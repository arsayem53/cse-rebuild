"""Exercise 28: Check Palindrome ⭐
```
Ask user for a word.
Check if it's a palindrome (reads same forwards and backwards).
Case insensitive.

Example:
Enter a word: Racecar
Palindrome!

Enter a word: Python
Not a palindrome

Hint: Convert to lowercase, reverse it, compare
"""


initial = input("Enter your string: ")
reveresd = ""
for char in initial:
    reveresd = char + reveresd 

if initial == reveresd:
    print("Palindrom")
else: 
    print("Not a Palindrom")

    