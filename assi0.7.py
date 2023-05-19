#WAP to accept the height of a peron in centimeter
height=int(input("Enter the height of a person in centimeters:"))
if height<150:
    print("DWARF")
elif 165>height>=150:
    print("AVERAGE HEIGHT")
elif height>165:
    print("TALL")
