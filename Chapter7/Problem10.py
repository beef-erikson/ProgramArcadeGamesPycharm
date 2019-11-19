"""
 Write nested loop that prints multiplication table from 1 to 9

 Beef Erikson Studios - 2019
"""

for i in range(1, 10):
    for j in range(1, 10):
        if i * j < 10:
            print(" ", end='')
        print(i * j, end=' ')
    print()
