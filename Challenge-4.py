import urllib.request
import urllib.parse
import re


x = "12345"
url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x


for i in range(400):
    response = urllib.request.urlopen(url)
    out = response.read()
    out = out.decode('utf-8')

    num = re.search('and the next nothing is ([0-9]+)', out)
    
    x = num.group(1)
    if x == "16044":
        x="8022"

    
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + x
    print(x)


