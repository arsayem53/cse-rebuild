"""Create a function is_prime(number) that:
- Takes a number
- Returns True if prime, False if not
- Prime = only divisible by 1 and itself

Logic:
- Numbers < 2 are not prime
- Check if number is divisible by any number from 2 to number-1
- If divisible by ANY number, it's not prime

Test:
print(is_prime(7))   # True
print(is_prime(10))  # False
print(is_prime(2))   # True
print(is_prime(1))   # False

Hint: Use a for loop with range(2, number) and % operator"""

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

number = int(input("Enter the number: "))

if is_prime(number):
    print("Prime")
else: 
    print("Not prime")