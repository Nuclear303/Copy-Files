import sys

with open("base.txt","r") as f:
    for i in range(3):
        for index,word in enumerate(f):
            with open("copy"+str(index)+".txt","w") as n:
                n.write(word)
