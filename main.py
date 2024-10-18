class Fraction:
    count = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.count += 1

    def get_fraction(self):
        return f'{self.numerator}/{self.denominator}'

    @staticmethod
    def get_object_count():
        return f'Number of Fraction objects created: {Fraction.count}'


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)

print(f1.get_fraction())
print(f2.get_fraction())
print(Fraction.get_object_count())


class TemperatureConverter:
    conversion_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.conversion_count += 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.conversion_count += 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_conversion_count():
        return f'Number of temperature conversions: {TemperatureConverter.conversion_count}'

temp_in_f = TemperatureConverter.celsius_to_fahrenheit(25)
temp_in_c = TemperatureConverter.fahrenheit_to_celsius(77)

print(f'25°C = {temp_in_f}°F')
print(f'77°F = {temp_in_c}°C')
print(TemperatureConverter.get_conversion_count())

class LengthConverter:
    conversion_count = 0

    @staticmethod
    def meters_to_feet(meters):
        LengthConverter.conversion_count += 1
        return meters * 3.28084

    @staticmethod
    def feet_to_meters(feet):
        LengthConverter.conversion_count += 1
        return feet / 3.28084

    @staticmethod
    def kilometers_to_miles(kilometers):
        LengthConverter.conversion_count += 1
        return kilometers * 0.621371

    @staticmethod
    def miles_to_kilometers(miles):
        LengthConverter.conversion_count += 1
        return miles / 0.621371

    @staticmethod
    def get_conversion_count():
        return f'Number of length conversions: {LengthConverter.conversion_count}'


length_in_feet = LengthConverter.meters_to_feet(100)
length_in_meters = LengthConverter.feet_to_meters(328.084)
length_in_miles = LengthConverter.kilometers_to_miles(10)
length_in_kilometers = LengthConverter.miles_to_kilometers(6.21371)

print(f'100 meters = {length_in_feet} feet')
print(f'328.084 feet = {length_in_meters} meters')
print(f'10 kilometers = {length_in_miles} miles')
print(f'6.21371 miles = {length_in_kilometers} kilometers')
print(LengthConverter.get_conversion_count())

