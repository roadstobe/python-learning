# Завдання 1: Клас "Людина" зі статичним методом для підрахунку кількості створених об'єктів

class Human:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Human.count += 1

    @staticmethod
    def get_object_count():
        return f'Number of Human objects created: {Human.count}'

# Завдання 2: Клас для підрахунку площі геометричних фігур

class Geometry:
    calculation_count = 0

    @staticmethod
    def area_of_triangle(base, height):
        Geometry.calculation_count += 1
        return 0.5 * base * height

    @staticmethod
    def area_of_rectangle(length, width):
        Geometry.calculation_count += 1
        return length * width

    @staticmethod
    def area_of_square(side):
        Geometry.calculation_count += 1
        return side * side

    @staticmethod
    def area_of_rhombus(diagonal1, diagonal2):
        Geometry.calculation_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return f'Number of area calculations: {Geometry.calculation_count}'

# Завдання 3: Клас для обчислення математичних операцій

class MathOperations:
    @staticmethod
    def maximum(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def minimum(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result


# Тестові 1

human1 = Human("John", 30)
human2 = Human("Alice", 25)
human3 = Human("Bob", 40)

print(Human.get_object_count())

# Тестові 2

triangle_area = Geometry.area_of_triangle(10, 5)
rectangle_area = Geometry.area_of_rectangle(10, 20)
square_area = Geometry.area_of_square(5)
rhombus_area = Geometry.area_of_rhombus(6, 8)

print(f'Triangle area: {triangle_area}')
print(f'Rectangle area: {rectangle_area}')
print(f'Square area: {square_area}')
print(f'Rhombus area: {rhombus_area}')

print(Geometry.get_calculation_count())

# Тестові 3

max_value = MathOperations.maximum(3, 5, 9, 1)
print(f'Maximum: {max_value}')

min_value = MathOperations.minimum(3, 5, 9, 1)
print(f'Minimum: {min_value}')

avg_value = MathOperations.average(3, 5, 9, 1)
print(f'Average: {avg_value}')

factorial_value = MathOperations.factorial(5)
print(f'Factorial: {factorial_value}')
