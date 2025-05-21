#Create a custom exception InvalidAgeError. 
#Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Define custom exception
class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(f"{message}. You entered: {age}")

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print("Age is valid.")

# Example usage with exception handling
try:
    check_age(16)
except InvalidAgeError as e:
    print(f" ⭕ InvalidAgeError caught: {e}")

