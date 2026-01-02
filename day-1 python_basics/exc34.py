"""Start with: student = {"name": "Alice", "age": 20, "grade": "B"}

Ask user which field to update (name, age, or grade).
Ask for new value.
Update the dictionary and print it.

Example:
Update which field? age
Enter new value: 21
Updated: {'name': 'Alice', 'age': 21, 'grade': 'B'}

Hint: Use student[field] = new_value
"""
student = {"name": "Alice", "age": 20, "grade": "B"}

field  = input("Which field to update: ")
l_field = field.lower()
fvalue = input("Enter new value:")

if l_field in student:
    student[l_field] = fvalue

print(student)