#Write a program that takes string input from the user and
#filters out all the consonants from the strings and
#print all respective ascii values in a list format.
sentence=str(input("Enter the sentence:"))#prajwal sankar
#consonents=" "
response=[]
vowels=('a','e','i','o','u')
for i in sentence:
#for i in range(0,len(sentence)):
    if i not in vowels:
        response.append(ord(i))
print(response)

