class Book:
    def __init__(self, title, author, year, is_available):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = is_available
        self.__loan_counter = 0

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - Available: {self.is_available}"

    def lend(self):
        if self.is_available:
            self.is_available = False
            self.__loan_counter += 1
            return f"Times borrowed - {self.title}: {self.__loan_counter}."
        return f"{self.title}: is not available"

    def give_back(self):
        if self.is_available == False:
            self.is_available = True

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

"""
catalog = [book_1, book_2]
 for x in catalog:
    print(f"{x.title}, {x.author}. {x.year} - available: {x.is_available}")
"""

print(book_1.lend())
book_1.give_back()
print(book_1.lend())
print(book_1.__loan_counter)
