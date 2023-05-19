#WAP to read temperature and state as
temp=float(input("Enter the temperature in centigrade:"))
if temp < 0:
    print("Freezing Weather")
elif 0<=temp<10:
    print("Very Cold Weather")
elif 10<=temp<20:
    print("Cold Weather")
elif 20<=temp<30:
    print("Normal in temp")
elif temp>=40:
    print("It is very Hot")
