#10.Write a program take two input strings of equal lengths
#and display the output with by representing same index value
#Example:  #input1:  MOTHER
                 #input2:  PYTHON
	    #output:  [ [M, P], [O, Y], [T, T], [H, H], [E, O], [R, N]]
'''
s1=input("Enter first string:")
s2=input("Enter second string:")
output=[]
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        t=[]
        t.append(s1[i])
        t.append(s2[i])
        output.append(t)
    print(output)
else:
    print("In valid Input")
    
'''

s1=input("Enter first string:")
s2=input("Enter second string:")
output=[]
if len(s1)==len(s2):
    for i in range(0,len(s1)):
        output.append([s1[i],s2[i]])
    print(output)
else:
    print("Invalid input")
