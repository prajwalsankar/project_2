"""
          *
        * *
      * * *
    * * * *
  * * * * *
"""
def pattern(n):
    for i in range(n):
        for j in range(n-i):
            print(" ",end = " ")
        for j in range(i+1):
            print("*",end= " ")
        print()

pattern(5)

print("-----------------------------------------")
"""
 * * * * * 
    * * * * 
      * * * 
        * * 
          * +-
"""

def pattern_of_decreasing_rt_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(n-i):
            print("*",end=" ")
        print()

pattern_of_decreasing_rt_triangle(5)