 #Your program should take input as a string and
 #display the total number vowels from the given string.
 #Assume the input contains the lower case letters. 
'''
#solution 1
s=str(input("Enter the string"))
c=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        c=c+1
        
print(c)
'''
'''
#solution 2

word=input("Enter the word")
counter=0
vowels="aeiou"
for ch in word:
    if ch in vowels:
        counter=counter+1
print(f"Total number of vowels:{counter} from the given: {word}")
'''
#counting each occurance of vowel
'''
word=input("Enter the word:")
word=word.lower()
d={}
vowels="aeiou"
for ch in word:
    if ch in vowels:
        if ch not in d:
            d[ch]=1  #Adding new key value pair{'i':1,'a':1}
        else:
            d[ch]=d[ch]+1
print(d)

'''
#counting each occurance of alphabet
word=input("Enter the word:")
word=word.lower()
d={}
for ch in word:
    if 'a'<=ch<='z':
        if ch not in d:
            d[ch]=1
        else:
            d[ch]=d[ch]+1
print(d)
