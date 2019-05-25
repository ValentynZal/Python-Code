"""
1 Pick a location in the galaxy, an average travel speed of 5 to 10 percent of the speed of light,
    and a time step of 500,000 years.
2 At each time step, calculate the size of the expanding colonization bubble
    and update the galaxy map.
3 Check your results by placing the home­world location at the center of the galaxy,
    setting the speed to 1 , and confirming that it takes 50,000 years to reach the edge of the galaxy.

* Test how fast we would need to go to explore the galaxy in 10 million years
* Estimate how much of the galaxy the STF could have explored in its first 100 years,
    assuming they averaged 100x light speed
"""
from galaxy_simulator1 import build_galaxy
import tkinter as tk
# =============================================================================
# MAIN INPUT

VEL_FRACTION = 0.005
TIME_STEP = 1000000
GAL_RADIUS = 50000

# END INPUT
# ==============================================================================
def col_bubble(vel_fraction, time_step):
    """
    Simulate expanding colonisation bubble regarding to its arguments

    Arguments:
    velocity   - velocity as fraction of light
    location   - center of colonisation bubble
    time_step  - step for bubble expansion visualisation
    """
    root = tk.Tk()
    c = tk.Canvas(root, width=1000, height=800, bg='black')
    c.grid()
    c.configure(scrollregion=(-500, -400, 500, 400))
#   print velocity as fraction
    c.create_text(-455, -360, fill='white', anchor='w',
                  text='velocity as fraction of light = {} LY'.format(VEL_FRACTION))
#   print time_step
    c.create_text(-455, -330, fill='white', anchor='w',
                  text='time step = {} years'.format(TIME_STEP))
#   while expend won`t reach the galaxy edge
#       expend_rad = time_step*vel_fraction
#       determine distance to the galaxy edge
#       print(time_step)
#       draw circle according to expend_rad
#       time_step += time_step

def main():
    """Generate galaxy display, calculate detection probability, post stats."""
    build_galaxy()
    col_bubble(VEL_FRACTION, TIME_STEP)


if __name__ == '__main__':
    main()
