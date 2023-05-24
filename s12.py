#Write a program print an output as a list
#which contains all indices of the elements which are divisible by 4.
# x = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
'''
x = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
y=[]#for number/element
z=[]#for indices
#to traverse the indices we can use range() function
for n in range(0,len(x)):
    if x[n]%4==0:
        y.append(x[n])
        z.append(n)
print(f"Given Input:{x}")
print(f"Elements which are divisible by 4:{y}")
print(f"Indices of elements which are divisible by 4:{z}")
'''

x = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
d={}
#to traverse the indices we can use range() function
for i in range(0,len(x)):
    if x[i]%4==0:
        d[i]=x[i]
print(f"given input:{x}")
print(f"Indice for the elements which are divisible by 4:{d}")

