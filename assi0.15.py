#WAP to read roll no,name,marks of three subjects and calculate the total,percentage and division
roll=int(input("Enter roll number:"))
name=str(input("Enter name:"))
maths=int(input("Enter marks in maths:"))
phy=int(input("Enter marks in physics:"))
chem=int(input("Enter marks in chemistry:"))
total=maths+phy+chem
print("total=",total)
percentage=float((total/300)*100)
print("percentage=",percentage)
if percentage>=60:
    print("Division is First")
elif 48<=percentage<60:
    print("Division is Second")
if 36<=percentage<48:
    print("Division is Pass")
elif percentage<36:
    print("Division is Fail")
    
