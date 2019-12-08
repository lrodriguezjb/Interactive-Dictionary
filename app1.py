import json
from difflib import SequenceMatcher, get_close_matches

data = json.load(open("data.json"))


def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())[0]) > 0:
        answer = input(
            f"Did you mean {get_close_matches(word, data.keys())[0].title()} instead? Enter Y if Yes , or N if no: "
        )
        answer = answer.upper()
        if answer == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif answer == "N":
            return "The Word doesn't exist. Please Double Check It."
        else:
            return "We didn't understand your entry."
    else:
        return "The Word doesn't exist. Please Double Check It."


word = input("Enter A Word: ")
output = get_definition(word)

if type(output) == list:
    for item in output:
        print(f"-{item}")
else:
    print(output)
