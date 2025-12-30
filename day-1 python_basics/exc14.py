"""
Create a function called is_positive(number) that:
- Takes a number as parameter
- Returns True if positive, False if negative or zero

Test it with:
print(is_positive(5))   # True
print(is_positive(-3))  # False
print(is_positive(0))   # False

"""
def is_positive(number):
    if number > 0:
        return True 
    else:
        return False 

number = int(input("Enter your number: "))        
if is_positive(number):
    print("True")
else:
    print("False")