"""
  Make a diamond out of numbers 1 to 9 to 1

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
for i in range(8):
    for j in range(i + 1):
        print('  ', end='')
    for k in range(8 - i):
        print(k + 1, end=' ')
    for l in range(7, i, -1):
        l -= i
        print(l, end=' ')
    print()
