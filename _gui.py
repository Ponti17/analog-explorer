import tkinter as tk
from tkinter import StringVar
import json

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

import numpy as np

class Gui:
    def __init__(self) -> None:
        # settings = json.load(open("settings.json", "r"))
        # self.xscale = float(settings["RESX"]) / 1920.0
        # self.yscale = float(settings["RESY"]) / 1080.0 
        self.__reset_vars()
        self.__init_tk()
        self.__setup_frame()
        self.__setup_buttons()
        self.__setup_labels()
        self.__setup_entries()
        self.__setup_dropdowns()
        self.__setup_checkboxes()
        self.plot()
        self.__run_tk()
        
    def __reset_vars(self) -> None:
        self.gateL:  dict[str, str] = {"a": "", "b": "", "c": "", "d": ""}
        self.vdsrc:  dict[str, str] = {"a": "", "b": "", "c": "", "d": ""}
        self.models: dict[str, str] = {"a": "", "b": "", "c": "", "d": ""}
        self.x_axis: dict[str, str] = {"a": "", "b": "", "c": "", "d": ""}
        self.y_axis: dict[str, str] = {"a": "", "b": "", "c": "", "d": ""}
        self.logx:   dict[str, int]      = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.show_legend: dict[str, int] = {"a": 0, "b": 0, "c": 0, "d": 0}
        
    def quit(self) -> None:
        self.root.quit()
        
    def plot(self) -> None:
        fig, axs = plt.subplots(nrows=1, ncols=1, figsize=(5,4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot().plot(t, 2 * np.sin(2 * np.pi * t))
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=80, columnspan=120, pady=10, padx=10, sticky="NSEW")
        
    def get_entry(self, entry: str) -> str:
        match entry:
            case "gateL":
                return self.gateL_entry.get()
            case "vdsrc":
                return self.vdsrc_entry.get()
            case "selected_plot":
                return self.selected_plot.get()
            case "selected_model":
                return self.selected_model.get()
            case "selected_x":
                return self.selected_x.get()
            case "selected_y":
                return self.selected_y.get()
            case _:
                raise Exception("Invalid entry")
            
    def get_checkbox(self, checkbox: str) -> int:
        match checkbox:
            case "logx":
                return self.logx.get()
            case "single_plot":
                return self.single_plot.get()
            case "show_legend":
                return self.show_legend.get()
            case "gmoverid_mode":
                return self.gmoverid_mode.get()
            case _:
                raise Exception("Invalid checkbox")
        
    def __init_tk(self) -> None:
        self.root = tk.Tk()
        self.root.title("analog-py-designer")
        self.root.after(201, lambda :self.root.iconbitmap('bjt.ico'))
        
    def __run_tk(self) -> None:
        self.root.mainloop()
        
    def __setup_frame(self) -> None:      
        self.figure_frame = tk.Frame(self.root, bg="darkblue", height=800, width=1200)
        self.figure_frame.grid(row=0, column=0, rowspan=80, columnspan=120, pady=10, padx=10)
        
    def __setup_buttons(self) -> None:
        plot_btn = tk.Button(master=self.root, width=10, height=1, text="Plot", command=self.plot)
        plot_btn.grid(row=76, column=120, pady=1, padx=1)
        
        save_btn = tk.Button(master=self.root, width=10, height=1, text="Save Figure")
        save_btn.grid(row=76, column=121, pady=1, padx=1)
        
    def __setup_labels(self)  -> None:
        l1 = tk.Label(self.root, anchor="w", width=10, text="Plot:")
        l1.grid(row=10, column=120, pady=2)
        
        l2 = tk.Label(self.root, anchor="w", width=10, text="Model:")
        l2.grid(row=11, column=120, pady=2)
        
        l3 = tk.Label(self.root, anchor="w", width=10, text="x-axis:")
        l3.grid(row=12, column=120, pady=2)
        
        l4 = tk.Label(self.root, anchor="w", width=10, text="y-axis")
        l4.grid(row=13, column=120, pady=2)
        
        l4 = tk.Label(self.root, anchor="w", width=10, text="L (u):")
        l4.grid(row=14, column=120, pady=2)
        
        l4 = tk.Label(self.root, anchor="w", width=10, text="VDS (V):")
        l4.grid(row=15, column=120, pady=2)
        
    def __setup_dropdowns(self)  -> None:
        menus: dict[str, list[str]] = {
        "plots":    ["a", "b", "c", "d"],
        "models":   ["nch", "nch_25", "nch_hvt", "nch_lvt", "pch", "pch_25", "pch_hvt", "pch_lvt"],
        "axis":     ["vgs", "gmoverid", "gmro", "id/w"]}

        self.selected_plot = StringVar(self.root)
        self.selected_plot.set(menus["plots"][0])
        plot_menu = tk.OptionMenu(self.root, self.selected_plot, *menus["plots"])
        plot_menu.grid(row=10, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        self.selected_model = StringVar(self.root)
        self.selected_model.set(menus["models"][0])
        x_menu = tk.OptionMenu(self.root, self.selected_model, *menus["models"])
        x_menu.grid(row=11, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        self.selected_x = StringVar(self.root)
        self.selected_x.set(menus["axis"][3])
        x_menu = tk.OptionMenu(self.root, self.selected_x, *menus["axis"])
        x_menu.grid(row=12, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        self.selected_y = StringVar(self.root)
        self.selected_y.set(menus["axis"][1])
        x_menu = tk.OptionMenu(self.root, self.selected_y, *menus["axis"])
        x_menu.grid(row=13, column=121, pady=2, padx=(2, 10), sticky="ew")

    def __setup_entries(self)  -> None:
        self.gateL_entry = tk.Entry(self.root, width=10)
        self.gateL_entry.grid(row=14, column=121, pady=2, padx=(2, 10))
        
        self.vdsrc_entry = tk.Entry(self.root, width=10)
        self.vdsrc_entry.grid(row=15, column=121, pady=2, padx=(2, 10))
        
    def __setup_checkboxes(self)  -> None:
        self.logx       = tk.IntVar()
        log_btn         = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=self.logx, text="Log Scale")
        log_btn.grid(row=16, column=121, pady=2, padx=(2, 10))
        
        self.single_plot= tk.IntVar()
        single_plot_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=self.single_plot, text="Single Plot")
        single_plot_btn.grid(row=17, column=121, pady=2, padx=(2, 10))
        
        self.show_legend= tk.IntVar()
        show_legend_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=self.show_legend, text="Show Legend")
        show_legend_btn.grid(row=18, column=121, pady=2, padx=(2, 10))
        
        self.gmoverid_mode = tk.IntVar()
        gmoverid_mode_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=self.gmoverid_mode, text="gm/ID Mode")
        gmoverid_mode_btn.grid(row=19, column=121, pady=2, padx=(2, 10))