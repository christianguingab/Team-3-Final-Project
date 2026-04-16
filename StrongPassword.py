from PasswordGenerator import PasswordGenerator
import random

class StrongPassword(PasswordGenerator):
    def generate(self,length=12):
        """Option 1: Generates a random, secure password."""
        all_chars = self.lowercase + self.uppercase + self.digits + self.symbols
        return ''.join(random.choice(all_chars) for _ in range(length))