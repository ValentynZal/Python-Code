"""
                                    Input:
-   Clinton_votes_Illinois.txt
-   Johnson_votes_Illinois.txt
-   Stein_votes_Illinois.txt
-   Trump_votes_Illinois.txt
-   benford.py

1   Your program should steal votes from the other candidates, while preserving the by­
county totals; that way, the total number of votes cast doesn’t change.
2   Print out the old and new vote totals by county for Trump and Clinton, as
well as their old and new statewide totals.
3   write out a text file that you can input
into benford.py so you can check how you did with respect to Benford’s law.

"""
import benford
from benford import load_data


def main():

    Clinton_votes_list = load_data("Clinton_votes_Illinois.txt")
    Johnson_votes_list = load_data("Johnson_votes_Illinois.txt")
    Stein_votes_list = load_data("Stein_votes_Illinois.txt")
    Trump_votes_list = load_data("Trump_votes_Illinois.txt")

    list_for_benford = []
    for i in range(len(Trump_votes_list)):
        # find i county total votes sum
        county_votes = Trump_votes_list[i] + Clinton_votes_list[i] + Johnson_votes_list[i] + Stein_votes_list[i]
        print("\nTrump: {}\t Clinton: {}\t Johnson: {}\t Stein: {}\t(True)".format(Trump_votes_list[i],
                                                                                 Clinton_votes_list[i],
                                                                                 Johnson_votes_list[i],
                                                                                 Stein_votes_list[i]))
        # find max if it`s not Trump`s swap make Trump`s votes maximum
        county_votes_list = [Trump_votes_list[i], Clinton_votes_list[i],
                             Johnson_votes_list[i], Stein_votes_list[i]]

        Trump_has_more = False
        max_votes_number = max(county_votes_list)
        print("max: {}".format(max_votes_number))
        if Trump_votes_list[i] == max_votes_number:
            Trump_has_more = True
            continue
        else:
            temp = Trump_votes_list[i]
            Trump_votes_list[i] = max_votes_number
            if Clinton_votes_list[i] == max_votes_number:
                Clinton_votes_list[i] = temp
                update = 'Clinton'
            elif Johnson_votes_list[i] == max_votes_number:
                Johnson_votes_list[i] = temp
                update = 'Johnson'
            else:
                Stein_votes_list[i] = temp
                update = 'Stein'

        # print updates
        if Trump_has_more == False:
            print("Trump: {}\t {}: {}   ('exchanged')".format(max(county_votes_list), update, temp))

    state_votes_list = Clinton_votes_list + Trump_votes_list + Stein_votes_list + Johnson_votes_list
    with open('state_votes.txt', 'w') as f:
        for item in state_votes_list:
            f.write("%s\n" % item)
    benford.main()


# enter state_votes.txt in the prompt
if __name__ == '__main__':
    main()
