"""Exercise 21: Remove Item
```
Start with: fruits = ["apple", "banana", "cherry", "date"]

Ask user which fruit to remove.
If fruit exists, remove it and print updated list.
If fruit doesn't exist, print "Fruit not found".

Example:
Remove which fruit? banana
Updated list: ['apple', 'cherry', 'date']
"""


fruits = ["apple", "banana", "cherry", "date"]
cut = input("Which item to remove: ")
if cut in fruits:
    fruits.remove(cut)

print(fruits)
