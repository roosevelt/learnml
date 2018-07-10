#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 22:41:28 2018

@author: roosevelt
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# função cujos parâmetros serão otimizados
def func(x):
    y = (x-1)*((x+3)**2)*((x-2)**3)*((x+1)**4)
    return y

# derivada da função escolhida
def derivative(x):
    y = ((x-2)**2) * ((x+1)**3) * ((10*(x**4)) + (37*(x**3)) - (17*(x**2)) - (101*x)+39)
   
    return y

# algoritmo do gradiente descendente
def gradient_descent(start_point, learning_rate, epochs):
    plot_x = []
    plot_y = []
    
    plot_x.append(start_point)
    plot_y.append(func(start_point))
    
    x = start_point
    for epoch in range(epochs):
        ## atualizacao de parâmetros
        x = x - learning_rate*(derivative(x))
        ###
        plot_x.append(x)
        plot_y.append(func(x))

    return plot_x, plot_y 

    

fig, axs = plt.subplots(2,3, figsize=(20,10))

# ponto inicial
start_point = -2.4
# taxa de aprendizado
#learning_rate = [0.99, 0.9,0.5,0.3, 0.02, 0.01]
learning_rate = [0.0099, 0.009,0.005,0.003, 0.0002, 0.0001]
# quantidade de iterações do algoritmo (épocas)
epochs = 50

axs = axs.flatten()
k=0

def animate(i, lines, points, plots_x, plots_y):
    for k in range(len(lines)):
        lines[k].set_data(plots_x[k][:i], plots_y[k][:i])
        points[k].set_data(plots_x[k][i], plots_y[k][i])
        legs[k].set_text('Min = ' + str("{:.4f}".format(plots_y[k][i])))


lines = []
points = []
plots_x = []
plots_y = []
legs = []
for i in range(len(axs)):
    ax = axs[i]
    
    # Desenhar gráfico da função
    x = np.arange(-4, 4, 0.1)
    y = func(x)
    ax.plot(x, y, lw = 0.9, color = 'k')
    ax.set_xlim([min(x), max(x)])
    ax.set_ylim([min(y), 500])
    ax.set_xlabel(r'$x (\alpha='+str(learning_rate[k])+r')$')
    ax.set_ylabel(r'$f(x)=(x-1)(x+3)^2(x-2)^3(x+1)^4$')
    ##

    # Destacar pontos e desenhar as setas
    plot_x, plot_y = gradient_descent(start_point, learning_rate[k], epochs)
    k+=1

    line, = ax.plot([], [], 'r', label = 'Gradient descent', lw = 1.5)
    point, = ax.plot([], [], 'bo')
    leg = ax.text(0.02, 0.02, '', transform=ax.transAxes)
    
    lines.append(line)
    points.append(point)
    plots_x.append(plot_x)
    plots_y.append(plot_y)
    legs.append(leg)
       
anim = animation.FuncAnimation(fig, animate, fargs=(lines, points, plots_x, plots_y), 
                               frames=len(plot_x), interval=200, 
                               repeat_delay=60)

out = open("animation.html", "w")
out.write(anim.to_html5_video())
out.close()
anim.save('test.mp4', fps=15)


    
