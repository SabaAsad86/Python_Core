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

                #BOOL DATATYPE

marks = 75
passing_marks = 50

is_pass = marks >= passing_marks

print("Marks:", marks)
print("Passed:", is_pass)
print("Is marks less than 50?", marks < 50)
print(type(is_pass))

print()
                  #NONE DATATYPE

result = None

print("Result:", result)
print(type(result))

result = 90
print("Updated Result:", result)

print()
                     #BYTES DATATYPE

data = bytes([65, 66, 67])

print("Bytes:", data)
print("First Byte:", data[0])
print("Text:", data.decode())

print()

                   #TYPE CASTING

# Type Casting using 4 Functions

a = 10

b = int(5.8)
c = float(a)
d = str(a)
e = bool(a)

print("Integer:", b)
print("Float:", c)
print("String:", d)
print("Boolean:", e)

print(type(b))
print(type(c))
print(type(d))
print(type(e))      