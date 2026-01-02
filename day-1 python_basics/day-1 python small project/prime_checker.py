"""## **PROGRAM 2: PRIME CHECKER (30 min)**

### **Requirements:**
Build a program that:
1. Asks user for a number
2. Checks if it's prime
3. Shows the result
4. **Asks if they want to check another number**
5. Repeats until user says "no"

### **Features to Include:**
- Use a **function** `is_prime(number)` that returns True/False
- Handle edge cases (numbers < 2 are not prime)
- Clear output messages
- Loop to check multiple numbers
- Input validation

### **Example Run:**
```
Enter a number: 7
7 is a PRIME number!

Check another number? (yes/no): yes

Enter a number: 10
10 is NOT a prime number.

Check another number? (yes/no): yes

Enter a number: 1
1 is NOT a prime number.

Check another number? (yes/no): no
Goodbye!
Hints:

Reuse your is_prime() function from Exercise 18! (You already wrote this!)
Use a while loop controlled by user's yes/no response
Prime logic: check if divisible by any number from 2 to (number-1)
Numbers less than 2 are not prime
2 is the only even prime number

Prime Function Reminder:
pythondef is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
```

---"""


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

while True:
    print("=== Prime number checker ===")
    number = int(input("Enter a number: "))
    result = is_prime(number)
    if result == True:
        print(f"{number} is a PRIME NUMBER")
    else:
        print(f"{number} is NOT A PRIME NUMBER")
    
    option = input("Check another number? (yes/no): ").lower()
    if option == 'yes':
        continue
    elif option == 'no':
        print("Goodbye!")
        break
    else:
        print("invalid input try again. Check another number? (yes/no): ")
