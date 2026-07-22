fobj = open("Demo.txt", "r")

count = 0

for line in fobj:
    count = count+1

print("Count of line is: ",count)
fobj.close()