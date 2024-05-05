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
        settings = json.load(open("settings.json", "r"))
        self.xscale = float(settings["RESX"]) / 1920.0
        self.yscale = float(settings["RESY"]) / 1080.0 
        self.__init_tk()
        self.__setup_frame()
        self.__setup_buttons()
        self.__setup_labels()
        self.__setup_entries()
        self.__setup_dropdowns()
        self.__setup_checkboxes()
        self.plot()
        self.__run_tk()
        
    def quit(self) -> None:
        self.root.quit()

        
    def plot(self) -> None:
        fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=80, columnspan=120, pady=10, padx=10, sticky="NSEW")
        
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
        self.plot_btn = tk.Button(master=self.root, width=10, height=1, text="Plot", command=self.plot)
        self.plot_btn.grid(row=76, column=120, pady=1, padx=1)
        
        self.save_btn = tk.Button(master=self.root, width=10, height=1, text="Save Figure")
        self.save_btn.grid(row=76, column=121, pady=1, padx=1)
        
    def __setup_labels(self)  -> None:
        self.l1 = tk.Label(self.root, anchor="w", width=10, text="Plot:")
        self.l1.grid(row=10, column=120, pady=2)
        
        self.l2 = tk.Label(self.root, anchor="w", width=10, text="Model:")
        self.l2.grid(row=11, column=120, pady=2)
        
        self.l3 = tk.Label(self.root, anchor="w", width=10, text="x-axis:")
        self.l3.grid(row=12, column=120, pady=2)
        
        self.l4 = tk.Label(self.root, anchor="w", width=10, text="y-axis")
        self.l4.grid(row=13, column=120, pady=2)
        
        self.l4 = tk.Label(self.root, anchor="w", width=10, text="L (u):")
        self.l4.grid(row=14, column=120, pady=2)
        
        self.l4 = tk.Label(self.root, anchor="w", width=10, text="VDS (V):")
        self.l4.grid(row=15, column=120, pady=2)
        
    def __setup_dropdowns(self)  -> None:
        menus: dict[str, list[str]] = {
        "plots":    ["a", "b", "c", "d"],
        "models":   ["nch", "nch_25", "nch_hvt", "nch_lvt", "pch", "pch_25", "pch_hvt", "pch_lvt"],
        "axis":     ["vgs", "gmoverid", "gmro", "id/w"]}

        selected_plot = StringVar(self.root)
        selected_plot.set(menus["plots"][0])
        plot_menu = tk.OptionMenu(self.root, selected_plot, *menus["plots"])
        plot_menu.grid(row=10, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        selected_model = StringVar(self.root)
        selected_model.set(menus["models"][0])
        x_menu = tk.OptionMenu(self.root, selected_model, *menus["models"])
        x_menu.grid(row=11, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        selected_x = StringVar(self.root)
        selected_x.set(menus["axis"][3])
        x_menu = tk.OptionMenu(self.root, selected_x, *menus["axis"])
        x_menu.grid(row=12, column=121, pady=2, padx=(2, 10), sticky="ew")
        
        selected_y = StringVar(self.root)
        selected_y.set(menus["axis"][1])
        x_menu = tk.OptionMenu(self.root, selected_y, *menus["axis"])
        x_menu.grid(row=13, column=121, pady=2, padx=(2, 10), sticky="ew")

    def __setup_entries(self)  -> None:
        self.plot_entry = tk.Entry(self.root, width=10)
        self.plot_entry.grid(row=10, column=121, pady=2, padx=(2, 10))
        
        self.model_entry = tk.Entry(self.root, width=10)
        self.model_entry.grid(row=11, column=121, pady=2, padx=(2, 10))

        self.xaxis_entry = tk.Entry(self.root, width=10)
        self.xaxis_entry.grid(row=12, column=121, pady=2, padx=(2, 10))
        
        self.yaxis_entry = tk.Entry(self.root, width=10)
        self.yaxis_entry.grid(row=13, column=121, pady=2, padx=(2, 10))
        
        self.gateL_entry = tk.Entry(self.root, width=10)
        self.gateL_entry.grid(row=14, column=121, pady=2, padx=(2, 10))
        
        self.vdsrc_entry = tk.Entry(self.root, width=10)
        self.vdsrc_entry.grid(row=15, column=121, pady=2, padx=(2, 10))
        
    def __setup_checkboxes(self)  -> None:
        logx            = tk.IntVar()
        log_btn         = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=logx, text="Log Scale")
        log_btn.grid(row=16, column=121, pady=2, padx=(2, 10))
        
        single_plot     = tk.IntVar()
        single_plot_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=single_plot, text="Single Plot")
        single_plot_btn.grid(row=17, column=121, pady=2, padx=(2, 10))
        
        show_legend     = tk.IntVar()
        show_legend_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=show_legend, text="Show Legend")
        show_legend_btn.grid(row=18, column=121, pady=2, padx=(2, 10))
        
        gmoverid_mode   = tk.IntVar()
        gmoverid_mode_btn = tk.Checkbutton(self.root, onvalue=1, offvalue=0, width=10, anchor="w", variable=gmoverid_mode, text="gm/ID Mode")
        gmoverid_mode_btn.grid(row=19, column=121, pady=2, padx=(2, 10))