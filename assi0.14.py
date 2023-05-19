#WAP to find the eligibility of admission
maths=int(input("Enter marks in maths:"))
phy=int(input("Enter marks in physics:"))
chem=int(input("Enter marks in chemistry:"))
MPC=maths+phy+chem
MP=maths+phy
if maths>=65 and phy>=55 and chem>=50:
    if MPC>=180 or MP>=140:
        print("eligible")
    else:
        print("not eligible")
    
