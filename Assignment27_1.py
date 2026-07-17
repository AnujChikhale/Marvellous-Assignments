class BookStore:
    NoOfBooks = 0
    def __init__(self, n, a):
        self.Name = n
        self.Author = a
        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):
        print(f"{self.Name} of {self.Author}. No of book: {self.NoOfBooks}")

bobj1 = BookStore("Atomic habbits1", "Charles")
obj1 = bobj1.Display()
bobj3 = BookStore("Atomic habbit3", "Charles")

obj1 = bobj3.Display()