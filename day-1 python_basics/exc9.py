"""
Ask user: "How many numbers to add?"
Then ask them to enter that many numbers, one by one.
Print the total sum.

Example:
How many numbers? 3
Enter number: 10
Enter number: 20
Enter number: 5
Total sum: 35

Hint: Use a for loop and keep adding to a sum variable

"""
num = int(input("How many numbers to add?"))
sum = 0
for i in range(num):
    num1 = int(input("Enter number: "))
    sum = sum + num1

print(f"Total sum: {sum}")
