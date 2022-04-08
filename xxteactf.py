import xxtea
import base64
import hashlib
import os
import binascii

text = "SDZcVdXvZHhKkxopTPYbTvmxTHwFZyyvnutAwsjijXwDqeOg"
myfile = open("passwordspecial.txt", "r")
while myfile:
  line = myfile.readline()
  """line_bytes = line.encode('ascii')
  base64_bytes = base64.b64encode(line_bytes)
  key = base64_bytes.decode('ascii')
  linehash = hashlib.md5(line.encode())
  key = linehash.hexdigest()
  print(len(key))"""
  decrypt_data = xxtea.decrypt(text,line)
  if decrypt_data != "" :
    print(line)
    print(decrypt_data);
  if line == "":
      break
myfile.close()
