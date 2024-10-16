# Завдання 1

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f'Name: {self.name}, Age: {self.age}, Gender: {self.gender}'

class Builder(Human):
    def __init__(self, name, age, gender, experience):
        super().__init__(name, age, gender)
        self.experience = experience

    def get_info(self):
        return super().get_info() + f', Experience: {self.experience} years as Builder'

class Sailor(Human):
    def __init__(self, name, age, gender, rank):
        super().__init__(name, age, gender)
        self.rank = rank

    def get_info(self):
        return super().get_info() + f', Rank: {self.rank}'

class Pilot(Human):
    def __init__(self, name, age, gender, flight_hours):
        super().__init__(name, age, gender)
        self.flight_hours = flight_hours

    def get_info(self):
        return super().get_info() + f', Flight hours: {self.flight_hours}'


builder = Builder('John Doe', 30, 'Male', 5)
sailor = Sailor('Alice Smith', 28, 'Female', 'Captain')
pilot = Pilot('Tom Cruise', 40, 'Male', 1200)

print(builder.get_info())
print(sailor.get_info())
print(pilot.get_info())

# Завдання 2

class Passport:
    def __init__(self, full_name, country, passport_number):
        self.full_name = full_name
        self.country = country
        self.passport_number = passport_number

    def get_info(self):
        return f'Full Name: {self.full_name}, Country: {self.country}, Passport Number: {self.passport_number}'

class ForeignPassport(Passport):
    def __init__(self, full_name, country, passport_number, visa_info, foreign_passport_number):
        super().__init__(full_name, country, passport_number)
        self.visa_info = visa_info
        self.foreign_passport_number = foreign_passport_number

    def get_info(self):
        return super().get_info() + f', Visa Info: {self.visa_info}, Foreign Passport Number: {self.foreign_passport_number}'

passport = Passport('Jane Doe', 'Ukraine', 'UA1234567')
foreign_passport = ForeignPassport('Jane Doe', 'Ukraine', 'UA1234567', 'USA Visa', 'FP987654')

print(passport.get_info())
print(foreign_passport.get_info())

# Завдання 3

class Animal:
    def __init__(self, name, weight, habitat):
        self.name = name
        self.weight = weight
        self.habitat = habitat

    def get_info(self):
        return f'Animal: {self.name}, Weight: {self.weight} kg, Habitat: {self.habitat}'

class Tiger(Animal):
    def __init__(self, name, weight, habitat, stripe_count):
        super().__init__(name, weight, habitat)
        self.stripe_count = stripe_count

    def get_info(self):
        return super().get_info() + f', Stripe Count: {self.stripe_count}'

class Crocodile(Animal):
    def __init__(self, name, weight, habitat, length):
        super().__init__(name, weight, habitat)
        self.length = length

    def get_info(self):
        return super().get_info() + f', Length: {self.length} meters'

class Kangaroo(Animal):
    def __init__(self, name, weight, habitat, jump_distance):
        super().__init__(name, weight, habitat)
        self.jump_distance = jump_distance

    def get_info(self):
        return super().get_info() + f', Jump Distance: {self.jump_distance} meters'

tiger = Tiger('Bengal Tiger', 220, 'Jungle', 120)
crocodile = Crocodile('Nile Crocodile', 400, 'River', 5)
kangaroo = Kangaroo('Red Kangaroo', 85, 'Australian Outback', 10)

print(tiger.get_info())
print(crocodile.get_info())
print(kangaroo.get_info())
