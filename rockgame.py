
import random

options = ("rock","scissor","paper")
player = None
computer = random.choice(options)

while player not in options:
    player = input("Enter your Choice(rock,paper,scissor):")

print(f"Player:{player}")
print(f"Computer:{computer}")