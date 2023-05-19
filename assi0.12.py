#WAP to find profit and loss from cp and sp
cp=int(input("Enter the cost price(CP):"))
sp=int(input("Enter the selling price(SP):"))
p=sp-cp
if p>0:
    print("Profit =",p)
elif p<0:
    print("Loss =",p)
elif p==0:
    print("no profit or no loss")
