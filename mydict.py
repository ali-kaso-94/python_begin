
r"""
This is my first try to code an interactive program in Python
using a json file data file as a dictionary to give a definition _or multiple definitions_ to a given word by user,
utilizing python features and modules.
"""
import json
from difflib import get_close_matches as gcm
# in case we needed the value of similarity between two words scale [0,1]
#from difflib import SequenceMatcher as SM

data = json.load(open("data.json"))

def translate(word):
        word = word.lower()
        if word in data:
            return data[word]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif len(gcm(word, data.keys(), cutoff=0.8)) > 0:
            print("Did you mean %s instead?" %gcm(word, data.keys())[0])
            yn = input("press 'Y' or 'N': ")
            if yn == 'Y' or yn =='y':
                return data[gcm(word, data.keys())[0]]
            elif yn =='n' or yn =='N':
                 new = input("Enter a new word: ")
                 return translate(new)
            else:
                return "The word doesn't exist, please double check it."
        else:
            print("The word doesn't exist, please double check it.")
            new = input("Enter a new word: ")
            return translate(new)


word = input("Enter a Word: ")

output= translate(word)
if type(output) == list:
    total_lines = len(output)
    for line, line_num in zip(output, range(total_lines)):
        print(f"{line_num +1}- {line}")
else:
    print(output)
