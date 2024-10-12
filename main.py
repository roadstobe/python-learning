class Car:
  def __init__(self, model, year, manufacturer, engine_capacity, color, price):
    self.model = model
    self.year = year
    self.manufacturer = manufacturer
    self.engine_capacity = engine_capacity
    self.color = color
    self.price = price

  def display_info(self):
    print(f"Модель: {self.model}")
    print(f"Рік випуску: {self.year}")
    print(f"Виробник: {self.manufacturer}")
    print(f"Об'єм двигуна: {self.engine_capacity} л")
    print(f"Колір: {self.color}")
    print(f"Ціна: {self.price} $")

  def set_price(self, new_price):
    self.price = new_price
    print(f"Ціна оновлена: {self.price} $")

class Book:
  def __init__(self, title, year, publisher, genre, author, price):
    self.title = title
    self.year = year
    self.publisher = publisher
    self.genre = genre
    self.author = author
    self.price = price

  def display_info(self):
    print(f"Назва книги: {self.title}")
    print(f"Рік видання: {self.year}")
    print(f"Видавництво: {self.publisher}")
    print(f"Жанр: {self.genre}")
    print(f"Автор: {self.author}")
    print(f"Ціна: {self.price} $")

  def set_price(self, new_price):
    self.price = new_price
    print(f"Ціна оновлена: {self.price} $")

class Stadium:
  def __init__(self, name, opening_date, country, city, capacity):
    self.name = name
    self.opening_date = opening_date
    self.country = country
    self.city = city
    self.capacity = capacity

  def display_info(self):
    print(f"Назва стадіону: {self.name}")
    print(f"Дата відкриття: {self.opening_date}")
    print(f"Країна: {self.country}")
    print(f"Місто: {self.city}")
    print(f"Місткість: {self.capacity} осіб")

  def set_capacity(self, new_capacity):
    self.capacity = new_capacity
    print(f"Місткість оновлена: {self.capacity} осіб")




car = Car(model='VW', year="2024", manufacturer="German", engine_capacity=1.6, color="red", price=40000)
car.set_price(35000)

book = Book(title='Python', year=2024, publisher="IT step", genre="X3", author="E", price=300)

stadium = Stadium('Lviv arena', 2014, 'Ukraine', 'Lviv', 3000)

car.display_info()

book.display_info()

stadium.display_info()
