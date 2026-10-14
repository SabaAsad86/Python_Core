                              #CALL FUNCTION                                      
def greet():
    print("Hello Python")

greet()

print()

                               #ASSIGN PARAMETERS
def add(a, b):
    print(a + b)

add(5, 3)

print()

                               #LOCAL/GLOBAL VARIABLES
x = 10  # Global variable

def show():
    y = 5  # Local variable
    print(x)
    print(y)

show()