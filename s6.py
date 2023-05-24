#6.	Take two input strings of the same length
#and check if all the characters from string1 are available in string2 or not
#if yes print True otherwise print False. 
s1=input("enter the first string:") #TAM
s2=input("enter the second string:")#MAT
output=[]
if len(s1)==len(s2):
    #pass
    for ch in s1:
        if ch in s2:
            output.append(True)
        else:
            output.append(False)
    print(output)

else:
    print(false)
if all(output):
    print(True)
else:
    print(False)
