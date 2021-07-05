"""This is a small program that takes search term as input from the user and returns exact or close match from a
json dict file called data"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))
while True:
    word = input("Insert the word you want to search: ").lower()

    if word in data:
        print(*(i for i in data[word]), sep="\n")
    elif word.title() in data:
        print(*(i for i in [word.title()]), sep="\n")
    elif word.upper() in data:
        print(*(i for i in data[word.upper()]), sep="\n")
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Exact match not found! Did you mean \u001b[36;1m%s\u001b[0m?" % get_close_matches(word, data.keys())[0])
        while True:
            decide = input("Press \033[1;92mY\033[1;m for \033[1;92mYES\033[1;m or \033[1;31;48mN\033[1;m for \033[1;31;48mNO\033[1;m.").lower()
            if decide == "y":
                print(*(i for i in data[get_close_matches(word, data.keys())[0]]), sep="\n")
                break
            elif decide not in ["y", "n"]:
                print("You have entered wrong input please insert \033[1;92mY\033[1;m or \033[1;31;48mN\033[1;m. ")
            else:
                print("Sorry, no other matches found! Try a different search term.")
                break
    else:
        print("Sorry, no matches found!")
        continue
    while True:
        print("Would you like to make another search?")
        another_word = input("Insert \033[1;92mY for another search\033[1;m or \033[1;31;48mN to quit\033[1;m. ").lower()

        if another_word == "y":
            break

        elif another_word not in ["y", "n"]:
            print("Wrong input!")
            another_word
        else:
            print("Thank you for using PyDict!")
            exit()



