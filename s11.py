#.Write a program to find the sum of all the numbers which are divisible by 4.
#X = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
#Expected Output:
#Given input : [450, 540, 1256, 2506, 15342, 32424, 20018, 56300]
#Elements which are divisible by 4 : [540, 1256, 32424, 56300]
#Sum of elements which are divisible by 4:90520

x = [450, 540, 1256, 2506, 15342, 32424, 20018,56300]
y=[] #place holder to store all the numbers divisible by 4
total=0 #to store sum
for n in x:
    if n%4==0:
        y.append(n)
        total=total+n
print(f"Given Input:{x}")
print(f"Elements which are divisible by 4:{y}")
print(f"sum of elements which are divisible by 4:{total}")

