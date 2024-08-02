import re

def validate_password(password):
    # Rule 1: Length between 6 and 24 letters
    if not 6 <= len(password) <= 24:
        return False

    # Rule 2: At least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Rule 3: At least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Rule 4: At least one digit (0-9)
    if not any(char.isdigit() for char in password):
        return False

    # Rule 5: Maximum of 2 repeated letters
    if re.search(r'(.)\1{2,}', password):
        return False

    # Rule 6: Supported special characters (@, #, $, *, _, !)
    if not any(char in '@#$*_!' for char in password):
        return False

    # All rules passed
    return True

# Example usage:
password_to_check = input("Enter the password to validate: ")

if validate_password(password_to_check):
    print("Password is valid.")
else:
    print("Password is invalid.")
