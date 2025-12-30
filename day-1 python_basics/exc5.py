score = int(input("Enter your score: "))
if 0 <= score <= 100  :
        if 90 <= score <= 100:
            print(f"A")
        elif 80 <= score <= 89:
            print(f"B")
        elif 70 <= score <= 79:
            print(f"C")
        elif 60 <= score <= 69:
            print(f"D")
        elif score < 60:
            print(f"F")
else: 
     print(f"Invalid Score")