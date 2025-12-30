"""Create a function factorial(n) that:
- Takes a number n
- Returns n! (n factorial)
- Factorial: n! = n × (n-1) × (n-2) × ... × 1
- Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

Test:
print(factorial(5))  # 120
print(factorial(3))  # 6
print(factorial(1))  # 1
print(factorial(0))  # 1 (special case)

Hint: Use a for loop and multiply
"""
def factorial(n):
    result = 1
    for i in range(1, n+1):  # Must include n!
        result = result * i
    return result


number = int(input("Enter your number: "))
print(f"{factorial(number)}")
