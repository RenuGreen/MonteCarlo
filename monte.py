"""Approximation of Pi value using the Monte Carlo method.
...
...     Select random points (x,y) in the unit square and determine
...     the ratio p = m/n where m is the number of points that satisfy
...     x^2 + y^2 <= 1 (points inside the circle) and n is the number 
...     of trials. Pi = 4 * p
...     """

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

figure = plt.figure(figsize=(8,8))
axes1 = figure.add_subplot(1, 1, 1)
axes1.set_title("Pi approximation using Monte Carlo method")
axes1.set_xlim(0, 1.5)
axes1.set_ylim(0, 1.5)

#-------------------
# draw the square
#-------------------
x = [1, 1, 1, 0]
y = [0, 1, 1, 1]
axes1.plot(x, y, color='k', linestyle='-', linewidth=3)

#--------------------
# draw the quadrant
#--------------------
circle1 = plt.Circle((0, 0), 1, color='k', fill=False, linewidth=3)
axes1.add_artist(circle1)

trials = 0
inside_circle = 0
x_outside, y_outside, x_inside, y_inside = [],[], [], []
sc_outside = axes1.scatter(x_outside, y_outside)
sc_outside.set_color('y')
sc_inside = axes1.scatter(x_inside, y_inside)
sc_inside.set_color('g')

text1 = plt.text(1, 1.4, "trials = 0")
text2 = plt.text(1, 1.3, "inside circle = 0")
text3 = plt.text(1, 1.2, "pi = 0")

#------------------------------------------
# plot the points and update the pi value
#------------------------------------------
def animate(i):
    global trials, inside_circle
    trials = trials + 1
    x = np.random.rand(1)
    y = np.random.rand(1)

    if x**2 + y**2 <= 1:
        x_inside.append(x)
        y_inside.append(y)
        sc_inside.set_offsets(np.c_[x_inside, y_inside])
        inside_circle = inside_circle + 1
    else:
        x_outside.append(x)
        y_outside.append(y)
        sc_outside.set_offsets(np.c_[x_outside, y_outside])

    text1.set_text("trials = %d" % trials)
    text2.set_text("inside circle = %d" % inside_circle)
    pi = 4.0*inside_circle/trials
    text3.set_text("pi = %f" % pi)

#-------------------------------------------------------------

ani = animation.FuncAnimation(figure, animate, frames=50, interval=1, repeat=True) 
plt.show()