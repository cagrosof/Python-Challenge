import re

with open("capital.txt") as f:
    text = f.read()


x = ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))


print(x)
