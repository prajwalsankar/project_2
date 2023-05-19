"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
def pattern(n):
    p= 1
    for i in range(n):
        for j in range(i+1):
            print(p,end = " ")
        p+=1
        print()
#pattern(5)
"""
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
def pattern(n):
    for i in range(n):
        p=1
        for j in range(i+1):
            print(p,end = " ")
            p+=1
        print()
#pattern(5)
"""
  1 2 3 4 5 
    1 2 3 4 
      1 2 3 
        1 2 
          1 
"""
def pattern(n):
    for i in range(n):
        p=1
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(n-i):
            print(p,end = " ")
            p+=1
        print()
#pattern(5)
"""
          1 
        1 2 3 
      1 2 3 4 5 
    1 2 3 4 5 6 7 
  1 2 3 4 5 6 7 8 9 
"""
def pattern(n):
    for i in range(n):
        p=1
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print(p,end = " ")
            p+=1
        for j in range(i + 1):
            print(p, end=" ")
            p+=1
        print()
#pattern(5)

"""
5 
5 4 
5 4 3 
5 4 3 2 
5 4 3 2 1 
"""
def pattern_decrementing_column(n):
    for i in range(n):
        p= 5
        for j in range(i+1):
            print(p,end = " ")
            p-=1
        print()
#pattern_decrementing_column(5)
"""IMP
  5 4 3 2 1 
    4 3 2 1 
      3 2 1 
        2 1 
          1 
"""
def pattern_decrementing_column(n):
    k=n
    for i in range(n):
        p= k
        for j in range(i+1):
            print(" ",end = " ")
        for j in range(n-i):
            print(p,end = " ")
            p-=1
        k-=1
        print()
#pattern_decrementing_column(5)
"""
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 
"""
def hill_with_changing_columns(n):
    for i in range(n):
        p=1
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print(p,end=" ")
            p+=1
        for j in range(i+1):
            print(p,end=" ")
            p-=1
        print()
#hill_with_changing_columns(5)
"""
Floyd Triangle
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
"""
def floyed_triangle(n):
    p=1
    for i in range(n):
        for j in range(i+1):
            print(p,end=" ")
            p+=1
        print()
floyed_triangle(5)