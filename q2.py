import random
# Make a random pet.

# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["gorrila", "human", "neanderthal"])
# Age (integer)
age = random.randint(1,100)
 # type: ignore
# Color (at least 3 choices, string)
color = random.choice(["black", "white", "yellow",])
# Weight (float)
weight = random.uniform(1,1000)


# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} he is {age} years old, he is {color} and weighs {weight} pounds")#REPLACE THIS WITH YOUR CODE