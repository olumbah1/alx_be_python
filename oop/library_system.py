class Book:
    
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
         
    def __str__(self):
        return f'Book: {self.title} by {self.author}'
        
class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        super().__init__(title, author) # Initialize parent attributes
        self.file_size = file_size    # Child-specific attribute
        
    def __str__(self):
        return f'EBook: {super().__str__()}, File size: {self.file_size}KB' 
      
class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        super().__init__(title, author)
        self.page_count = page_count
        
    def __str__(self):
        return f'PrintBook: {super().__str__()}, Page Count: {self.page_count}'  
       
class Library:
    def __init__(self):
        self.books = []  # This is composition: Library HAS books
    
    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for book in self.books:
            print(book)