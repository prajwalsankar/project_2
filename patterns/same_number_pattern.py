"""
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
"""
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("1",end =" ")
        print()
        
#pattern(5)

print("------------------------------------------------")
"""
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
"""
def pattern(n):
    p = 1
    for i in range(n):
        #p = 1
        for j in range(i+1):
            print(p,end =" ")
        p += 1
        print()


pattern(5)

"""
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
"""
def pattern(n):
    p= 5
    for i in range(n):
        for j in range(i+1):
            print(p,end = " ")
        p-=1
        print()
#pattern(5)
"""
0 
2 2 
4 4 4 
6 6 6 6 
8 8 8 8 8 
"""
def pattern(n):
    p= 0
    for i in range(n):
        for j in range(i+1):
            print(p,end = " ")
        p+=2
        print()
#pattern(5)
"""
1 
2 2 
1 1 1 
2 2 2 2 
1 1 1 1 1 
"""
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            if (i%2==0):
                print(1,end = " ")
            else:
                print(2,end = " ")
        print()
#pattern(5)

