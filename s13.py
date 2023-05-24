# Write programs take a value from the input and display the output , how
#many times the value is repeated from the given list and print the
#message “NO ELEMENT FOUND” incase of no element present.
#X = [20, 19, 25, 17, 32, 17, 39, 17, 20]
#Note: The list.count() function should returns the number of occurrences,
# you should not use the function to implement this
v=int(input("Enter a value"))#17
x=[20, 19, 25, 17, 32, 17, 39, 17, 20]
print(f"Enter input:{x}")
count=0
if v in x:
    for e in x:
        if e == v:
            count=count+1
    print(f"The element {v} is repeated {count} time")
else:
    print(f"Element {v} is not found")
    
