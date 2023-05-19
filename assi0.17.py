#WAP to check whether a triangle is equilateral,Isosceles or scalene
#let us assume the lenghts of sides of the triangle is a,b,c
a=int(input("Enter the length of a:"))
b=int(input("Enter the length of side b:"))
c=int(input("Enter the length of side c:"))
if a==b==c:
    print("The triangle is Equilateral Triangle:")
elif a==b or a==c or a==b or b==c:
    print("The triangle is Isosceles Triangle:")
elif a!=b!=c:
    print("The triangle is Scalene Triangle:")

