import zipfile, re

doc = zipfile.ZipFile("channel.zip")
x = "90052"
y = 0
comments = []

for i in range(908):
    stuff = doc.read(x + ".txt").decode("utf-8")
    comments.append(doc.getinfo(x + ".txt").comment.decode("utf-8"))
    y += 1
    print('Count: ', y, '     ', stuff)
    num = re.search('Next nothing is ([0-9]+)', stuff)
    x = num.group(1)

print("".join(comments))
