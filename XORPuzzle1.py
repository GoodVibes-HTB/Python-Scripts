import codecs
from Crypto.Util.number import *

hexinput = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
textinput = bytearray.fromhex(hexinput).decode()
numinput = [ord(b) for b in textinput]
xorlist = []
i = 1
while i < 10 :
    for j in numinput:
        xorlist.append(i ^ j)
    finalflag = [chr(c) for c in xorlist]
    print finalflag
    i += 1

"""print textinput
print numinput"""
