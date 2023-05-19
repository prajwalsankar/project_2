#hill_upward_pattern
"""
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
"""
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end=" ")
        for j in range(i):
            print("*",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        print()
pattern(5)

print("-----------------------------------------------")
"""
 * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
"""
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(n-i-1):
            print("*",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()
pattern(5)