import random

# Function to generate a random number
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Example function call
random_number = generate_random_number(1, 100)

print(f"The randomly generated number between {1} and {100} is: {random_number}")
