#WAP to show the XY coordinating point in quadrant
x=float(input("Enter the x-coordinate:"))
y=float(input("Enter the y-coordinate:"))
print("XY coordinates are",(x,y))
if x>=0 and y>=0:
    print((x,y),"1st Quadrant")
elif x<=0 and y>=0:
    print((x,y),"2nd Quadrant")
elif x<=0 and y<=0:
    print((x,y),"3rd Quadrant")
elif x>=0 and y<=0:
    print((x,y),"4th Quadrant")    
