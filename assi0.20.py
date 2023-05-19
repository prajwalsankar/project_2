#WAP to accept grades and declare the equivalent description
"""grade=str(input("Enter the grade among ('E','V','G','A','F'):"))
if grade=="E":
    print("Excellent")
elif grade=="V":
    print("Very Good")
elif grade=="G":
    print("Good")
elif grade=="A":
    print("Average")
elif grade=="F":
    print("Fail")
"""
gd={"E":"Excellent","V":"Very good","G":"Good","A":"Average","F":"Fail"}
i=str(input("Enter the grade among ('E','V','G','A','F'):"))
if i in gd:
    print(gd[i])
else:
    print("please check the grade you have entered")
