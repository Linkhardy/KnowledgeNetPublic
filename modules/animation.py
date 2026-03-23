# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:09:45 2026

@author: FuchsbergerKai
"""

# animation.py
from matplotlib.animation import FuncAnimation

class Animator:
    def __init__(self, fig, update_func, frames=300, interval=50):
        self.anim = FuncAnimation(
            fig,
            update_func,
            frames=frames,
            interval=interval
        )