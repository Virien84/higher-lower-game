import art
from game_data import data
import random
import os


def print_choices(a_entity, b_entity):
    print(
        f"Compare A: {a_entity['name']}, a {a_entity['description']}, from {a_entity['country']}."
    )
    print(art.vs)
    print(
        f"Against B: {b_entity['name']}, a {b_entity['description']}, from {b_entity['country']}."
    )


def game():
    score = 0
    keep_playing = True
    a_entity = random.choice(data)
    b_entity = random.choice(data)
    print(art.logo)
    print_choices(a_entity, b_entity)
    while keep_playing:
        choice = (input("Who has more followers? Type 'A' or 'B': ")).lower()
        if choice == "a":
            if a_entity["follower_count"] > b_entity["follower_count"]:
                score += 1
                os.system("clear")
                print(art.logo)
                print(f"You're right! Current score: {score}")
                b_entity = random.choice(data)
                print_choices(a_entity, b_entity)
            else:
                keep_playing = False
                print(f"Sorry, that's wrong. Final score: {score}")
        if choice == "b":
            if b_entity["follower_count"] > a_entity["follower_count"]:
                score += 1
                os.system("clear")
                print(art.logo)
                print(f"You're right! Current score: {score}")
                a_entity = b_entity
                b_entity = random.choice(data)
                print_choices(a_entity, b_entity)
            else:
                keep_playing = False
                print(f"Sorry, that's wrong. Final score: {score}")


game()
