""" Example:
    arr = [5, 2, 5, 8, 5, 1]
    find_all_occurrences(arr, 5)
    Result: [0, 2, 4]
    """

def find_all_occurrences(numbers, target):
    result = [0] * len(numbers)
    count = 0

    for i in range(len(numbers)):
        if numbers[i] == target:
            result[count] = i
            count += 1

    final = [0] * count
    for i in range(count):
        final[i] = result[i]

    return final


numbers = [5, 2, 5, 8, 5, 1]

target = int(input("Enter the target number: "))

print("Initial array")
for i in range(len(numbers)):
    print(f"{i}th position's value : {numbers[i]} ")

indices = find_all_occurrences(numbers, target)

print("\nNumber found at indices")
for i in range(len(indices)):
    print(indices[i])


