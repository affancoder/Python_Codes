import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    # Define all possible characters that can be used
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password by randomly selecting characters from the list of possible characters
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Ask user for password length
length = int(input("Enter desired password length: "))

# Generate password with the desired length
password = generate_password(length)

# Print the generated password
print(f"Generated password: {password}")