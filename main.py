from art import logo, vs
from game_data import data
import random
import os

print(logo)

def person():
    return random.choice(data)

game = True
person1 = person()
person2 = person()

print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
print(vs)
print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
score = 0

while game:
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    highest = max(person1["follower_count"], person2["follower_count"])

    if answer == "a":
        if person1["follower_count"] == highest:
            score += 1
        else:
            print(logo)
            game = False
            break
            print(f"Sorry, that's wrong. Final score: {score}")
    elif answer == "b":
        if person2["follower_count"] == highest:
            score += 1
        else:
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            game = False
            break

    person1 = person2
    person2 = person()

    os.system('cls')
    print(logo)
    print(f"You're right! Current score: {score}")
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
    print(vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")




