import random

def russian_roulette():
    shots = random.choice(["you are dead","you survive","you survive","you survive","you survive","you survive"])
    return shots
print(russian_roulette())

