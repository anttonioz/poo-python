class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

first_book = Book("El padre Brown al completo", "G.K. Chesterton")
second_book = Book("Más allá del orden", "Jordan B. Peterson")

print(f"My book: {first_book.title} {first_book.author}")
print(f"My book: {second_book.title} {second_book.author}")