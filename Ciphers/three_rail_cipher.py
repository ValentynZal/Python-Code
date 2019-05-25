"""
This prog encrypt input string into three rail cipher
"""
# ==============================================================================
# USER INPUT:

# plain text to encrypt
plaintext = "I_really_like_puzzles!!!"

# number letters in chunk
n = 4

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
# ==============================================================================

def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    ciphertext = encrypt(rails)
    print("\nciphertext = {}".format(ciphertext))

    message = prep_ciphertext(ciphertext)
    length, row1, row2, row3 = split_rails(message)
    encrypt_mes = decrypt(length, row1, row2, row3)
    print("\nplaintext = {}".format(encrypt_mes))

def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace."""
    message = "".join(plaintext.split())
    message = message.upper()  # convention for ciphertext is uppercase
    print("\nplaintext = {}".format(plaintext))
    return message

def build_rails(message):
    """Build strings with every other letter in a message."""
    first_rail = message[0::4]
    # print(first_rail)
    seconde_rail = message[1::2]
    # print(seconde_rail)
    third_rail = message[2::4]
    # print(third_rail)
    rails = first_rail + seconde_rail + third_rail
    return rails

def encrypt(rails):
    """Split letters in ciphertext into chunks of n & join to make string."""
    ciphertext = ' '.join([rails[i:i+n] for i in range(0, len(rails),
                                                       n)])
    return ciphertext


def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    # print("\nciphertext = {}".format(ciphertext))
    return message


def split_rails(message):
    """Split message in three rows."""
    length = len(message)
    mod = length % 4

    if mod == 1:
        r1_len = (1/4)*(length-mod)+1
        r2_len = (1/2)*(length-mod)

    elif mod == 2:
        r1_len = (1/4)*(length-mod)+1
        r2_len = (1/2)*(length-mod)+1

    elif mod == 3:
        r1_len = (1/4)*(length-mod)+1
        r2_len = (1/2)*(length-mod)+1

    else:
        r1_len = (1/4)*(length-mod)
        r2_len = (1/2)*(length-mod)

    row1 = message[:int(r1_len)]
    row2 = message[int(r1_len):int(r1_len + r2_len)]
    row3 = message[int(r1_len + r2_len):]
    return length, row1, row2, row3


def decrypt(length, row1, row2, row3):
    """Build list with every other letter in 2 strings & print."""
    rev_row1 = list(reversed(row1))
    rev_row2 = list(reversed(row2))
    rev_row3 = list(reversed(row3))
    encrypt_mes = ""

    i = 1
    i = 1
    for i in range(int(length / 4)):
        encrypt_mes += "".join(rev_row1.pop())
        i += 1
        encrypt_mes += "".join(rev_row2.pop())
        i += 1
        encrypt_mes += "".join(rev_row3.pop())
        i += 1
        encrypt_mes += "".join(rev_row2.pop())
        i += 1
    if length % 4 == 1:
        encrypt_mes += "".join(rev_row1.pop())
    elif length % 4 == 2:
        encrypt_mes += "".join(rev_row1.pop())
        encrypt_mes += "".join(rev_row2.pop())
    elif length % 4 == 3:
        encrypt_mes += "".join(rev_row1.pop())
        encrypt_mes += "".join(rev_row2.pop())
        encrypt_mes += "".join(rev_row3.pop())

    return encrypt_mes

if __name__ == '__main__':
    main()