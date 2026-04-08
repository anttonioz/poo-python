class User:
  def __init__(self, name, card_id):
    self.name = name
    self.card_id = card_id
    self.borrowed_books = []
    self.loan_limit = 2

  def request_book(self, title):
    return f"Solicitud de libro {title} realizada"

class Student(User):
  def __init__(self, name, card_id, degree):
    super().__init__(name, card_id)
    self.degree = degree

    # Overwriding the limit
    self.loan_limit = 3

  def request_book(self, title):
    if len(self.borrowed_books) < self.loan_limit:
      self.borrowed_books.append(title)
      return f"Préstamo realizado: {title}"
    else:
      return f"Límite de préstamos alcanzado: {self.loan_limit}"

  def get_requested_books(self):
    return len(self.borrowed_books)


class Teacher(User):
  def __init__(self, name, card_id):
    super().__init__(name, card_id)

    # Overwriding the limit
    self.loan_limit = None

  def request_book(self, title):
    self.borrowed_books.append(title)
    return f"Préstamo realizado: {title}"


# Students
student_1 = Student("Jhon", "1234", "Engineering")
print(student_1.request_book("Sócrates"))
print(student_1.request_book("La Biblia"))
print(student_1.request_book("Psicoplogía"))
print(student_1.request_book("Padre Brown"))

# Teacher
teacher_1 = Teacher("Oswaldo", "Chemical")

print(teacher_1.request_book("Sócrates"))
print(teacher_1.request_book("La Biblia"))
print(teacher_1.request_book("Psicoplogía"))
print(teacher_1.request_book("Padre Brown"))
print(teacher_1.request_book("Chemical II"))