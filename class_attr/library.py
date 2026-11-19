
class Book:
    
    def __init__(self, title, author):
        self.title = title
        self.author = author
        availability = True
    
    def borrow_book(self):
        if self.availability == True:
            print("Book Borrowed Successfully")
            self.availability = False
        else:
            print("Book not available")
            
    def return_book(self):
        if self.availability == False:
            print("Book returned")
            self.availability = True
            
    def display_info(self):
        if self.availability == True:
            print(f"Title: {self.title}\nAuthor : {self.author}\nStatus : Available!")
        else:
            return (f"Title: {self.title}\nAuthor : {self.author}\nStatus : Borrowed!")
        
def run():
    
    book1 = Book("Things Fall Apart", "Chinua Achebe")

    book1.display_info()

    book1.borrow_book()
    book1.display_info()

    book1.borrow_book()

    book1.return_book()
    book1.display_info()
    