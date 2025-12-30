#Multiplication Table
#Ask user for a number (n).
#Print the multiplication table from 1 to 10.

#Example input: 5
#Output:
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
...
#5 x 10 = 50

#Use a for loop with range()
    
num = int(input("Enter your number: "))
for i in range(1,11):
    print(f"{num}*{i} = {num*i}")
