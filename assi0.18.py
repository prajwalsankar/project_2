#WAP to check whether the triangle is formed with the given angles
#let the angles of the triangle are a,b,c
a=float(input("Enter the 1st angle:"))
b=float(input("Enter the 2nd angle:"))
c=float(input("Enter the 3rd angle:"))
if a+b+c==180:
    print("Triangle can be formed with these angles",a,b,c)
else:
    print("Triangle can be not formed with these angles",a,b,c)
