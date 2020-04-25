import matplotlib.pyplot as plt
import numpy as np
#fig, ax = plt.subplots() # Create a figure containing a single axes.
#ax.plot([1,2,3,4],[1,4,2,3]) # Plot some data on the axes.
#plt.plot([1,2,3,4],[1,4,2,3]) # Matplotlib plots.
#fig = plt.figure() # an empty figure with no Axes
#fig, ax = plt.subplots() # a figure with a single Axes
#fig, axs = plt.subplots(2,2) # a figure with a 2*2 grid of axes

#b = np.matrix([[1,2],[3,4]])
#b_asarray = np.asarray(b)

"""
#object-oriented(OO)style
x = np.linspace(0,2,100)

# Note tha even in the OO-style, we use '.pyplot.figure' to create the figure.
fig, ax = plt.subplots() # Create a figure and an axes.
ax.plot(x,x,label="linear") # Plot some data on the axes.
ax.plot(x,x**2,label="quadratic") # Plot more data on the axes.
ax.plot(x,x**3,label="cubic") # ... and some more.
ax.set_xlabel("x label") # Add an x-label to the axes.
ax.set_ylabel("y label") # Add a y-label to the axes.
ax.set_title("Simple Plot") # Add a title to the axes.
ax.legend() # Add a legend

# pyplot-set_ylabel
x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
"""

def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out : list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
"""
data1,data2,data3,data4 = np.random.randn(4,100)
fig,ax = plt.subplots(1,1)
my_plotter(ax,data1,data2,{"marker":"o"})
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
"""

#plt.ion()
#plt.draw()
#plt.ioff()
#plt.show()
"""
for i in range(3):
    plt.plot(np.random.rand(10))
    plt.show()
"""
