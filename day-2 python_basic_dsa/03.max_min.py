"""arr = [45, 12, 78, 23, 67, 9]
find_max(arr)  # 78
find_min(arr)  # 9"""

def big(numbers):
    high = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > high:
          high = numbers[i]
    return high
        
def smul(numbers):
    low = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] < low:
          low = numbers[i]
    return low

numbers = [45, 12, 78, 23, 67, 9]

"""maximum = big(numbers)
minimum = smul(numbers)"""

print(f"Max : {big(numbers)}")
print(f"Min : {smul(numbers)}")
     