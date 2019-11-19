"""
 Write nested loop that prints 0 - 9 going down a digit each line

 Beef Erikson Studios - 2019
"""

for i in range(10):
    for j in range(i + 1):
        print('  ', end='')
    for k in range(10 - i):
        print(k, end=' ')
    print()
