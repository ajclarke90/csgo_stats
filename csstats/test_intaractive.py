"""
This is some code I used once to do interactive plots
allowing toggling of lines from the legend.
"""
import numpy as np
import matplotlib.pyplot as plt
import pynbody

s = pynbody.load('run670Diff.01550')
pynbody.analysis.angmom.faceon(s)
p = pynbody.analysis.profile.Profile(s.s, min=0.0, max=30, nbins=30)
q = pynbody.analysis.profile.Profile(s.g, min=0.0, max=30, nbins=30)


fig, ax = plt.subplots()
ax.set_title('Click on legend line to toggle line on/off')
line1, = ax.plot(p['rbins'], p['density'], lw=2, color='red', label='Stellar Density')
line2, = ax.plot(q['rbins'], q['density'], lw=2, color='blue', label='Gas Density')
leg = ax.legend(loc='upper right', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)


# we will set up a dict mapping legend line to orig line, and enable
# picking on the legend line
lines = [line1, line2]
lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)  # 5 pts tolerance
    lined[legline] = origline


def onpick(event):
    # on the pick event, find the orig line corresponding to the
    # legend proxy line, and toggle the visibility
    legline = event.artist
    origline = lined[legline]
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
plt.semilogy()
