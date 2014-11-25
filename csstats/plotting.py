import numpy as np
import matplotlib.pyplot as plt
import weapons
import pdb



def plot_damage(wtype="pistol", firerange=2048, armor=True, location="head"):

    if wtype not in {w.type for w in weapons.weapons}:
        raise ValueError("{0} not a valid weapon type".format(wtype))
    if location not in ["head", "chest", "stomach", "leg"]:
        raise ValueError("{0} not a valid hitbox location".format(location))
    CS_MAX_RANGE = int(firerange) # 2048 is roughly the distance down DD2 long
    # First set up the axis and figure environment
    fig, ax = plt.subplots()

    ax.set_xlabel('Range [units]')
    ax.set_ylabel('Damage [units]')

    linearray = []
    for weapon in [w for w in weapons.weapons if w.type == wtype]:

        xpoints = range(0, CS_MAX_RANGE, (CS_MAX_RANGE-0)/100)

        if armor:
            ypoints = [weapon.damagerange_calc_witharmor(distance, location) for distance in xpoints]
            ax.set_title('Damage at Distance with Armor')
        else:
            ypoints = [weapon.damagerange_calc_noarmor(distance, location) for distance in xpoints]
            ax.set_title('Damage at Distance without Armor')
        line, = ax.plot(xpoints,ypoints, label=weapon.name)
        linearray.append((weapon.name, line))
        lines = [a[1] for a in linearray]
        leg = ax.legend(loc='upper right', fancybox=True, shadow=True)
        leg.get_frame().set_alpha(0.4)

        legd = {}
        for legline, origline in zip(leg.get_lines(), lines):
            legline.set_picker(5)  # 5 pts tolerance
            legd[legline] = origline

    def onpick(event):
        # on the pick event, find the orig line corresponding to the
        # legend proxy line, and toggle the visibility
        legline = event.artist
        origline = legd[legline]
        vis = not origline.get_visible()
        origline.set_visible(vis)
        # Change the alpha on the line in the legend so we can see what lines
        # have been toggled
        if vis:
            legline.set_alpha(1.0)
        else:
            legline.set_alpha(0.2)
        fig.canvas.draw()

    fig.canvas.mpl_connect('pick_event', onpick)
    plt.plot([0,CS_MAX_RANGE],[100,100], 'r--')

    return plt
