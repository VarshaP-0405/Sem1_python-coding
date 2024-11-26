class Library:
    def __init__(self):
        self.book_name="Harry Potter"
        self.author_name="J.K.Rowling"
    def display(self):
        print(f"The Book Name is {self.book_name} and the author name is {self.author_name}")
lib=Library()
lib.display()
