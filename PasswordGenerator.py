from abc import ABC, abstractmethod
import string

class PasswordGenerator(ABC):
    def __init__(self):
        # Character sets for generating passwords
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

    @abstractmethod
    def generate(self):
        pass
  
