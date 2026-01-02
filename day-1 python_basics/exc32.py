"""Create an empty dictionary called student.
Ask user for:
- Name
- Age  
- Grade

Store these in the dictionary and print it.

Example:
Enter name: Alice
Enter age: 20
Enter grade: A
Student: {'name': 'Alice', 'age': 20, 'grade': 'A'}

"""

student = {
    "Name" : " ",
    "Age"  : " ",
    "Grade": " "
}

student["Name"] = input("Enter the name: ")
student["Age"] = input("Enter the Age: ")
student["Grade"] = input("Enter the Grade: ")

print(student)

