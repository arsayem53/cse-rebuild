"""
Create a function find_max(a, b, c) that:
- Takes three numbers
- Returns the largest one
- DON'T use max() built-in function - use if statements!

Test:
print(find_max(10, 5, 8))   # 10
print(find_max(3, 15, 7))   # 15
print(find_max(4, 2, 20))   # 20

"""
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(find_max(a, b, c))


