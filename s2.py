#The given string contains both lowercase and uppercase letters in random order and combines all lowercase letters and displays in output.
#Example:  #input :   AmaZOn
	    #output: man
'''
#solution 1

s=str(input("Enter the letter"))
c=str()
for i in s:
    if 'a'<=i<='z':
        c=c+i
print(c)
'''
'''
#solution 2
word=input("Enter the word:")
output=" "
for ch in word:
    if 'a'<=ch<='z':
        output=output+ch
print(f"the combination of lower letters is:{output} from :{word}")
'''

#solution 3
word=input("Enter the word:")
output=" "
for ch in word:
    if ord(ch)>=97 and ord(ch)<=122:
        output=output+ch
print(f"the combination of lower letters is:{output} from :{word}")



