"""This is a small program that takes  search term as input from the user and returns exact or close match from a
json dict file called data"""

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

word = input("Please insert your search term: ").lower()


def translate(word):

    next_search = True
    while next_search:
        if word in data:
            print(data[word])
        elif word.title() in data:
            print([word.title()])
        elif word.upper() in data:
            print (data[word.upper()])
        elif len(get_close_matches(word, data.keys())) > 0:
            print("Exact match not found! Did you mean %s?" % get_close_matches(word, data.keys())[0])
            while True:
                decide = input("Press Y for YES or N for NO.").lower()
                if decide == "y":
                    print(data[get_close_matches(word, data.keys())[0]])
                elif decide == "n":
                    print("Sorry, no matches found! Try a different search term.")
                else:
                    print("You have entered wrong input please insert Y or N. ")
        else:
            print("Sorry, no matches found!")
            another_word = input("Press Y for another search or N to quit. ").lower()

            if another_word == "y":
                translate(word)
            elif another_word == "n":
                print("Thank you for using PyDict!")
                next_search = False




output = translate(word)
if type(output) == list:
    answer_n = 1
    for item in output:
        print("Meaning %d:" % answer_n)
        print(item)
        answer_n += 1
else:
    if output != None:
        print(output)



#elif next_search == "n":


