fobj = open("Demo.txt", "r")

data = fobj.read()

print("Count of words is:", len(data.split(" ")))