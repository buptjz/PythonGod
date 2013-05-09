import os
r=input("type a directory name:")
for root,dirs,files in os.walk(r):
    for f in files:
        print(root,f)