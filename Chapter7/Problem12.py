"""
  Draw a pyramid, then a cascading number line using loops

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
    print()
