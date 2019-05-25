"""Decrypt a path through a Union Route Cipher.
Designed for whole-word transposition ciphers with variable rows & columns.
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers means start at top & read down.
Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route; for negative key values read UP.
  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | | MESSAGE IS WRITTEN
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | ACROSS EACH ROW
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | IN THIS MANNER
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | | LAST ROW IS FILLED WITH DUMMY WORDS
|_|_|_v_|_|_|_v_|
START        END
Required inputs - a text message, # of columns, # of rows, key string
Prints translated plaintext
"""
import sys
import itertools

# ==============================================================================
# USER INPUT:

# the string to be decrypted (type or paste between triple-quotes):
cipherlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
              13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

"""THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY
AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM
CAN UP
"""

# number of columns in the transposition matrix:


# number of rows in the transposition matrix:


# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
# key = """ -1 2 -3 4 """


# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================


def main():
    # """Run program and print decrypted plaintext."""
    # print("\nCiphertext = {}".format(ciphertext))

    # split elements into words, not letters
    # cipherlist = list(ciphertext.split())

    cols, rows = validate_col_row(cipherlist)
    for col, row in itertools.zip_longest(cols, rows):

        # keys = [None] * 4
        # keys[0], keys[1] = keys_generator(col)
        # keys[2], keys[3] = keys_generator(list(reversed(cipherlist)), cols, rows)
        keys = {}
        keys["LU"], keys["LB"] = keys_generator(col)
        keys["RU"], keys["RB"] = keys_generator(list(reversed(cipherlist)), cols, rows)

        for k in keys.values():
            translation_matrix = build_matrix(col, row, keys, cipherlist)
            plaintext = decrypt(translation_matrix, row)
            print(plaintext)


def validate_col_row(cipherlist):
    """ перебрать все возможные комбины столбцов и рядов(другими словами кофигурация матрицы)"""
    """ возможнот предоставить пользователю отсеять маловероятные комбины """
    """Check that input columns & rows are valid vs. message length."""
    cols = []
    rows = []
    factors = []
    len_cipher = 24  # len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    for i in factors:
        j = i + 1
        for j in factors:
            if i * j == len_cipher:
                rows.append(i)
                cols.append(j)
    return cols, rows
    # print("\nLength of cipher = {}".format(len_cipher))
    # print("Acceptable column/row values include: {}".format(factors))
    # print()


""" написать функцию генератор ключей, которая будет принимать все варианты конфигураций матрицы 
и возращать все возможные пути"""


def keys_generator(col):
    keys1 = []
    keys2 = []
    for i in range(1, col + 1):
        if i % 2 == 0:
            keys1.append(i)
        else:
            keys1.append(i * (-1))
    return keys1
    for i in range(1, col + 1):
        if i % 2 != 0:
            keys2.append(i * (-1))
        else:
            keys2.append(i)
    return keys2


def build_matrix(cols, rows, keys, cipherlist):
    """Turn every n-items in a list into a new item in a list of lists."""
    translation_matrix = [None] * cols
    start = 0
    stop = rows
    for k in keys:
        if k < 0:  # read bottom-to-top of column
            col_items = cipherlist[start:stop]
        elif k > 0:  # read top-to-bottom of columnn
            col_items = list((reversed(cipherlist[start:stop])))
        translation_matrix[abs(k) - 1] = col_items
        start += rows
        stop += rows
    return translation_matrix


def decrypt(translation_matrix, row):
    """Loop through nested lists popping off last item to a string."""
    plaintext = ''
    for i in range(row):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()
