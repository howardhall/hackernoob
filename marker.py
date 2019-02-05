#!/usr/bin/python3

import os, subprocess, sys
print("Prepare")
filename = sys.argv[1]
lol = [open("stdout.txt","w"),open("stderr.txt","w"),open("marked.txt","w")]
print("Initailize")
rc = subprocess.call(["gcc","-o","marking.out","submissions/"+filename],stdout=lol[0],stderr=lol[1])
if rc == 0:
    print("Execute")
    subprocess.call(["./marking.out"],stdout=lol[2])
print("Display\n")
for i in lol:
    i.close()
print("\33[93m"+open("marked.txt","r").read())
