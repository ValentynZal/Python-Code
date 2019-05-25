"""
This program  takes the message as input
and automatically substitutes the code words,
fills the bottom row with dummy words, and
transposes the words using the key
[ - 1 , 3 , - 2 , 6 , 5 , - 4 ] .
It`s used a 6×7 matrix build from input plain text and own dummy words.

                        Code Words      Substitute words

                        Batteries       HOUNDS
                        Vicksburg       ODOR
                        April           CLAYTON
                        16              SWEET
                        Grand           TREE
                        Gulf            OWL
                        Forts           BAILEY
                        River           HICKORY
                        25              MULTIPLY
                        29              ADD
                        Admiral         HERMES
                        Porter          LANGFORD

                          translation_matrix

        We          will        run     the     batteries   at
        Vicksburg   the         night   of      April       16
        and         proceed     to      Grand   Gulf        where
        we          will        reduce  the     forts.      Be
        prepared    to          cross   the     river       on
        April       25          or      29.     Admiral     Porter.
        Keep        your        men     ready   for         party.
"""
# ==============================================================================
# USER INPUT:
plaintext = "We will run the batteries at\
            Vicksburg the night of April 16\
            and proceed to Grand Gulf where\
            we will reduce the forts. Be\
            prepared to cross the river on\
            April 25 or 29. Admiral Porter. "

#dummy row words which we going to add to our plain text
dummy_words = "Keep your men ready for party."

# route cipher keys
keys = [- 1, 3, - 2, 6, 5, - 4]

# key words wich will be substitute
key_words = ["batteries", "vicksburg", "april",   "16",    "grand", "gulf", "forts.",
             "river",     "25",       "29.",  "admiral", "porter."]
# words wich will substitute key words
subst_words = ["HOUNDS",  "ODOR",      "CLAYTON", "SWEET", "TREE",  "OWL",  "BAILEY.",
               "HICTORY", "MULTIPLY", "ADD.", "HERMES",  "LANGFORD."]

# column numbers
COLS = 6
# rows` numbers
ROWS = 7


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================

def substitute(complete_plaintext):
    """Automatically substitutes the code words"""
    cipherlist = list((complete_plaintext.lower()).split())
    for i in range(len(cipherlist)):
        if cipherlist[i] in key_words:
            # print(cipherlist[i])
            index = key_words.index(cipherlist[i])
            cipherlist[i] = subst_words[index]
            # print(subst_words[index])
        else:
            cipherlist[i] = cipherlist[i].upper()
    return cipherlist

def build_matrix(cipherlist):
    """Build 6×7 translation_matrix"""
    original_matrix = [None] * ROWS
    start = 0
    stop = COLS
    for k in range(1, ROWS+1):
        col_items = cipherlist[start:stop]
        original_matrix[k - 1] = col_items
        start += COLS
        stop += COLS
    return original_matrix

def encrypt(original_matrix):
    """Loop through nested lists popping off last item to a string."""
    new_col = []
    ciphertext = ''
    for k in keys:
        col = abs(k)
        for i in range(ROWS):
            new_col.append(original_matrix[i][col-1])
        if k < 0:
            new_col = list(reversed(new_col))
        for word in new_col:
            ciphertext += word + ' '
        new_col = []
    return ciphertext

def main():
    """convert input plaintext """
    complete_plaintext = plaintext + dummy_words
    cipherlist = substitute(complete_plaintext)
    original_matrix = build_matrix(cipherlist)
    print("\n")
    print(*original_matrix, sep="\n")
    print("\n")
    ciphertext = encrypt(original_matrix)
    print(ciphertext)

if __name__ == '__main__':
    main()