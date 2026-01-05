"""  Example:
    arr = [10, 20, 30, 40]
    Result: [40, 30, 20, 10]"""

def reverese(numbers, reveresed):
     x = 0
     for i in range(len(numbers)-1, -1, -1):
          reveresed[x] = numbers[i]
          x+=1           
     print(f"\nReversed sucsessfully!")
     return reveresed

numbers = [10, 20, 30, 40]
reveresed = [0,0,0,0]
print(f"Initial array")
for i in range(len(numbers)):
     print(f"{i}th position's value : {numbers[i]} ")
reverese(numbers, reveresed)
print(f"\nReveresed array")
for i in range(len(reveresed)):
     print(f"{i}th position's value : {reveresed[i]} ")
     


