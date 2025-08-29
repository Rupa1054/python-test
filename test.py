
### 1. Add an integer and float. What is the result’s type?


a = 5      # integer
b = 3.2    # float
result = a + b
print(result)        # 8.2
print(type(result))  # <class 'float'>

### 2. Create a string and access its:

s = "Python"

print("First character:", s[0])     # P
print("Last character:", s[-1])     # n
print("Substring (2 to 5):", s[2:5])  # tho

### 3. Concatenate two strings and print the result.

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)   # Hello World

### 4. Define list. What is the difference between List and Tuple?

#List:Ordered, mutable (can change values), written with [].
#Tuple: Ordered, immutable (cannot change values), written with ().

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

### 5. Write a program to print a list in reverse order.

num = [1, 2, 3, 4, 5]
print("Reversed:", num[::-1])   # [5, 4, 3, 2, 1]

### 6. Create a tuple of 4 elements. Print the first and last element.

t = (10, 20, 30, 40)
print("First:", t[0])   # 10
print("Last:", t[-1])   # 40

### 7. Try changing a value in a tuple. What happens?

t = (1, 2, 3)
# t[0] = 100   # ❌ Error: 'tuple' object does not support item assignment

### 8. Create a dictionary of 3 students with their marks. Print the dictionary.

students = {"Ravi": 85, "Anita": 92, "Suresh": 78}
print(students)

### 9. Access the marks of one student using their name.

print("Anita's marks:", students["Anita"])  # 92

### 10. Update the marks of an existing student.

students["Ravi"] = 90
print(students)  # {'Ravi': 90, 'Anita': 92, 'Suresh': 78}


### 11. Can I access a key using a value in a dictionary?

#Directly ❌ No.
#But you can *loop* or use reverse lookup:

for name, marks in students.items():
    if marks == 92:
        print("Student with 92 marks:", name)


### 12. Can I have duplicate values and keys in a dictionary?

# Duplicate Keys ❌* → Last value will overwrite previous.

d = {"a": 1, "b": 2, "a": 3}
print(d)   # {'a': 3, 'b': 2} → last "a" kept


# Duplicate Values ✅* → Allowed.


d = {"x": 10, "y": 10, "z": 20}
print(d)   # {'x': 10, 'y': 10, 'z': 20}


### 13. Print all multiples of 17 using range. Numbers should start from -34 and end below 400.

for num in range(-34, 400, 17):
    print(num, end=" ")
