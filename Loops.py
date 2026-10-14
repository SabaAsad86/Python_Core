 
                         #for loop
marks = [80, 35, 60, 25, 90]

for mark in marks:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")
        
print()

                         #while loop
marks = 50

while marks <= 100:
    print(marks)
    marks += 10
                         #BREAK STATEMENT
for i in range(1, 6):
    if i == 3:
        break
    print(i)
    
print()
                         #CONTINUE STATEMENT

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print()
