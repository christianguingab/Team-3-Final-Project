import random
from PasswordGenerator import PasswordGenerator

class StrengthenPassword(PasswordGenerator):
    def generate(self):
        print('Enter a password that will be strengthened')
        password = input('Password: ')

        while (
            len(password) < 12 or
            not any(char.isdigit() for char in password) or
            not any(char in '!@#$%^&*()' for char in password) or
            not any(char.isalpha() for char in password)
        ):
            password = (
                password.capitalize()
                + str(random.randint(50, 599))
                + random.choice('!@#$%^&*()')
                + random.choice('abcdefghijklmnopqrstuvwxyz')
            )

        return 'New password created: ' + password