class Book:
    def __init__(self, title, author, year, is_available):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available

book_1 = Book(
    "El padre Brown al completo",
    "G.K. Chesterton",
    "2017",
    True
)

book_2 = Book(
    "Más allá del orden",
    "Jordan B. Peterson",
    "2021",
    False
)

catalog = [book_1, book_2]

for x in catalog:
    print(f"{x.title}, {x.author}. {x.year} - available: {x.is_available}")