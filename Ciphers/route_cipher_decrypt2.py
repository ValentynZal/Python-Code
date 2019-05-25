"""
Solve this route cipher. The number of columns
and rows must be factors of the message length, and the route starts in one of the corners,
doesn’t skip columns, and alternates direction with every column change.
"""


import sys
import itertools

# ==============================================================================
# USER INPUT:

ciphertext = "THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT WHY\
              AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN UP"

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================


def main():
    # """Run program and print decrypted plaintext."""
    # print("\nCiphertext = {}".format(ciphertext))

    # split elements into words, not letters
    cipherlist = list(ciphertext.split())


    cols, rows = validate_col_row(cipherlist)
    for col, row in itertools.zip_longest(cols, rows):

        # keys = [None] * 4
        # keys[0], keys[1] = keys_generator(col)
        # keys[2], keys[3] = keys_generator(list(reversed(cipherlist)), col)
        # keys = {}
        # keys["LU"], keys["LB"] = keys_generator(col)
        # keys["RU"], keys["RB"] = keys_generator(list(reversed(cipherlist)), col)

        keys = keys_generator(col)
        translation_matrix = build_matrix(col, row, keys, cipherlist)
        plaintext = decrypt(translation_matrix, row)
        plaintext.replace('WAYLAND', '')
        print(plaintext)
        print("\n\n")


def validate_col_row(cipherlist):
    """ перебрать все возможные комбины столбцов и рядов(другими словами кофигурация матрицы)"""
    """ возможнот предоставить пользователю отсеять маловероятные комбины """
    """Check that input columns & rows are valid vs. message length."""
    cols = []
    rows = []
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):  # range excludes 1-column ciphers
        if len_cipher % i == 0:
            factors.append(i)
    for i in range(len(factors)):
        j = i + 1
        for j in range(len(factors)):
            if factors[i] * factors[j] == len_cipher:
                rows.append(factors[i])
                cols.append(factors[j])
    return cols, rows


""" написать функцию генератор ключей, которая будет принимать все варианты конфигураций матрицы 
и возращать все возможные пути"""


def keys_generator(col):
    keys1 = []
    # keys2 = []
    for i in range(1, col + 1):
        if i % 2 == 0:
            keys1.append(i)
        else:
            keys1.append(i * (-1))
    return keys1
    # for i in range(1, col + 1):
    #     if i % 2 != 0:
    #         keys2.append(i * (-1))
    #     else:
    #         keys2.append(i)
    # return keys2


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
            if word == "WAYLAND":
                word = "captured"
            elif word == "NEPTUNE":
                word = "Richmond"
            elif word == "TRIBUNE":
                word = "Tribune"
            else:
                word = word.lower()
            plaintext += word + ' '
    return plaintext


if __name__ == '__main__':
    main()
