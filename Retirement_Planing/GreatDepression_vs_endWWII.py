"""
            Input variables:
portfolio: 10 000 000 USD
                Object:
1 Take 2 periods for comparison:
    Great Depression(29-34) end of WWII(44-47)
                      4-9               19-22
2 For each year in each case, print out:
    the year,
    the returns rate,
    the inflation rate, and the outcome.
3 edit the bar chart to display each year’s outcome
"""

"""Retirement nest egg calculator using Monte Carlo simulation."""
import sys
import random
import matplotlib.pyplot as plt


def read_to_list(file_name):
    """Open a file of data in percent, convert to decimal & return a list."""
    with open(file_name) \
            as in_file:
        lines = [float(line.strip()) for line in in_file]
        decimal = [round(line / 100, 5) for line in lines]
        return decimal


def default_input(prompt, default=None):
    """Allow use of default values in input"""
    prompt = '{} [{}]: '.format(prompt, default)
    response = input(prompt)
    if not response and default:
        return default
    else:
        return response


# load data files with original data in percent form
print("\nNote: Input data should be in percent, not decimal!\n")
try:
    bonds = read_to_list('10-yr_TBond_returns_1926-2013_pct.txt')
    stocks = read_to_list('SP500_returns_1926-2013_pct.txt')
    blend_40_50_10 = read_to_list('S-B-C_blend_1926-2013_pct.txt')
    blend_50_50 = read_to_list('S-B_blend_1926-2013_pct.txt')
    infl_rate = read_to_list('annual_infl_rate_1926-2013_pct.txt')
except IOError as e:
    print("{}. \nTerminating program.".format(e), file=sys.stderr)
    sys.exit(1)

# get user input; use dictionary for investment-type arguments
investment_type_args = {'bonds': bonds, 'stocks': stocks,
                        'sb_blend': blend_50_50, 'sbc_blend': blend_40_50_10}

# print input legend for user
print("   stocks = SP500")
print("    bonds = 10-yr Treasury Bond")
print(" sb_blend = 50% SP500/50% TBond")
print("sbc_blend = 40% SP500/50% TBond/10% Cash\n")

print("Press ENTER to take default value shown in [brackets]. \n")

# get user input
invest_type = default_input("Enter investment type: (stocks, bonds, sb_blend," \
                            " sbc_blend): \n", 'bonds').lower()
while invest_type not in investment_type_args:
    invest_type = input("Invalid investment. Enter investment type " \
                        "as listed in prompt: ")

start_value = default_input("Input starting value of investments: \n", \
                            '10000000')
while not start_value.isdigit():
    start_value = input("Invalid input! Input integer only: ")

withdrawal = (0.04*int(start_value))


def montecarlo(returns, start_year, end_year):
    """Run MCS and return investment value at end-of-plan and bankrupt count."""
    outcome = []
    investments = int(start_value)
    lifespan = [i for i in range(start_year-26, end_year-26)]

    # build temporary lists for each case
    lifespan_returns = []
    lifespan_infl = []
    for i in lifespan:
        lifespan_returns.append(returns[i])
        lifespan_infl.append(infl_rate[i])

    # loop through each year of retirement for each case run
    for index, i in enumerate(lifespan_returns):
        infl = lifespan_infl[index]

        # don't adjust for inflation the first year
        if index == 0:
            withdraw_infl_adj = int(withdrawal)
        else:
            withdraw_infl_adj = int(withdraw_infl_adj * (1 + infl))

        investments -= withdraw_infl_adj
        investments = int(investments * (1 + i))

        outcome.append(investments)

    return outcome


def plot_func(plotdata, years):
    """generate matplotlib bar chart"""
    plt.figure('Outcome by Case (showing first {} runs)'.format(len(plotdata)),
               figsize=(16, 5))  # size is width, height in inches
    index = [i + years for i in range(len(plotdata))]
    plt.bar(index, plotdata, color='black')
    plt.xlabel('Year', fontsize=18)
    plt.ylabel('$ Outcome', fontsize=18)
    plt.ticklabel_format(style='plain', axis='y')
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}"
                                                         .format(int(x))))
    plt.title("Annual outcome", fontsize=20, color='red')
    plt.show()


def res_print(a, b, returns, outcome):
    for i in range(a-26, b-26):
        print("\nCurrent year {}: ".format(i+26))
        print("Annual return rate - '{}'".format(returns[i]))
        print("Annual inflation rate - '{}'".format(infl_rate[i]))
        print("Annual outcome - ${:,}".format(outcome[i]))


def main():
    """Call MCS & bankrupt functions and draw bar chart of results."""
    st_year_index = 29
    end_year_index = 34
    outcome = montecarlo(investment_type_args[invest_type], st_year_index, end_year_index+1)
    plot_func(outcome, st_year_index)
    res_print(st_year_index, end_year_index, investment_type_args[invest_type], outcome)

   
# run program
if __name__ == '__main__':
    main()
