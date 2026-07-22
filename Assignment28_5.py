filename = input("Enter file name: ")
Word = input("Enter the word to find: ")

fobj = open(filename, "r")

data = fobj.read()

array_of_words = data.split()

present = False
for word in array_of_words:
    
    if(word == Word):
        present = True

if(present == True):
    print("Word is present in file")
else:
    print("word is not present in file")