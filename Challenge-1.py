mess='g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'
url='http://www.pythonchallenge.com/pc/def/map.html'

al='abcdefghijklmnopqrstuvwxyzab'
fin=""

length = len(mess)
t=0

while t<length:
        
    if not mess[t] in al:
        fin=fin+mess[t]
        t += 1
        continue
    else:
        ml = mess[t]
        pl = al.index(ml)
        x = al[pl+2]
        fin=fin+x
        t += 1

print(fin)
