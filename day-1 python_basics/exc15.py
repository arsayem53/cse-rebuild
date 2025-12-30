"""
Create a function rectangle_area(length, width) that:
- Takes length and width as parameters
- Returns the area

Then ask user for length and width, call the function, and print result.

Example:
Enter length: 5
Enter width: 3
Area: 15
"""

def area_clac(length, width):
    return length*width
leng = float(input("Enter length: "))
widt = float(input("Enter width: "))
area = area_clac(leng,widt)
print(f"Total area is: {area}")