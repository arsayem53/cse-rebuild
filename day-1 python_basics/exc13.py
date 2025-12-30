"""
Ask user for a number.
Print it in reverse.

Example input: 12345
Output: 54321

Hint: Use % to get last digit, then // to remove it
Example: 12345 % 10 = 5 (last digit)
         12345 // 10 = 1234 (remaining)

Use a while loop

"""

num = int(input("Enter a number: "))
original = num
reversed_num = 0
while num != 0:
    last = num % 10
    reversed_num = reversed_num * 10 + last
    num = num // 10
print(reversed_num)
    