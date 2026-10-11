             #INT DATATYPE          
age = 20
print("Age:", age)
print(type(age))

print()
            #FLOAT DATATYPE
price = 250.50
print("Price:", price)
print(type(price))

print()
            #COMPLEX DATATYPE

a = 2 + 3j
print(type(a))

print()
            #STR DATATYPE

name = "Saba"
print("Student Name:", name)
print("Name Length:", len(name))
print("First Letter:", name[0])

print()
            #LIST DATATYPE

students = ["Saba", "Haram", "Ayman"]

print("Original List:", students)

students.append("Laiba")
print("After Adding:", students)

students[0] = "Saba"
print("After Updating:", students)

students.remove("Ayman")
print("After Removing:", students)

print("First Student:", students[0])
print("Total Students:", len(students))

            #TUPLE DATATYPE

marks = (80, 75, 90, 85)

print("All Marks:", marks)
print("First Mark:", marks[0])
print("Total Subjects:", len(marks))

print()
             #SET DATATYPE

numbers = {10, 20, 30, 20, 10}

print("Original Set:", numbers)

numbers.add(40)
print("After Adding:", numbers)

numbers.discard(20)
print("After Removing 20:", numbers)

print()
            #SET ELEMENTS
            
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)

print()
             #DICTIONARY
student = {
    "name": "Saba",
    "age": 20,
    "marks": 85
}

print("Student Details:", student)
print("Name:", student["name"])
print("Age:", student["age"])

student.pop("age")
print("After Removing Age:", student)

print()
              #RANGE FUNCTION

for i in range(1, 6):
    print(i)
    
print()  

for i in range(5):
    print(i) 
    
print()    
              #ARRAY DATATYPE

import array

numbers = array.array('i', [10, 20, 30, 40])

print("Array:", numbers)
print("First Element:", numbers[0])

numbers.append(50)
print("After Adding:", numbers)

numbers[1] = 25
print("After Updating:", numbers)