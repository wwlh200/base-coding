import os

L=[]

for d in os.listdir('.'):
    L.append(d)

print(L)