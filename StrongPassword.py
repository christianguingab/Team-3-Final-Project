import random
import string
from PasswordGenerator import PasswordGenerator

class StrongPassword(PasswordGenerator):
    def generate(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(chars) for _ in range(12))
