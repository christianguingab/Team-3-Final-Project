import random
from PasswordGenerator import PasswordGenerator

class PersonalizedPassword(PasswordGenerator):
    def generate(self):
        name = input("Enter your name: ")
        year = input("Enter your birth year: ")
        symbol = random.choice("!@#$%")
        return name + year + symbol