import re

with open("challenge-3.txt") as f:
    text = f.read()


x = ''.join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', text))


print(x)
