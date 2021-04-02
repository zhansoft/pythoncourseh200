import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

# plt.ioff()
# plt.plot(0, 0, 'ro')
# plt.axis([-10, 10, -10, 10])
# plt.title("non-interactive drawing fun")
# plt.xlabel("x shit")
# plt.ylabel("y shit")

fig = plt.gcf()
ax = plt.gca()
fig, ax = plt.subplots(1,1)

peppaNose = Ellipse((-2.5,3), width=8, height=5.3, angle=-32, color='#FFB6C1', fill=True)
peppaBHead = Ellipse((0,0), width=8, height=10.4, color = '#FFB6C1', fill=True)
peppaLEye = plt.Circle((-1.33065, 3.10606), .55 ,edgecolor='#FF69B4', linewidth = 2, facecolor='w', fill=True)
peppaREye = plt.Circle((0.32345, 1.83923), .55 ,edgecolor='#FF69B4', linewidth = 2, facecolor='w', fill=True)
peppaLEar = Ellipse((1,5.3), width = 1.3, height = 3.5, angle = -30, color = '#FFB6C1', fill = True)
peppaREar = Ellipse((2.8,4.2), width = 1.3, height = 3.5, angle = -50, color = '#FFB6C1', fill = True)
lpupil = plt.Circle((-1.59,3.29), .3, color = 'k', fill = True)


ax.set_title("peppa")
ax.set_xlim((-10, 10 ))
ax.set_xlabel('some type of x shiiii')
ax.set_ylim((-10, 10 ))
ax.set_ylabel('some type of y shiiii')

ax.add_artist(peppaNose)
ax.add_artist(peppaBHead)
ax.add_artist(peppaLEye)
ax.add_artist(peppaREye)
ax.add_artist(peppaREar)
ax.add_artist(peppaLEar)
ax.add_artist(lpupil)

plt.show()


#mplstyle.use(['dark_background','ggplot','fast'])

fig.savefig('doggy.png')