#Write a program count each occurrence of a vowel from the given string
sentence=str(input("Enter the sentence"))
vowels=('a','e','i','o','u')
d={}
sentence=sentence.lower()
for i in sentence:
    if i in vowels:
        if i not in d:
            d[i]=1
        else:
            d[i]=d[i]+1
print(d)
