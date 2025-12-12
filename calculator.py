def add(x,y):
    sum= x + y
    print(sum)
    print("This is the sum function.")
   
    print("This is after Return")

#This is the subtraction..

def sub(x,y):
    subtract= x - 2*y
    print(subtract)



def div(x,y):
    if(y==0):
        print("This can't be divided")
    else:
        divide= x / y
        print(divide)
def mul(x,y):
    multiply= x * y
    print(multiply)



x=int(input("Enter first number:"))
y=int(input("Enter scond number:"))
z=int(input("press 1:add , 2:subtract , 3:divide , 4:multiply = "))


if z == 1:
    add(x,y)
elif z == 2:
    sub(x,y)
elif z == 3:
    div(x,y)
elif z == 4:
    mul(x,y)
else:
    print("unknown operator.")

