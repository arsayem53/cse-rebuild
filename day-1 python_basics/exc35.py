"""Ask user for a string.
Count how many times EACH character appears.
Store in a dictionary where:
- Key = character
- Value = count

Print the dictionary.

Example:
Enter string: hello
{'h': 1, 'e': 1, 'l': 2, 'o': 1}

Hint: Loop through string, check if char in dict, increment or initialize
"""
Val = input("Enter a string:")

spere = {}

for char in Val:
    if char in spere:
        spere[char] += 1
    else:
        spere[char] = 1

print(spere)