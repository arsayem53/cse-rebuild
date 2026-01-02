"""
Create a dictionary: grades = {}

Ask user how many students to add.
For each student, ask for name and grade.
Store in dictionary.
Print the complete grade book.

Example:
How many students? 2
Enter name: Alice
Enter grade: 85
Enter name: Bob
Enter grade: 92
Grade book: {'Alice': 85, 'Bob': 92}
"""

grades = {}

num=int(input("Enter how many sudent do you want to add:"))

for i in range(num):
    name =   input("Enter Name:")
    grad =   input("Enter Grade:")

    grades[name] = grad

for key, values in grades.items():
    print(f"{key} : {values}")

print(grades) #Another type of print added 
