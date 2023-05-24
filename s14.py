#WAP print all duplicate elements from the given list
#X = [10, 25, 28, 10, 78, 26, 25, 35, 28]
#output: [10, 25, 28]
x=[10, 25, 28, 10, 78, 26, 25, 35, 28]
print(f"Given Input:{x}")
y=[]
z=[]
for i in x:
    if i not in y:
        y.append(i)
    else:
        z.append(i)
print(f"Duplicates:{z}")
print(f"Uniques:{y}")

    
