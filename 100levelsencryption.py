import telnetlib
import json
import base64
import random
import codecs
from Crypto.Util.number import *

HOST = "socket.cryptohack.org"
PORT = 13377
finalinput = ""
i = 1
tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

"""received = json_recv()

print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])
encodingtype1 = received["type"]
encodedinput1 = received["encoded"]"""

def decode_received(encodingtype,encodedinput):

    if encodingtype == "base64":
        finalinput1 = str(base64.b64decode(encodedinput))
    elif encodingtype == "hex":
        finalinput1 = bytearray.fromhex(encodedinput).decode()
    elif encodingtype == "rot13":
        finalinput1 = codecs.decode(encodedinput, 'rot_13')
    elif encodingtype == "bigint":
        encodedinput = encodedinput[2:]
        finalinput1 = bytearray.fromhex(encodedinput).decode()
        print(finalinput1)
    elif encodingtype == "utf-8":
        finalinput2 = [chr(b) for b in encodedinput]
        finalinput1 = ""
        for x in finalinput2:
            finalinput1 += x

    return finalinput1
received = json_recv()
while i < 110 :

    """print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])"""
    encodingtype1 = received["type"]
    encodedinput1 = received["encoded"]
    print(encodingtype1)
    finalinput = decode_received(encodingtype1,encodedinput1)
    to_send = {
        "decoded": finalinput
        }
    json_send(to_send)
    received = json_recv()
    print(received)
    i += 1
    print(i)
