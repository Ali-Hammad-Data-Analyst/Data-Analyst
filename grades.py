marks=int(input("Enter your Marks /100:"))
if marks >= 90:
    print("congratulation you have got 'A' grade")
elif  80<=marks<90:
    print("You have got 'B' grade")
elif 70<=marks<80:
    print("You have got 'C' grade")
elif 60<=marks<70:
    print("You have got 'D' grade")
elif 50<=marks<60:
    print("You have got 'E' grade")
elif marks<50:
    print("Unfortunately you have got 'F' grade")
else:
    print("Unknown number")
