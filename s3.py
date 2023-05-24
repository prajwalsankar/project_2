#3.combine all the characters from the given sentence
#which the respective indices are divisible by 5 and ignore the space in output.
#Example : #input : Winners are not those who never fail but those who never quit
                #output:  Wreerlert

#solution 1
'''
s=str(input("Enter the sentence:"))
k=""
for i in range(0,len(s)):
    if i%5 ==0:
        if s[i]!=" ":
            k=k+s[i]
print(k)
'''
#solution 2
sentence=input("Enter sentence:")
print(type(sentence))
res=""
for i in range(0,len(sentence)):
    if i%5==0:
        if sentence[i]!=' ':
            res=res+sentence[i]
print(res)

#for counting total number of indices divisible by 5

    
sentence=input("Enter sentence:")
print(type(sentence))
res=int()
for i in range(0,len(sentence)):
    if i%5==0:
        if sentence[i]!=' ':
            res=res+1
print(res)

