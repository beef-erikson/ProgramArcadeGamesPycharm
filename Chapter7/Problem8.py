"""
 Write nested loop that prints 0 - 9 going up a digit each line

 Beef Erikson Studios - 2019
"""

for i in range(10):
    for j in range(i + 1):
        print(j, end=' ')
    print()
