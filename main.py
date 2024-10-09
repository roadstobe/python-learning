# Завдання 1: Клас «Людина»
class Person:
    def __init__(self, full_name, birth_date, phone, city, country, address):
        self.full_name = full_name
        self.birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def __str__(self):
        return f"Name: {self.full_name}, Born: {self.birth_date}, Phone: {self.phone}, City: {self.city}, Country: {self.country}, Address: {self.address}"

    def update_info(self, full_name=None, birth_date=None, phone=None, city=None, country=None, address=None):
        if full_name: self.full_name = full_name
        if birth_date: self.birth_date = birth_date
        if phone: self.phone = phone
        if city: self.city = city
        if country: self.country = country
        if address: self.address = address

# Завдання 2: Клас «Місто»
class City:
    def __init__(self, name, region, country, population, postal_code, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def __str__(self):
        return f"City: {self.name}, Region: {self.region}, Country: {self.country}, Population: {self.population}, Postal Code: {self.postal_code}, Phone Code: {self.phone_code}"

    def update_city(self, name=None, region=None, country=None, population=None, postal_code=None, phone_code=None):
        if name: self.name = name
        if region: self.region = region
        if country: self.country = country
        if population: self.population = population
        if postal_code: self.postal_code = postal_code
        if phone_code: self.phone_code = phone_code

# Завдання 3: Клас «Країна»
class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities  # Список міст

    def __str__(self):
        cities_str = ", ".join(self.cities)
        return f"Country: {self.name}, Continent: {self.continent}, Population: {self.population}, Phone Code: {self.phone_code}, Capital: {self.capital}, Cities: {cities_str}"

    def add_city(self, city_name):
        self.cities.append(city_name)

# Завдання 4: Клас «Дріб»
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def subtract(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def multiply(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def divide(self, other):
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

    def simplify(self):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor
        return self
