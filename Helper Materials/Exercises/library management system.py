class Library:
    def __init__(self):
        self.noBooks = 0
        self.Books = []

    def addBook(self, book):
        self.Books.append(book)
        self.noBooks = len(self.Books)
    
    @property #--> Getter
    def showdetails(self):
        print(f"Number of books in this library is : {self.noBooks}")
        print("Names of books present in this library are : ")
        for book in self.Books:
            print(book)


a = Library()
a.addBook("Hercules")
a.addBook("Java")
a.addBook("Python")
a.showdetails
