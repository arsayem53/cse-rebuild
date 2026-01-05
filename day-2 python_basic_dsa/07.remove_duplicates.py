"""  Remove duplicate elements, keep first occurrence.
    
    Example:
    arr = [1, 2, 2, 3, 1, 4, 3]
    Result: [1, 2, 3, 4]"""

def duplicates(numbers):
    result = [0] * len(numbers)
    count = 0

    for i in range(len(numbers)):
        current_val = numbers[i]
        already_exists = False

        for j in range(count):
            if result[j] == current_val:
                already_exists = True
                break
        
        if not already_exists:
            result[count] = current_val
            count += 1

    final = [0] * count
    for i in range(count):
        final[i] = result[i]
        
    return final

numbers = [5, 2, 5, 8, 5, 1]


print("Initial array")
for i in range(len(numbers)):
    print(f"{i}th position's value : {numbers[i]} ")

final_arr = duplicates(numbers)

print("\nAfter removing duplicat values: ")
for i in range(len(final_arr)):
     print(f"{i}th position's value : {final_arr[i]} ")