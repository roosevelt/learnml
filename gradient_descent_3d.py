#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

def func(x, y):
    # Calculate values of Z from the created grid
    z = x**2/5. + x*y/50. + y**2/5.
    return z

def partial_x(x,y):
    return 2*x/5. + y/50.

def partial_y(x,y):
    return x/50. + y/5.

# Algoritmo do Gradiente Descendente
def gradient_descent(x0, y0, learning_rate, epoch):
    plot_x = []
    plot_y = []
    plot_z = []

    plot_x.append(x0)
    plot_y.append(y0)
    plot_z.append(func(x0, y0))

    x = x0
    y = y0
    for i in range(epoch):
        x = x - learning_rate*(partial_x(x,y))
        y = y - learning_rate*(partial_y(x,y))
        
        plot_x.append(x)
        plot_y.append(y)
        plot_z.append(func(x, y))

    return plot_x, plot_y, plot_z


x0 = -2
y0 = 2.5
learning_rate = 1.3
epoch = 10

a = np.arange(-3, 3, 0.05)
b = np.arange(-3, 3, 0.05)

x, y = np.meshgrid(a, b)
z = func(x, y)

fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(x, y, z, edgecolor='none', rstride=1,
                        cstride=1, cmap='coolwarm')

# Desenhar gráfico da função
min_point = np.array([0., 0.])
min_point_ = min_point[:, np.newaxis]
ax.plot(*min_point_, func(*min_point_), 'bo', markersize=5)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$y$')
ax.set_zlabel(r'$z$')
##


# Criar animação
plot_x, plot_y, plot_z = gradient_descent(x0, y0, learning_rate, epoch)

line, = ax.plot([], [], [], 'g-', label = 'Gradient descent', lw = 1.5)
point, = ax.plot([], [], [], 'go')

def animate(i, line, point, plot_x, plot_y, plot_z):
    line.set_data(plot_x[:i], plot_y[:i])
    line.set_3d_properties(plot_z[:i])
    point.set_data(plot_x[i], plot_y[i])
    point.set_3d_properties(plot_z[i])


line.set_data([], [])
line.set_3d_properties([])
point.set_data([], [])
point.set_3d_properties([])


ax.legend(loc = 1)

anim = animation.FuncAnimation(fig, animate, fargs=(line, point, plot_x, plot_y, plot_z),
                               frames=len(plot_x), interval=120, 
                               repeat_delay=60)

out = open("animation.html", "w")
out.write(anim.to_html5_video())
out.close()
anim.save('3d.mp4', fps=15)
