import secrets
import string
import random

class PasswordGenerator:
    def __init__(self, pw_len, min_upper, min_lower, min_digits, min_spec):
        self.pw_len = pw_len
        self.min_upper = min_upper
        self.min_lower = min_lower
        self.min_digits = min_digits
        self.min_spec = min_spec
        self.all_chars = string.ascii_letters + string.digits + string.punctuation
        self.password = []

    def generate_random_chars(self, char_set, count):
        return ''.join(random.choice(char_set) for _ in range(count))

    def generate_password(self):
        self.password.extend(self.generate_random_chars(string.ascii_uppercase, self.min_upper))
        self.password.extend(self.generate_random_chars(string.ascii_lowercase, self.min_lower))
        self.password.extend(self.generate_random_chars(string.digits, self.min_digits))
        self.password.extend(self.generate_random_chars(string.punctuation, self.min_spec))

        remaining = self.pw_len - self.min_lower - self.min_upper - self.min_digits - self.min_spec
        self.password.extend(self.generate_random_chars(self.all_chars, remaining))
        random.shuffle(self.password)

    def get_password(self):
        return ''.join(self.password)

# User input
pw_len = int(input("How long should the password be? "))
min_upper = int(input("Minimum Upper Case: "))
min_lower = int(input("Minimum Lower Case: "))
min_digits = int(input("Minimum Numbers: "))
min_spec = int(input("Minimum Special: "))

# Create PasswordGenerator object
password_generator = PasswordGenerator(pw_len, min_upper, min_lower, min_digits, min_spec)

# Generate and print the password
password_generator.generate_password()
print("Generated Password:", password_generator.get_password())
