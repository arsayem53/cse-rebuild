"""Example:
    arr = [10, 20, 30, 40, 50]
    delete_from_position(arr, 2)
    Result: [10, 20, 40, 50]"""

def delete_at_position(numbers, position):
     for i in range(position, len(numbers) - 1):
        numbers[i] = numbers[i + 1]
     numbers[len(numbers)-1] = None
     print(f"Number in {position}th position deleted sucsessfully in !")
     return numbers

numbers = [10, 20, 30, 40, 50]

position = int(input("Which position: "))

delete_at_position(numbers, position)
for i in range(len(numbers)):
     print(f"{i}th position's value : {numbers[i]} ")
     


