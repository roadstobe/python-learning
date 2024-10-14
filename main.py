# Завдання 1 Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування, реалізуйте клас CoffeeMachine (містить інформацію про кавоварку),
# клас Blender (містить інформацію про блендер),
# клас MeatGrinder (містить інформацію про м'ясорубку).
# Кожен із класів має містити необхідні для роботи методи.
#


class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def display_info(self):
        print(f"Бренд: {self.brand}")
        print(f"Модель: {self.model}")
        print(f"Потужність: {self.power} Вт")


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_tank_capacity):
        super().__init__(brand, model, power)
        self.water_tank_capacity = water_tank_capacity

    def make_coffee(self):
        print(f"Приготування кави з {self.brand} {self.model}...")

    def display_info(self):
        super().display_info()
        print(f"Ємність резервуара для води: {self.water_tank_capacity} л")


class Blender(Device):
    def __init__(self, brand, model, power, speed_settings):
        super().__init__(brand, model, power)
        self.speed_settings = speed_settings

    def blend(self):
        print(f"Змішування інгредієнтів з {self.brand} {self.model}...")

    def display_info(self):
        super().display_info()
        print(f"Кількість швидкостей: {self.speed_settings}")


class MeatGrinder(Device):
    def __init__(self, brand, model, power, max_meat_capacity):
        super().__init__(brand, model, power)
        self.max_meat_capacity = max_meat_capacity

    def grind_meat(self):
        print(f"Подрібнення м'яса з {self.brand} {self.model}...")

    def display_info(self):
        super().display_info()
        print(f"Максимальна кількість м'яса: {self.max_meat_capacity} кг")

#
# Завдання 2 Створіть клас Ship, який містить інформацію про корабель.
# За допомогою механізму успадкування, реалізуйте клас Frigate (містить інформацію про фрегат),
# клас Destroyer (містить інформацію про есмінець),
# клас Cruiser (містить інформацію про крейсер). Кожен із класів має містити необхідні для роботи методи.

class Ship:
    def __init__(self, name, displacement, country_of_origin):
        self.name = name
        self.displacement = displacement
        self.country_of_origin = country_of_origin

    def display_info(self):
        print(f"Назва: {self.name}")
        print(f"Водотоннажність: {self.displacement} тонн")
        print(f"Країна походження: {self.country_of_origin}")


class Frigate(Ship):
    def __init__(self, name, displacement, country_of_origin, missile_count):
        super().__init__(name, displacement, country_of_origin)
        self.missile_count = missile_count

    def fire_missiles(self):
        print(f"Фрегат {self.name} запускає {self.missile_count} ракет.")

    def display_info(self):
        super().display_info()
        print(f"Кількість ракет: {self.missile_count}")


class Destroyer(Ship):
    def __init__(self, name, displacement, country_of_origin, torpedo_count):
        super().__init__(name, displacement, country_of_origin)
        self.torpedo_count = torpedo_count

    def launch_torpedoes(self):
        print(f"Есмінець {self.name} запускає {self.torpedo_count} торпед.")

    def display_info(self):
        super().display_info()
        print(f"Кількість торпед: {self.torpedo_count}")


class Cruiser(Ship):
    def __init__(self, name, displacement, country_of_origin, gun_caliber):
        super().__init__(name, displacement, country_of_origin)
        self.gun_caliber = gun_caliber

    def fire_guns(self):
        print(f"Крейсер {self.name} стріляє з гармат калібру {self.gun_caliber} мм.")

    def display_info(self):
        super().display_info()
        print(f"Калібр гармат: {self.gun_caliber} мм")


# Завдання 3 Запрограмуйте клас Money (об'єкт класу оперує однією валютою) для роботи з грошима.
# У класі мають бути передбачені поле для зберігання цілої частини грошей (долари, євро, гривні тощо)
# і поле для зберігання копійок (центи, євроценти, копійки тощо).
# Реалізувати методи для виведення суми на екран, задавання значень для частин.

class Money:
    def __init__(self, paper = 0, cents = 0):
        self.paper = paper + self.normalize(cents)[0]
        self.cents = self.normalize(cents)[1]


    def normalize(self, cents):
        if cents > 100:
            paper = cents // 100
            cents = cents % 100

            return paper, cents
        else:
            return 0, cents

    def add(self, paper, cents):
        self.paper += paper + self.normalize(cents)[0]
        self.cents += self.normalize(cents)[1]

    def get(self):
        return self.paper, self.cents

    def get_in_cents(self):
        return self.paper * 100 + self.cents

    def spend(self, paper, cents):
        self.paper -= paper + self.normalize(cents)[0]
        self.cents -= self.normalize(cents)[1]

    def get_balance(self, currency):
        return f'{self.paper} papers and {self.cents} cents {currency}'

class UAH(Money):
    def __init__(self, paper, cents):
        super().__init__(paper, cents)

    def get_balance(self):
        return super().get_balance('uah')

class USD(Money):
    def __init__(self, paper, cents):
        super().__init__(paper, cents)

    def get_balance(self):
        return super().get_balance('usd')

class EUR(Money):
    def __init__(self, paper, cents):
        super().__init__(paper, cents)

    def get_balance(self):
        return super().get_balance('euro')


# class Exchange:
#     def do_exchange(self, money_from, money_to, rate):
#         get_money_from = money_from.get_in_cents()
#
#         get_money_to = get_money_from * rate
#         money_to.add(get_money_to // 100, get_money_to % 100)
#         money_from.spend(get_money_to // 100, get_money_to % 100)


uah = UAH(1, 202)
usd = USD(0, 0)
eur = EUR(5, 6)

uah.add(5, 202)
uah.spend(1, 202)

# print(uah.get_balance())
# exchange = Exchange()
#
# exchange.do_exchange(uah, usd, 0.2)

print(usd.get_balance())
print(uah.get_balance())





