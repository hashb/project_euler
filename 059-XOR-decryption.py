from itertools import permutations as perm 
import re
def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(a^ord(b)) for a,b in zip(s,t))

f = open("059_cipher.txt","r")
w = open("cipher.txt","a")
cipher = map(int,f.read().split(","))

keys = map(list,perm('abcdefghijklmnopqrstuvwxyz',3))

for key in keys:
    key_new = key*401

    decrypt = xor_strings(cipher,key_new)
    new = decrypt
    if re.match("[*%#`\\*\~]",new.replace(' ','')):
        continue
    w.write("".join(key) + '\t' + decrypt+"\n")