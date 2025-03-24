import secrets #Import secrets module for cryptographically secure random choices
import string #Import string module for character sets

def generate_secure_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation  # Combine all character sets
    password = ''.join(secrets.choice(characters) for _ in range(length))  # Generate password securely
    return password

# Test the function
print("Welcome to the Secure Password Generator!")
length = int(input("Enter the desired password length: "))
password = generate_secure_password(length)
print(f"Your generated secure password is: {password}")