"""Exercise 20: Shopping List Manager
```
Create an empty list called shopping_list.

Ask user: "How many items to add?"
Then let them add that many items using append().
Print the final list.

Example:
How many items? 3
Enter item: milk
Enter item: bread
Enter item: eggs
Shopping list: ['milk', 'bread', 'eggs']
"""


shopping_list = []
item = int(input("How many item to add: "))
for i in range(item):
    new_item = input("")
    shopping_list.append(new_item)

print(f"Shopping list:{shopping_list}")
