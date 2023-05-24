#Write a program to reverse the given input string.
s=input("Enter the string")
print(f"Input:{s}")
output=""
for i in range(len(s)-1,-1,-1):
    output=output+s[i]
print(f"Output:{output}")
rev = (str(reversed(s)))
print(str(rev))