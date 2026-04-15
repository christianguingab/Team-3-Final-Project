from Password import Password
import string
import random 

class PasswordGenerator:
    def __init__(self):
        # Character sets for generating passwords
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate_strong_password(self, length=12):
        """Option 1: Generates a random, secure password."""
        all_chars = self.lowercase + self.uppercase + self.digits + self.symbols
        return ''.join(random.choice(all_chars) for _ in range(length))

    def analyze_password(self, password):
        """Option 2: Checks the strength of a password."""
        score = 0
        if any(c in self.lowercase for c in password): score += 1
        if any(c in self.uppercase for c in password): score += 1
        if any(c in self.digits for c in password): score += 1
        if any(c in self.symbols for c in password): score += 1
        if len(password) >= 12: score += 1
            
        strengths = {1: "Very Weak", 2: "Weak", 3: "Moderate", 4: "Strong", 5: "Very Strong"}
        return strengths.get(score, "Very Weak")

    def personalized_generator(self, keywords, length=16):
        """Option 3: Creates a password using specific user inputs."""
        base = "".join(keywords)
        if len(base) >= length:
            return base[:length]
        # Fills the rest of the length with random strong characters
        padding = self.generate_strong_password(length - len(base))
        return base + padding

    def strengthen_password(self, password):
        """Option 4: Adds extra complexity to an existing password."""
        if self.analyze_password(password) == "Very Strong":
            return password
        # Appends 4 random strong characters to improve it
        return password + self.generate_strong_password(4)
        
  
