def plot_damage(wts="5", firerange="2048", armor="yes", location="head"):

    import numpy as np
    import matplotlib.pyplot as plt
    import weapons
    import pdb

    MAX_WEAPONS_TO_SHOW = int(wts)
    MAX_WEAPONS_TO_SHOW = 5
    CS_MAX_RANGE = int(firerange) # 2048 is roughly the distance down DD2 long
        # First set up the axis and figure environment
    fig, ax = plt.subplots()
    ax.set_title('Click on legend line to toggle line on/off')
    ax.set_xlabel('Range [units]')
    ax.set_ylabel('Damage [units]')

    linearray = []
    for weapon in weapons.weapons[:MAX_WEAPONS_TO_SHOW]:
        xpoints = range(0, CS_MAX_RANGE, 100)
        if armor == 'yes':
            ypoints = [weapon.damagerange_calc_witharmor(distance, location) for distance in xpoints]
        else:
            ypoints = [weapon.damagerange_calc_noarmor(distance, location) for distance in xpoints]

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
    plt.show()
    pdb.set_trace()
