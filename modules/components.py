# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:10:25 2026

@author: FuchsbergerKai
"""

# components.py
class OscillatorPlot:
    def __init__(self, ax):
        self.line, = ax.plot([], [], color='tab:blue')  # same color as circle trace

    def update(self, t_data, x_data):
        self.line.set_data(t_data, x_data)


class CirclePlot:
    def __init__(self, ax, R):
        self.point, = ax.plot([], [], 'ro')          # moving circle point
        self.projection, = ax.plot([], [], 'b--')   # horizontal projection line
        self.trace, = ax.plot([], [], color='tab:blue')  # full trace line

        self.x_history = []
        self.y_history = []
        self.R = R

    def update(self, x, y):
        # update the moving point
        self.point.set_data([x], [y])

        # vertical projection to y-axis
        self.projection.set_data([x, x], [0, y])  # vertical line

        # append to full trace
        self.x_history.append(x)
        self.y_history.append(y)
        self.trace.set_data(self.x_history, self.y_history)

    def clear_trace(self):
        self.x_history.clear()
        self.y_history.clear()
        self.trace.set_data([], [])
        