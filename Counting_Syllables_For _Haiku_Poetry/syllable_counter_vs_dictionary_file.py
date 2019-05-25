"""
This program lets you test count_syllables.py  against a dictionary file.
After allowing the user to specify how many words to check,
choose the words at random and display a listing of each word
and its syllable count on separate lines.
"""
import sys
import load_dictionary
import pprint
import random
import json
from nltk.corpus import cmudict

# load dictionary of words in haiku corpus but not in cmudict
with open('missing_words.json') as f:
    missing_words = json.load(f)

cmudict = cmudict.dict()

def save_as_json(dict):
    """Save exceptions dictionary as json file."""
    json_string = json.dumps(dict)
    file = open('word_list.json', 'w')
    file.write(json_string)
    file.close()


"""upload dict maybe convert"""
word_list = load_dictionary.load('english_dict.txt')
save_as_json(word_list)

with open('word_list.json') as file_:
    word_list = json.load(file_)

def count_syllables(word):
    """Use corpora to count syllables in English word or phrase."""
    num_sylls = 0
    if word.endswith("s") or word.endswith("s"):
        word = word[:-1]
    if word in missing_words:
        num_sylls += missing_words[word]
    elif word in cmudict:
        for phonemes in cmudict[word][0]:
            for phoneme in phonemes:
                if phoneme[-1].isdigit():
                    num_sylls += 1
    else:
        print("This word is not present both in cmudict and missing_words: {}".format(word), file=sys.stderr)
        num_sylls = int(input("Please enter the number of syllables: "))

    return num_sylls

# try:
#     print("This word is not present both in cmudict and missing_words: {}".format(word))
# except KeyError:
#     num_sylls = int(input("Please enter the number of syllables: ", file=sys.stderr))

def main():
    while True:
        print("Syllable Counter")
        while True:
            to_check = input("Enter the number of words to check: ")
            if to_check.isdigit():
                to_check = int(to_check)
                break
        """choose randomly words from dict"""
        words = []
        syllables = {}
        for i in range(to_check):
            index = random.randrange(0, len(word_list))
            words.append(word_list[index])
        for word in words:
            syllables[word] = count_syllables(word)
        pprint.pprint(syllables)
        exit = input("press 'Enter' to repeat the process or 'n' to exit: ")
        if exit.lower() == "n":
            sys.exit()

if __name__ == '__main__':
    main()
