"""
                                        Object
Write the program so that it predicts the probability of detecting 16 LY radius bubbles
given 15,600,000 transmitting civilizations randomly distributed throughout the galaxy (updated Drake equation output from Wikipedia). Use the
full 50,000 LY radius and 1,000 LY height of the galactic model when distributing the civilizations.

from random import randint
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import math
# =============================================================================
# MAIN INPUT

#
GAL_DISC_AREA = 7.85e9
GAL_DISC_HEI = 1000
BUBBLE_RAD = 100

# Number of advanced alien civilizations
NUM_CIVS = 15600000


# ==============================================================================
eq_gal_vol = GAL_DISC_AREA * GAL_DISC_HEI
print(eq_gal_vol)

eq_bubble_svol = math.ceil((4/3) * math.pi * math.pow(BUBBLE_RAD, 3))
# print(eq_bubble_svol)

cube_edge = math.floor(math.pow(eq_bubble_svol, (1/3)))
# print(cube_edge)
eq_bubble_cvol = math.pow(cube_edge, 3)
# print(eq_bubble_cvol)

num_eq_vol = int(eq_gal_vol/eq_bubble_cvol)
print(num_eq_vol)
"""

"""Calculate probability of detecting 32 LY-diameter radio bubble given 15.6 M
randomly-distributed civilizations in the galaxy."""
import math
from random import uniform, random
from collections import Counter

# length units in light-years
DISC_RADIUS = 50000
DISC_HEIGHT = 1000
NUM_CIVS = 15600000
DETECTION_RADIUS = 16


def random_polar_coordinates_xyz():
    """Generate uniform random xyz point within a 3D disc."""
    r = random()
    theta = uniform(0, 2 * math.pi)
    x = round(math.sqrt(r) * math.cos(theta) * DISC_RADIUS, 3)
    y = round(math.sqrt(r) * math.sin(theta) * DISC_RADIUS, 3)
    z = round(uniform(0, DISC_HEIGHT), 3)
    return x, y, z


def rounded(n, base):
    """Round a number to the nearest number designated by base parameter."""
    return int(round(n/base) * base)


def distribute_civs():
    """Distribute xyz locations in galactic disc model and return list."""
    civ_locs = []
    while len(civ_locs) < NUM_CIVS:
        loc = random_polar_coordinates_xyz()
        civ_locs.append(loc)
    return civ_locs


def round_civ_locs(civ_locs):
    """Round xyz locations and return list of rounded locations."""
    # convert radius to cubic dimensions:
    detect_distance = round((4 / 3 * math.pi * DETECTION_RADIUS**3)**(1/3))
    print("\ndetection radius = {} LY".format(DETECTION_RADIUS))
    print("cubic detection distance = {} LY".format(detect_distance))

    # round civilization xyz to detection distance
    civ_locs_rounded = []

    for x, y, z in civ_locs:
        i = rounded(x, detect_distance)
        j = rounded(y, detect_distance)
        k = rounded(z, detect_distance)
        civ_locs_rounded.append((i, j, k))

    return civ_locs_rounded


def calc_prob_of_detection(civ_locs_rounded):
    """Count locations and calculate probability of duplicate values."""
    overlap_count = Counter(civ_locs_rounded)
    overlap_rollup = Counter(overlap_count.values())
    num_single_civs = overlap_rollup[1]
    prob = 1 - (num_single_civs / NUM_CIVS)

    return overlap_rollup, prob


def main():
    """Call functions and print results."""
    civ_locs = distribute_civs()
    civ_locs_rounded = round_civ_locs(civ_locs)
    overlap_rollup, detection_prob = calc_prob_of_detection(civ_locs_rounded)
    print("length pre-rounded civ_locs = {}".format(len(civ_locs)))
    print("length of rounded civ_locs_rounded = {}"
          .format(len(civ_locs_rounded)))
    print("overlap_rollup = {}\n".format(overlap_rollup))
    print("probability of detection = {0:.3f}".format(detection_prob))

    # QC step to check rounding
    print("\nFirst 3 locations pre- and post-rounding:\n")
    for i in range(3):
        print("pre-round: {}".format(civ_locs[i]))
        print("post-round: {} \n".format(civ_locs_rounded[i]))


if __name__ == '__main__':
    main()


