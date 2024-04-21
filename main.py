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
        self.setup_textboxes()
        self.setup_dropdowns()
        self.setup_entries()
        self.setup_checkboxes()
        self.ctk_run()

    def new_plot(self):
        self.parse_input()
        self.plot()

if __name__ == "__main__":
    CTK_Window = py_analog_designer()