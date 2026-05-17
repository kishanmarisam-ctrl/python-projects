# fake headline generator. #

import random

subjects = ["Scientists", "Politicians", "Celebrities",
            "Aliens", "Prime Ministers", "Presidents", "Kings", "Queens",
            "Wizards"]
verbs = ["discover", "invent", "debate", "conquer", "mysteriously disappear",
         "announce", "reveal", "steal", "save the world from",
         "celebrate the discovery of"]
objects = ["a new planet", "a cure for a disease",
           "a time machine", "a secret society", "a hidden treasure",
           "a new species", "a conspiracy theory", "a new technology",
           "a shocking scandal", "a groundbreaking invention"]


def generate_headline():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    headline = f"BREAKING NEWS: {subject} {verb} {obj}!"
    return headline


while True:
    user_input = input(
        "Do you want to generate a fake headline? (y/n): ").lower().strip()
    if user_input == "y":
        print(generate_headline())
    elif user_input == "n":
        print("Okay, goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'")
