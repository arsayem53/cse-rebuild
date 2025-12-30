"""
Ask user for a number (n).
Print all EVEN numbers from 1 to n.

Example input: 10
Output: 2 4 6 8 10

Hint: Use for loop with range() and if statement to check even numbers

"""

num = int(input("Input:"))
for i in range(1,num+1):
    if i%2 == 0:
        print(f"{i}")
