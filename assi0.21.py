#WAP to read any date and show the name of the day in a week
day={1:"monday",2:"tuesday",3:"wednesday",4:"thursday",5:"friday",6:"saturday",7:"sunday"}
i=int(input("Enter the day number: "))
if i in day:
    print(day[i])
else:
    print("Out of range of days in a week")
