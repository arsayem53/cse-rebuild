"""Create a program that:
1. Creates an empty dictionary called 'contact'
2. Asks user for: name, phone, email, city
3. Stores these in the dictionary
4. Prints all contact details in a clean format like:

===== CONTACT DETAILS =====
Name: Alex
Phone: 1234567890
Email: alex@example.com
City: New York
"""
student = {
    "name" : " X ",
    "phone" : " 01581489810",
    "email" : "s@gmail.com",
    "city"  : "dhaka"

}
print("Enter name, phone, email, city: ")
print(student.values())

for key, values in student:
    print(f"{key} : {values}")

