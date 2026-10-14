              #if CONDITION

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
    
print()

                        #if elif

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
print()

 
             #IF , ELIF, ELSE
marks = 75

if marks >= 80:
    print("Grade A")

elif marks >= 60:
    print("Grade B")

else:
    print("Grade C")
    
print()

            #NESTED if
marks = 75

if marks >= 50:
    print("Pass")

    if marks >= 80:
        print("Grade A")
    else:
        print("Grade B")

else:
    print("Fail")
    
print()
            
