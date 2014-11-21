
import numpy as np
import matplotlib.pyplot as plt
import weapons

MAX_WEAPONS_TO_SHOW = 20
CS_MAX_RANGE = 2048

# First set up the axis and figure environment
fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')

linearray = []
for weapon in weapons.weapons[:MAX_WEAPONS_TO_SHOW]:
    xpoints = range(0, CS_MAX_RANGE, 100)
    ypoints = [weapon.damagerange_calc_witharmor(distance, 'chest') for distance in xpoints]
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
