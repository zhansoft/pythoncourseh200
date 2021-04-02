
# matplotlib usage guide

import matplotlib.pyplot as plt
# top of hierarchy w/ simple functions to create figures and explicitly create/keep track of figures/axes
# no pyplot = object oriented approach
import numpy as np
import pandas

# figure keeps track of all child 'axes' [titles, legends, etc] and the canvas [irrelevant for now]
fig = plt.figure()
fig.suptitle('No axes on this figure')
fig, ax_lst = plt.subplots(2, 2) # figure with grid of 2 x 2 axes

# axes: can only belong to one figure & has 2-3 axises; set_xlim(), set_ylim(), set_title(), set_xlabel(), set_ylabel()
# axis: set graph limits/generate ticks/ticklabels; location: Locator obj; ticklabel strings formatted by Formatter
# artist: everything visible on figure; drawn to canvas;most are tied to an axes but not shared or moved from one another

# for inputs: it expects np.array or np.ma.masked_array as input; change any other classes to np.array objects
# conversion of pandas.DataFrame
a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values
# conversion of np.matrix
b = np.matrix([[1,2], [3,4]])
b_asarray = np.asarray(b)

# plt.plot() creates axes from the first call
x = np.linspace(0, 2, 100) # returns array of numbers between (start, end, how many numbers you want)
y = np.linspace(0, 2, 100) # this creates the axes
plt.plot(x, x, label = 'linear')
plt.plot(x, x**2, label = 'quadratic')
plt.plot(x, x**3, label = 'cubic')
plt.plot(y, 2*(y**2), label = 'calciisucks') # still follows a f(x) format basically.
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("simple plot shit")
plt.legend()
#plt.show()
# pylab is for cluttered messy bitches. use pyplot instead

# coding styles: use the imports typically at the top
x = np.arange(0, 10, 0.2) # (start, end, increments)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
#plt.show()

# recommended function signature
def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax: Axes
        The axes to draw to
    
    data1: array
        The x data

    data2: array
        The y data
    
    param_dict : dict
        Dictionary of kwargs to pass to ax.plot

    Returns
    -------
    out: list
        list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out
# this turns into:
data1, data2, data3, data4 = np.random.randn(4,100)
fig, ax = plt.subplots(1,1) # row col
my_plotter(ax, data1, data2, {'marker': 'x'})
#plt.show()
# or for two
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
plt.show()

"""
backends: matplotlib has many different case uses and cant arget different outputs and thus each capability is a
 BACKEND
-does all the hard work behind-the-scenes to make the figure:
    -user interface backends "interactive" and hardcopy backends to make images "non-interactive"
# four ways to configure backend; if conflicting, the method mentioned last in the following list will be used
# use() will overide the setting in matplotlibrc
1. backend parameter in matplotlibrc file:
    backend: WXAgg # use wxpython with antigrain (agg) rendering  *** what the fuck
    # okay so wxpython is the gui module; antigrain is just some fucking thing
2. setting MPLBACKEND environment variable either for the current shell or single script
    windows: set MPLBACKEND=module://my_backend 
            python simple_plot.py
    # will override the backend parameter in ANY matplotlibrc so like try not to set it globally lmaooooo
3. use() # done before importing matplotlib.pyplot and will require changes in code if you want a different backend
    # avoid explicit usee unless absolutely necessary
"""

"""
writing graphical user interfaces or web apps:
matplotlib separates the renderer (drawing mechanism) from the canvas (window/place where drawing is)
-canon renderer = Agg (Anti-Grain Geometry C++ Library) to make a pixel image
    -raster renderer & filetypes of png & non-interactive (capable of writing to a file)
-raster renderers: pixel representation of line whose accuracy dependent on DPI setting
-vector renderers: commands needed like "line from here to there"
-other renderers that are interactive (capabel of displaying to the screen & writing a file using non-interactive renderers)
"""

# you can use the interactive backend of matplotlib but like that depends on funcs/methods
# so like matplotlib.pyplot.ion() or matploylib.pyplot.ioff()
# plt.ion()
# plt.plot([1.6, 2.7])
# plt.title("interactive test")
# plt.xlabel("index")
# ax = plt.gca()
# ax.plot([3.1, 2.2])
# plt.draw() #only call if it's not updtaed immediately

#non-interactive example
#import your shit
# plt.ioff()
# plt.plot([1.6, 2.7])
# plt.show()
# see it but terminal command line is unresponsive
# so non-interactive is actually more efficient

# summary: plt.show() = non-interactive; called multiple times & plt.draw() = interactive if shit broke

"""
Performance in matplotlib:
You can significantly reduce the rendering time by changing the appearance slightly of your graph but that's dependent
on the type of graph.
# line segment simplification lol ok
-path.simplify() #boolean whether they are & path.simplify_threshold() #controls how much line segments are simplified; the higher the better
example code:
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
y = np.random.rand(100000)
y[50000:] *= 2
y[np.logspace(1, np.log10(50000), 400).astype(int)] = -1
mpl.rcParams['path.simplify'] = True
mpl.rcParams['path.simplify_threshold'] = 0.0
plt.plot(y)
plt.show()
mpl.rcParams['path.simplify_threshold'] = 1.0
plt.plot(y)
plt.show()
'''
default simplifcation value: 1/9
# marker simplification but i'm really too fucking lazy
# splitting lines into smaller chunks whoops
# good ol fast style
'''
import matplotlib.style as mplstyle
mplstyle.use('fast')
'''
boom


