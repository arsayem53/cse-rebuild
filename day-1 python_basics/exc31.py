"""Exercise 31: First and Last Character ⭐⭐
```
Ask user for a string.
Create a new string where:
- If length < 2: return empty string
- Otherwise: return first character + last character

Example:
Enter a string: Python
Result: Pn

Enter a string: Hello
Result: Ho

Enter a string: A
Result: (empty)

Hint: Check length first, then use indexing
"""
initial = input("Enter your string: ")
result = ""

if len(initial) < 2:
    result = " "
else:
    result = initial[0]+initial[-1]
print(f"Result: {result}")
