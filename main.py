import pandas as pd
import customtkinter as ctk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker

import numpy as np

from _ctkcore import ctk_core
from _variables import py_designer_var
from _guisetup import gui
from _handledata import dataHandler
from _plot import guiplot

class py_analog_designer(ctk_core, py_designer_var, gui, dataHandler, guiplot):
    def __init__(self):
        self.init_variables()
        self.init()
        self.init_ctk()
        self.setup_frame()
        self.setup_buttons()
        self.setup_dropdowns()
        self.setup_entries()
        self.setup_checkboxes()
        self.ctk_run()
        
    def set_active_model(self, value):
        self.active_model = value
    
    def set_active_plot(self, value):
        self.active_plot = value
        
    def set_xaxis(self, value):
        self.xaxis[self.active_plot] = value
    
    def set_yaxis(self, value):
        self.yaxis[self.active_plot] = value

    def new_plot(self):
        self.parse_input()
        self.plot()

if __name__ == "__main__":
    CTK_Window = py_analog_designer()