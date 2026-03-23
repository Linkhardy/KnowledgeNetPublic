# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:09:12 2026

@author: FuchsbergerKai
"""

# controls.py
from matplotlib.widgets import Slider, Button

class ParameterSlider:
    def __init__(self, ax, label, valmin, valmax, valinit):
        self.slider = Slider(ax, label, valmin, valmax, valinit=valinit)

    def get(self):
        return self.slider.val

    def on_change(self, func):
        self.slider.on_changed(func)

class ActionButton:
    def __init__(self, ax, label, color='lightgray', hovercolor='0.9'):
        self.button = Button(ax, label, color=color, hovercolor=hovercolor)

    def on_click(self, func):
        self.button.on_clicked(func)