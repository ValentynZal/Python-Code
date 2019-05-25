"""
Write a program that recombines letters using Markov order 2, 3, and 4 models and use
the program to generate interesting new words. Give them a definition and start
applying them. Who knows—you may coin the next frickin, frabjous, chortle, or trill!
"""
import load_dictionary
import logging
from collections import defaultdict
from itertools import permutations
import pprint
import random

# logging.disable(logging.CRITICAL)  # comment-out to enable debugging messages
# logging.basicConfig(level=logging.DEBUG, format='%(message)s')

# upload dict
dict_file = load_dictionary.load('english_dict.txt')

# generate all possible 2letters combs
comb_2_let = []
comb_2_let = {''.join(i) for i in permutations('abcdefghijklmnopqrstuvwxyz', 2)}
# print(comb_2_let, sep='')

# build dict assigning 2letters combs as keys(prefix)
# searhing for all possible suffixes for each 2letters prefix
dict_2_let = defaultdict(list)
for word in dict_file:
    for comb in comb_2_let:
        if comb in word:
            if dict_2_let.get(comb) == None:
                suf_index = word.rindex(comb)+2  # define suffix index
                if suf_index >= len(word):
                    break
                dict_2_let[comb] = []
                dict_2_let[comb].append(word[suf_index])
            else:
                suf_index = word.rindex(comb) + 2  # define suffix index
                if suf_index >= len(word):
                    break
                if word[suf_index] not in dict_2_let[comb]:
                    dict_2_let[comb].append(word[suf_index])
        # logging.debug("map_letter_to_letter value for key %s = %s\n",
        #               comb, dict_2_let[comb])
# pprint.pprint(dict_2_let, depth=20)

# prompt for word length
w_length = int(input("\nEnter desired length: "))
# prompt for word amount
w_amount = int(input("Enter desired amount of words to generate: "))

# rand from 2letters keys
def rand_let_gen():
    keys = list(dict_2_let.keys())
    rand_index = random.randrange(0, len(keys))
    return keys[rand_index]

# call function to build new word with Markov order 2
nword_list_m2 = []
for i in range(w_amount):
    rand_2_let = rand_let_gen()
    nword = "".join(rand_2_let)
    i = 0
    while len(nword) != w_length:
        prefix = nword[i:i+2:1]
        if dict_2_let.get(prefix) != None:
            nword += (dict_2_let[prefix][0])
            i += 1
        else:
            i = 0
            rand_2_let = rand_let_gen()
    nword_list_m2.append(nword)

# print words build with Markov order 2
print("\nHere is the list of new words: ")
pprint.pprint(nword_list_m2)