def hist2d_flanking1d(x, y, bins="50"):


    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.ticker import NullFormatter, MaxNLocator
    from numpy import linspace
    import matplotlib.gridspec as gridspec
    from matplotlib import cm as cm

    # Set up default x and y limits
    xlims = [min(x),max(x)]
    ylims = [min(y),max(y)]
    # xlims = [0.0,0.4]
    # ylims = [0.8,1.0]
    # Set up your x and y labels
    xlabel = 'ecc'
    ylabel = 'JcJz'

    gs = gridspec.GridSpec(2,2, width_ratios=[4,1], height_ratios=[1,4])
    axTemperature = plt.subplot(gs[1,0])
    axHistx = plt.subplot(gs[0,0])
    axHisty = plt.subplot(gs[1,1])

    # # Remove the inner axes numbers of the histograms
    nullfmt = NullFormatter()
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # Find the min/max of the data
    xmin = min(xlims)
    xmax = max(xlims)
    ymin = min(ylims)
    ymax = max(ylims)

    # Make the 'main' temperature plot
    # Define the number of bins
    nxbins = 50
    nybins = 50
    nbins = 100

    xbins = linspace(start = xmin, stop = xmax, num = nxbins)
    ybins = linspace(start = ymin, stop = ymax, num = nybins)
    xcenter = (xbins[0:-1]+xbins[1:])/2.0
    ycenter = (ybins[0:-1]+ybins[1:])/2.0
    aspectratio = 1.0*(xmax - 0)/(1.0*ymax - 0)

    H, xedges,yedges = np.histogram2d(y,x,bins=(ybins,xbins))
    X = xcenter
    Y = ycenter
    Z = H

    # Plot the temperature data
    cax = (axTemperature.imshow(H, extent=[xmin,xmax,ymin,ymax],
    interpolation='nearest', origin='lower',aspect=aspectratio,
    cmap=cm.cubehelix))

    #Plot the axes labels
    axTemperature.set_xlabel(xlabel,fontsize=25)
    axTemperature.set_ylabel(ylabel,fontsize=25)

    #Make the tickmarks pretty
    ticklabels = axTemperature.get_xticklabels()
    for label in ticklabels:
        label.set_fontsize(18)
        label.set_family('serif')

    ticklabels = axTemperature.get_yticklabels()
    for label in ticklabels:
        label.set_fontsize(18)
        label.set_family('serif')

    #Set up the plot limits
    axTemperature.set_xlim(xlims)
    axTemperature.set_ylim(ylims)

    #Set up the histogram bins
    xbins = np.arange(xmin, xmax, (xmax-xmin)/nbins)
    ybins = np.arange(ymin, ymax, (ymax-ymin)/nbins)

    #Plot the histograms
    axHistx.hist(x, bins=xbins, color = 'blue', histtype='step')
    axHisty.hist(y, bins=ybins, orientation='horizontal', color = 'red',
    histtype='step')

    #Set up the histogram limits
    axHistx.set_xlim( xmin, xmax )
    axHisty.set_ylim( ymin, ymax )

    #Make the tickmarks pretty
    ticklabels = axHistx.get_yticklabels()
    for label in ticklabels:
            label.set_fontsize(12)
            label.set_family('serif')

    #Make the tickmarks pretty
    ticklabels = axHisty.get_xticklabels()
    for label in ticklabels:
        label.set_fontsize(12)
        label.set_family('serif')

    #Cool trick that changes the number of tickmarks for the histogram axes
    axHisty.xaxis.set_major_locator(MaxNLocator(2))
    axHistx.yaxis.set_major_locator(MaxNLocator(2))

    #Show the plot
    plt.draw()
