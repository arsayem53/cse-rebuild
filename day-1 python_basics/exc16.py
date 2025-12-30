"""
Create a function power(base, exponent) that:
- Takes two numbers
- Returns base raised to the power of exponent
- DON'T use ** operator - use a loop!

Example:
power(2, 3) should return 8 (2*2*2)
power(5, 2) should return 25 (5*5)
"""

def power(base, exponent):
    result = 1
    for i in range(exponent): 
        result = result * base
    return result 

base = int(input("Enter your base: "))
expo = int(input("Enter your exponent: "))
print(f"Total: {power(base, expo)}")