import random
from PasswordGenerator import PasswordGenerator

class StrengthenPassword(PasswordGenerator):
    def generate(self,password):
        while len(password) < 12 or not any(char.isdigit() for char in password) or not any(char in '!@#$%^&*()' for char in password) or not any(char.isalpha() for char in password):  
            password = password.capitalize() + str(random.randint(50,599)) + str(random.choice('!@#$%^&*()')) + random.choice('abcdefghijklmnopqrstuvwxyz')
        else:
            print('New password created: ' + password +'\n')