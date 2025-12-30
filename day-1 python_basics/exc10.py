"""
Ask user for a starting number.
Count down to 1, then print "Blast off!"

Example input: 5
Output:
5
4
3
2
1
Blast off!

Use a while loop
"""
num = int(input("Example input: "))
while num != 0:
    print(f"{num}")
    num=num-1
print("Blast off!")