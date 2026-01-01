"""Exercise 30: Remove Spaces ⭐
```
Ask user for a sentence.
Create a new string with ALL spaces removed.
DON'T use .replace() - use a loop!

Example:
Enter a sentence: Hello World Python
Result: HelloWorldPython

Hint: Loop through each character, only add to result if it's not a space
"""
initial = input("Enter your string: ")
words = " "
for char in initial:
    if char != " ":
        words+=char
print(words)