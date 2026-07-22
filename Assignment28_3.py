fobj = open("Demo.txt", "r")

for line in fobj:
    print(line)
    print("-"*15)

fobj.close()