#WAP to calculate electricity bill
customer_id=int(input("Enter the customer Id:"))
name=str(input("Enter name of the customer:"))
units=int(input("Enter the units consumed by the User:"))
charge=float()
bill=float(units*charge)
if units<=199:
    charge=1.20
    bill=units*charge
    print("Bill:",bill)
elif 200<=units<400:
    charge=1.50
    bill=units*charge
    print("Bill:",bill)
elif 400<=units<600:
    charge=1.80
    bill=units*charge
    print("Bill:",bill)
elif units>=600:
    charge=2.00
    bill=units*charge
    print("Bill:",bill)
