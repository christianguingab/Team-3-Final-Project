import string
from PasswordGenerator import PasswordGenerator

class AnalyzePassword(PasswordGenerator):
    def generate(self):
        pwd = input("Enter password to analyze: ")
        
        if len(pwd) >= 8 and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd):
            return "Password Strength: Strong"
        elif len(pwd) >= 6:
            return "Password Strength: Medium"
        else:
            return "Password Strength: Weak"