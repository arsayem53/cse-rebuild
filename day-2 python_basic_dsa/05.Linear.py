numbers = [10, 20, 30, 40, 50]

target = int(input("Which number do you want to find: "))
position = -1
for i in range(len(numbers)):
    if  numbers[i] == target:
        position = i
        break
if position != -1:
    print(f"Found in {i}th position")
else:
        print(f"Not Found")

