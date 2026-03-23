# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 08:08:32 2026

@author: FuchsbergerKai
"""

# models.py
import numpy as np

def harmonic(t, A=1, omega=1, phi=0):
    return A * np.sin(omega * t + phi)

def circular(t, R=1, omega=1, phi=0):
    x = R * np.cos(omega * t + phi)
    y = R * np.sin(omega * t + phi)
    return x, y