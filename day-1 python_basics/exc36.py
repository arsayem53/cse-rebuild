"""Start with:
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"}
}

Ask user for a student name.
If found, print their age and grade.
If not found, print "Student not found".

Example:
Search name: Bob
Age: 21, Grade: B

Hint: Check if name in students, then access students[name]["age"]
"""
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 21, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"}
}

text = input("Enter student name: ")

if text in students:
    print(students[text])
else:
    print("Student not found")
    