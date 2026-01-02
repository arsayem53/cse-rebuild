"""PROGRAM 1: CALCULATOR (30 min)
Requirements:
Build a calculator that:

Shows a menu with operations (+, -, *, /, exit)
Asks user for two numbers
Performs the operation
Shows the result
Loops back to menu until user chooses to exit

Features to Include:

Menu-driven interface
All 4 basic operations
Input validation (handle division by zero)
Clean, user-friendly output
Loop until user quits"""

def addition(first, second):
     result = first + second
     return result

def subtraction(first, second):
     result = first - second
     return result

def multiplication(first, second):
     result = first * second
     return result

def division(first, second):
     if second == 0:
          print("Error: Cannot divide by zero!")
     else:
          result = first / second
          return result


while True:
     print("""=== CALCULATOR ===
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit"""
)

     option = int(input("Choose operation (1-5): "))
     if option == 5:
        print("Goodbye!")
        break 
     first = int(input("Enter your first number :"))
     second = int(input("Enter your second number: "))

     if   option == 1:
          operator = "+"
          result = addition(first, second)

     elif option == 2:
           operator = "-"
           result = subtraction(first, second)

     elif option == 3:
          operator = "*"
          result = multiplication(first, second)

     elif option == 4:
          operator = "/"
          result = division(first, second)
          if result == None:
               continue



     print(f"Result => {first} {operator} {second} = {result}")