#WAP to find the largest of three numbers
x=int(input("Enter the value of 1st number"))
y=int(input("Enter the value of 2nd number"))
z=int(input("Enter the value of 3rd number"))
if x>y>z:
    print("x is largest")
elif x>y<z:
    print("x is largest")
elif x<y<z:
    print("z is largest")
elif x>y<z:
    print("z is largest")
elif y>x>z:
    print("y is largest")
elif y>z>x:
    print("y is largest")

    
