""" Write a program that takes a word as input and uses indexing
and slicing to return its Pig Latin equivalent """

def main():
    """prompt word, returns its Latin Pig equivalent"""
    vowels = ("a", "e", "i", "o", "u", "y")
    vowel = True

    while True:

        word = input("Enter any word: ")
        word = word.lower()
        sliced_1st_letter = word[0:1]
        sliced_word = word[1:]

        if word[0] in vowels:
            print(word + "way")
        else:
            print(sliced_word + word[0] + "ay")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()

