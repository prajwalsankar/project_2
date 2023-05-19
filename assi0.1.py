#WAP to accept two integers and check whether they are equal or not.
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a==b:
    print("a and b values are equal")
else:
    print("a nd b values are not equal")


def factorial(number):
    facto = 1
    for i in range(2, number + 1):
        facto = facto * i
    print(facto)


factorial(5)