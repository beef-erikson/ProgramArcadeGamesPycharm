"""
 Write code that will print 1 to 9 to 1 in a pyramid using loops

 Beef Erikson Studios - 2019
"""

for i in range(1, 10):
    for j in range(9 - i):
        print('  ', end='')
    for k in range(i):
        print(k + 1, end=' ')
    for l in range(i - 1):
        i -= 1
        print(i, end=' ')
    print()
