import xxtea
import base64
import hashlib
import os
import binascii

key = "1234567890123456"


text = "TEST MESSAGE"
"""myfile = open("passwordsxxteaupdated.txt", "r")
while myfile:
  line = myfile.readline()
  line_bytes = line.encode('ascii')
  base64_bytes = base64.b64encode(line_bytes)
  key = base64_bytes.decode('ascii')
  linehash = hashlib.md5(line.encode())
  key = linehash.hexdigest()
  print(len(key))
  decrypt_data = xxtea.decrypt(text,key)
  if decrypt_data != "":
      print(decrypt_data);
  if line == "":
      break
myfile.close()"""

e_data = xxtea.encrypt(text, key)
encoded = base64.b64encode(e_data)
print(encoded)
d_data = xxtea.decrypt(e_data,key)
print(text == d_data)
