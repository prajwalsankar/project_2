#WAP to find whether the given number is a leap year or not
#let us assume the year denoted as y
y=int(input("Enter the Year:"))
if y%4==0:
    if y%400 ==0:
        print("the given year is a leap year")
    else:
        print("the given year is not a leap year")
