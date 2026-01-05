def insert_at_position(numbers, position,x):
     numbers.append(None)
     for i in range(len(numbers)-1, position, -1):
          numbers[i] = numbers[i-1]
     
     numbers[position] = x
     print(f"Number {x} inserted sucsessfully in {position}th position!")
     return numbers
numbers = [10, 20, 30]

position = int(input("Which position: "))
target = int(input("Which number: "))

insert_at_position(numbers, position, target)
for i in range(len(numbers)):
     print(f"{i}th position's value : {numbers[i]} ")
     


