"""## **PROGRAM 3: CHARACTER FREQUENCY COUNTER (30 min)**

### **Requirements:**
Build a program that:
1. Asks user for a text/sentence
2. Counts how many times EACH character appears
3. Displays the results in a clean format
4. **Ignores spaces** (optional: make this a user choice)
5. Shows characters in order of frequency (highest first)

### **Features to Include:**
- Use a **dictionary** to store character counts
- Option to ignore spaces or count them
- Sort results by frequency (most common first)
- Clean, readable output
- Handle both uppercase and lowercase (decide: case-sensitive or not?)

### **Example Run:**
```
Enter text: Hello World

Character Frequency Counter:
l: 3
o: 2
H: 1
e: 1
W: 1
r: 1
d: 1
(space): 1

Most common character: 'l' (appears 3 times)
```

### **Advanced Version (Optional):**
```
Enter text: Hello World
Count spaces? (yes/no): no
Case sensitive? (yes/no): no

Character Frequency Counter:
l: 3
o: 2
h: 1
e: 1
w: 1
r: 1
d: 1

Most common character: 'l' (appears 3 times)
Hints:

Reuse your character counting logic from Exercise 35!
Use dictionary: char_count = {}
Loop through string: for char in text:
To ignore spaces: if char != " ":
To sort by frequency: Convert dict to list, then sort

"""