import sys
import math
from itertools import permutations, product

# ==============================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
ciphertext = "REST TRANSPORT YOU GODWIN VILLAGE ROANOKE WITH ARE YOUR IS JUST SUPPLIES\
              FREE SNOW HEADING TO GONE TO SOUTH FILLER"


# number of columns in the transposition matrix:
COLS = 4

# number of rows in the transposition matrix:
ROWS = 5

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key_ = " 1 2 3 4 "


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================


def main():
    """Run program and print decrypted plaintext."""
    print("\nCiphertext = {}".format(ciphertext))
    print("Trying {} columns".format(COLS))
    print("Trying {} rows".format(ROWS))
    print("Trying key = {}".format(key_))

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())
    n = 0
    key_int = key_to_int(key_)
    list_of_keys = perms(key_int)
    for keys in list_of_keys:
        translation_matrix = build_matrix(keys, cipherlist)
        plaintext = decrypt(translation_matrix)
        print("Plaintext = {}".format(plaintext))
        print()
        n += 1
    print(n)

def key_to_int(key):
    """Turn key into list of integers & check validity."""
    key_int = [int(i) for i in key.split()]
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
            or 0 in key_int:
        print("\nError - Problem with key. Terminating.", file=sys.stderr)
        sys.exit(1)
    else:
        return key_int

def perms(key_int):
    """Take number of columns integer & generate pos & neg permutations."""
    results = []
    for perm in permutations(key_int):
        for signs in product([-1, 1], repeat=len(key_int)):
            results.append([i*sign for i, sign in zip(perm, signs)])
    return results

def build_matrix(key_int, cipherlist):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * COLS
    i = 0
    for k in key_int:
        start = (abs(k)-1)*ROWS
        stop = abs(k)*ROWS
        if k > 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k < 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[i] = col_items
        i += 1
    return translation_matrix


def decrypt(translation_matrix):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(ROWS-1):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            if word == "VILLAGE":
                word = "Enemy"
            elif word == "GODWIN":
                word = "Tennesse"
            elif word == "ROANOKE":
                word = "Cavalery"
            elif word == "SNOW":
                word = "Rebels"
            else:
                word = word.lower()
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()