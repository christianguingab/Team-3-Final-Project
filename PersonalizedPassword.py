import random
from PasswordGenerator import PasswordGenerator

class PersonalizedPassword(PasswordGenerator):
    def generate(self,name,year,favorite_number):
        symbol1 = random.choice("!@#$%-_*")
        symbol2 = random.choice("!@#$%-_*")
        symbol3 = random.choice("!@#$%-_*")
        return name + year + symbol1 + favorite_number + symbol2 + symbol3
