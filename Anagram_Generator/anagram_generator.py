""" program should automatically
 generate phrase anagrams from an input name and display a subset (for example, the
 first 500) for the user to review."""

# import modules
from collections import Counter
import load_dictionary
import time

start_time = time.time()

# prompt data
phrase = input("Enter word|phrase to anagram: ")
language = input("Switch the language(en|ger): ")
anagr_to_show = input("Enter max anagrams to show: ")
# max_anagrams = input("Enter max words in phrase: ")
max_letters = input("Enter max letters in the words: ")
min_letters = input("Enter min letters in the words:")

# dictionary upload:
if language == 'en':
    dict_file = load_dictionary.load('english_dict.txt')
elif language == 'ger':
    dict_file = load_dictionary.load('german_dict.txt')
else:
    language = input("Switch the language('en' or 'ger'): ")

# Ensure "a" & "I" are included. Sort dictionary
dict_file.append('a')
dict_file.append('i')
dict_file = sorted(dict_file)
dict_file = set(dict_file)

# dictionary word length filter
filtered_dict_file = []
for word in dict_file:
    if int(min_letters) <= len(word) and len(word) <= int(max_letters):
        filtered_dict_file.append(word)


# find anagrams
def find_anagrams(name, word_list):
    phrase_letter_map = Counter(name)
    anagram = []
    for word_f in word_list:
        test = ''
        word_letter_map = Counter(word_f.lower())
        for letter_f in word_f:
            if word_letter_map[letter_f] <= phrase_letter_map[letter_f]:
                test += letter_f
        if Counter(test) == word_letter_map:
            anagram.append(word_f)
    return anagram

# form anagram phrase combinations
n = 0
anagram_phrase_list = []
first_word = find_anagrams(phrase, filtered_dict_file)
for word in first_word:
    left_over_list = list(phrase)
    for letter in word:
        if letter in left_over_list:
            left_over_list.remove(letter)
    sec_word = find_anagrams(left_over_list, filtered_dict_file)

    for word_to_add in sec_word:
        anagram_phrase_list.append(word.title() + ' ' +  word_to_add.title())
        n += 1

# display results
print("Anagrams for: {}".format(phrase))
print("Anagram phrases {} found. Displaying first {}: ".format(len(anagram_phrase_list), anagr_to_show))
i = 0
while i < int(anagr_to_show):
    print(anagram_phrase_list[i], sep='\n')
    i += 1

end_time = time.time()
print("Runtime for this program was {} seconds.".format(end_time-start_time))