"""
  Example of text stripping

  Beef Erikson Studios - 2019
"""

plain_text = "This is a test. ABC abc"

encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x += 1
    c2 = chr(x)
    encrypted_text += c2
print(encrypted_text)

plain_text = ""
for c in encrypted_text:
    x = ord(c)
    x -= 1
    c2 = chr(x)
    plain_text += c2
print(plain_text)
