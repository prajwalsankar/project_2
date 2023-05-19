#WAP to find area of various geometrical shapes
w=str(input("Enter the shape Circle(C),Rectangle(R),Triangle(T):"))
#Area of circle
if w=="C":
    r=float(input("Enter radius:"))
    area_c=float(3.14*r*r)
    print("area of circle:",area_c)
#area of rectangle
elif w=="R":
    length=float(input("Enter length:"))
    width=float(input("Enter width:"))
    area_r=float(length*width)
    print("area of rectangle:",area_r)
#area of triangle
elif w=="T":
    base=float(input("Enter base:"))
    height=float(input("Enter height:"))
    area_t=float(0.5*base*height)
    print("area of triangle :",area_t)
