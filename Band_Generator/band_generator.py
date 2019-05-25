"""Generate band names from 3 separate lists."""
import sys
import random

def main():
    """Choose names at random from 3 tuples of names and print to screen."""

    first_list = ('The', 'My', 'Our', 'This', 'Your', 'Her', 'Only', 'First', 
	              'New', 'About', 'Second', 'His', 'At', 'In', 'Behind', 'On',
	              'Over', 'Above', 'To', 'From', 'Into', 'Out', 'Among', 'All',
	              'Under', 'Between', 'For')

    second_list = ('Fallen', 'Discrupted', 'Lonely', 'Oldest', 'Dazzling', 'Dying'
	               , 'Burnt', 'Safety', 'Translating', 'Flying', 'Written', 
	               'Sleepy',  'Unfinished', 'Rainy', 'Tired', 'Burning', 'Broken', 
	               'Crying', 'Erased', 'Clear', 'Cold', 'Tender', 'Quiet', 
	               'Eternal', 'Waste', 'Pretty', 'Existing')

    third_list = ('Era', 'World', 'Day', 'Love', 'Quasar', 'Number', 'Star', 'Moon'
	              , 'Echo', 'Ghost', 'Tree', 'Time', 'Plane', 'Place', 'Fire', 
	              'Hope', 'Sky', 'Breath', 'Light', 'Sea', 'End', 'Field', 
	              'Platform', 'Mirror', 'Dream', 'Station', 'Pressure', 'Anxiet00y',
	              'Sign', 'Oxygen', 'Liquid')

    print("\nThis is band name random generetor")

    while True:

        first_word = random.choice(first_list)
        second_word = random.choice(second_list)
        third_word = random.choice(third_list)

        print("\nNew random name: ")
        print("{:>30} {} {}".format(first_word, second_word, third_word), file=sys.stderr)
    
        try_again = input("\n\nGenerate another name? (Press Enter else n to quit)\n ")

        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()