import random

# Function to generate a random number
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# Example function call
min_value = 1
max_value = 100
random_number = generate_random_number(min_value, max_value)

print(f"The randomly generated number between {min_value} and {max_value} is: {random_number}")
