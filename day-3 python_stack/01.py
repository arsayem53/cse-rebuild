def push(stack):
    number = int(input("How many inputs do you want to push: "))

    if len(stack) + number > MAX_SIZE:
        print("Stack Overflow!")
        return

    for i in range(number):
        element = int(input("Enter your element: "))
        stack.append(element)


def pop(stack, removed):
    number = int(input("How many items do you want to pop: "))

    if number > len(stack):
        print("Stack underflow! Not enough elements.")
        return

    for i in range(number):
        top = stack.pop()
        removed.append(top)

def peek(stack):
    if stack:
        return stack[-1]
    else:
        print("The stack is empty")
        return None


def is_empty(stack):
    if stack:
        return True
    else:
        return False

def is_full(stack):
    count = 0
    for i in range(len(stack)):
        count += 1
    return count

def display(stack):
    for i in range(len(stack)):
        print(f"{i}th value is {stack[i]}")

stack = []
removed = []
MAX_SIZE = 5
while True:
    print(f"""\n\nWelcome to basic stack operation.
      What can I do for you:
      1. Push
      2. Pop
      3. Peek
      4. Is empty
      5. Is full
      6. Display
      7. Exit
      """)
    options = int(input("Enter what do you want (1-7): "))

    if options == 1:
       push(stack)

    elif options == 2:    
       pop(stack, removed)
       
       print("After poping new stack is: ")
       for i in range(len(stack)):
           print(f"{i}th value is {stack[i]}")

       print("After poping new removed is: ")
       for i in range(len(removed)):
           print(f"{i}th value is {removed[i]}")
    
    elif options == 3:        
      top_element = peek(stack)
      print(f"Top elemnt is {top_element}")

    elif options == 4:        
        result = is_empty(stack)
        if result == True:
           print("Its not empty")
        else:
           print("Its empty")

    elif options == 5:        
       result = is_full(stack)
       if result == 5:
           print("Its full")
       else:
           print("Its not full")

    elif options == 6:        
       display(stack)

    elif options == 7:        
       break
