import pandas as pd
import customtkinter as ctk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from gui_ctk import ctk_setup

class py_analog_designer(ctk_setup):
    def __init__(self):
        self.init_ctk()
        self.setup_frame()
        self.setup_buttons()
        self.setup_variables()
        self.setup_dropdowns()
        self.setup_entries()
        self.setup_checkboxes()
        self.run()
        
    def setup_frame(self):
        self.frame = ctk.CTkFrame(master=self.root,
                            height =self.root.winfo_height()*0.9,
                            width  =self.root.winfo_width()*1.6,
                            fg_color="darkblue")
        self.frame.place(relx=0.025, rely=0.025)
    
    def setup_buttons(self):
        self.button = ctk.CTkButton(master=self.root,
                                    text="Plot",
                                    width=100,
                                    height=50,
                                    command=self.update_plot)
        self.button.place(relx=0.9,rely=0.55)
        
        self.save_button = ctk.CTkButton(master=self.root,
                                    text="Save Fig",
                                    width=100,
                                    height=50,
                                    command=self.save)
        self.save_button.place(relx=0.8,rely=0.55)
        
        self.quit_button = ctk.CTkButton(master=self.root,
                                    text="Quit",
                                    width=100,
                                    height=50,
                                    command=self.quit)
        self.quit_button.place(relx=0.9,rely=0.65)
        
    def setup_variables(self):
        self.active_plot = "a"
        self.yaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis_title = {"a": "",
                            "b": "",
                            "c": "",
                            "d": ""}
        self.yaxis_title = {"a": "",
                            "b": "",
                            "c": "",
                            "d": ""}
        self.models = ["nch"]
        self.axis_variables = ["gmoverid", "gm", "vgs", "gds", "gmro", "id/w", "ft", "ft*gmoverid"]
        self.plots = ["a", "b", "c", "d"]
        
        # user inputs
        self.model      = {"a": "nch",
                           "b": "nch",
                           "c": "nch",
                           "d": "nch"}
        self.vds        = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.L          = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.pros_L     = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.log_scale  = {"a": "off",
                           "b": "off",
                           "c": "off",
                           "d": "off"}
        
    def setup_dropdowns(self):
        # active plot
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.075)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.plots,
                                command=self.set_active_plot)
        self.xaxis_dropdown.place(relx=0.9,rely=0.08)
        self.xaxis_dropdown.set("a")
                        
        # active model
        self.model_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.model_text.place(relx=0.85, rely=0.125)
        self.model_text.insert("0.0", "Model:")
        self.model_text.configure(state="disabled") # READONLY after insert

        self.model_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.models,
                                command=self.set_active_model)
        self.model_dropdown.place(relx=0.9,rely=0.13)
        self.model_dropdown.set("nch")

        # axis dropdowns
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.175)
        self.axis_text.insert("0.0", "X-axis")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.225)
        self.axis_text.insert("0.0", "Y-axis")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.axis_variables,
                                command=self.set_xaxis)
        self.xaxis_dropdown.place(relx=0.9,rely=0.18)
        self.xaxis_dropdown.set("vgs")

        self.yaxis_dropdown = ctk.CTkComboBox(master=self.root,
                            values=self.axis_variables,
                            command=self.set_yaxis)
        self.yaxis_dropdown.place(relx=0.9,rely=0.23)
        self.yaxis_dropdown.set("gmoverid")
        
    def setup_entries(self):
        # length
        self.L_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.L_text.place(relx=0.85, rely=0.275)
        self.L_text.insert("0.0", "L (u):")
        self.L_text.configure(state="disabled") # READONLY after insert

        self.L_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.L_entry.place(relx=0.9,rely=0.28)
        
        # vds
        self.vds_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.vds_text.place(relx=0.85, rely=0.325)
        self.vds_text.insert("0.0", "VDS:")
        self.vds_text.configure(state="disabled") # READONLY after insert

        self.vds_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.vds_entry.place(relx=0.9,rely=0.33)
        
    def setup_checkboxes(self):
        # log scale
        self.log_scale_checkbox = ctk.CTkCheckBox(master=self.root, text="Log Scale", onvalue="on", offvalue="off")
        self.log_scale_checkbox.place(relx=0.9, rely=0.375)
        
        # single plot
        self.single_plot_checkbox = ctk.CTkCheckBox(master=self.root, text="Single Plot", onvalue="on", offvalue="off")
        self.single_plot_checkbox.place(relx=0.9, rely=0.425)
        
        # show legend
        self.legend_checkbox = ctk.CTkCheckBox(master=self.root, text="Show Legend", onvalue="on", offvalue="off")
        self.legend_checkbox.place(relx=0.9, rely=0.475)

    def run(self):
        self.load_model()
        self.root.mainloop()
        
    def set_active_model(self, value):
        self.active_model = value
        print(self.active_model)
    
    def set_active_plot(self, value):
        self.active_plot = value
        print(self.active_plot)
        
    def set_xaxis(self, value):
        self.xaxis[self.active_plot] = value
        print(self.xaxis)
    
    def set_yaxis(self, value):
        self.yaxis[self.active_plot] = value
        print(self.yaxis)
        
    def load_model(self):
        filename = "nch_full_sim.csv"
        self.model = pd.read_csv(filename)
        
    def save(self):
        print("Saving as plot.png")
        plt.savefig("plot.png")
        
    def plot_gmro(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gds" in title])
        gmro = self.model[data[0][1]] / self.model[data[1][1]]
        return gmro
    
    def plot_idw(self, length):
        search_params = [self.vds[self.active_plot], length, ":id"]
        data = [title for title in self.model.columns if all(param in title for param in search_params)]
        retval = self.model[data[1]]/(1e-6)
        return retval
    
    def plot_ft(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "cgg" in title])
        retval = self.model[data[0][1]] / (2 * np.pi * self.model[data[1][1]])
        return retval
    
    def plot_ft_gmoverid(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "cgg" in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gmoverid" in title])
        retval = self.model[data[0][1]] / (2 * np.pi * self.model[data[1][1]]) * self.model[data[2][1]]
        return retval
    
    def plot_simple(self, param, length):
        search_params = [self.vds[self.active_plot], length, param]
        data = [title for title in self.model.columns if all(param in title for param in search_params)]
        retval = self.model[data[1]]
        return retval
    
    def single_plot(self):
        # process lengths
        self.L[self.active_plot] = self.L_entry.get()
        if ':' in self.L[self.active_plot]:
            self.L[self.active_plot] = self.L[self.active_plot].split(":")
        else:
            self.L[self.active_plot] = [self.L[self.active_plot]]
        
        self.vds[self.active_plot] = "{:.2e}".format(float(self.vds_entry.get())) # convert to scientific notation
        self.log_scale[self.active_plot] = self.log_scale_checkbox.get()
        
        # fetch from dropdowns
        self.xaxis[self.active_plot] = self.xaxis_dropdown.get()
        self.yaxis[self.active_plot] = self.yaxis_dropdown.get()
        
        fig, ax = plt.subplots() # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        
        for k in range(len(self.L[self.active_plot])):
            length = "{:.2e}".format(float(self.L[self.active_plot][k]) * 1e-6)
            print(length)
            # fetch x data
            if self.xaxis[self.active_plot] == "gmro":
                x = self.plot_gmro(length)
            elif self.xaxis[self.active_plot] == "id/w":
                x = self.plot_idw(length)
            elif self.xaxis[self.active_plot] == "ft":
                x = self.plot_ft(length)
            elif self.xaxis[self.active_plot] == "ft*gmoverid":
                x = self.plot_ft_gmoverid(length)
            elif self.xaxis[self.active_plot] != "":
                x = self.plot_simple(self.xaxis[self.active_plot], length)
                
            # fetch y data
            if self.yaxis[self.active_plot] == "gmro":
                y = self.plot_gmro(length)
            elif self.yaxis[self.active_plot] == "id/w":
                y = self.plot_idw(length)
            elif self.yaxis[self.active_plot] == "ft":
                y = self.plot_ft(length)
            elif self.yaxis[self.active_plot] == "ft*gmoverid":
                y = self.plot_ft_gmoverid(length)
            elif self.yaxis[self.active_plot] != "":
                y = self.plot_simple(self.yaxis[self.active_plot], length)
            
            # check if log scale is enabled
            if self.log_scale[self.active_plot] == "on":
                ax.set_xscale("log")
                ax.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
            else:
                ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
            
            # plot
            if self.xaxis[self.active_plot] != "" and self.yaxis[self.active_plot] != "":
                ax.plot(x, y, label="L = {} m".format(length))
        if self.legend_checkbox.get() == "on":
            ax.legend()
        ax.set_xlabel(self.xaxis[self.active_plot], loc="left")
        ax.set_ylabel(self.yaxis[self.active_plot])
        ax.set_title("Plot ({})".format(self.active_plot), y=0.98)
        ax.grid()
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()


    def update_plot(self):
        # fetch user inputs
        
        if self.single_plot_checkbox.get() == "on":
            self.single_plot()
            return
        
        # process lengths
        self.L[self.active_plot] = self.L_entry.get()
        if ':' in self.L[self.active_plot]:
            self.L[self.active_plot] = self.L[self.active_plot].split(":")
        else:
            self.L[self.active_plot] = [self.L[self.active_plot]]
        
        self.vds[self.active_plot] = "{:.2e}".format(float(self.vds_entry.get())) # convert to scientific notation
        self.log_scale[self.active_plot] = self.log_scale_checkbox.get()
        
        # fetch from dropdowns
        self.xaxis[self.active_plot] = self.xaxis_dropdown.get()
        self.yaxis[self.active_plot] = self.yaxis_dropdown.get()
        
        # for ele in vars(self):
            # print(ele, getattr(self, ele))
        
        # ----------- PLOT ------------
        
        plot_columns = plot_rows = 2

        if plot_columns > 2 or plot_rows > 2:
            print("Too many plots")
            return

        fig, axs = plt.subplots(plot_rows, plot_columns) # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        fig.tight_layout(pad=2.5)

        plot = 0
        for i in range(plot_rows):
            for j in range(plot_columns):
                for k in range(len(self.L[self.active_plot])):
                    length = "{:.2e}".format(float(self.L[self.active_plot][k]) * 1e-6)
                    # fetch x data
                    if self.xaxis[self.plots[plot]] == "gmro":
                        x = self.plot_gmro(length)
                    elif self.xaxis[self.plots[plot]] == "id/w":
                        x = self.plot_idw(length)
                    elif self.xaxis[self.plots[plot]] == "ft":
                        x = self.plot_ft(length)
                    elif self.xaxis[self.plots[plot]] == "ft*gmoverid":
                        x = self.plot_ft_gmoverid(length)
                    elif self.xaxis[self.plots[plot]] != "":
                        x = self.plot_simple(self.xaxis[self.plots[plot]], length)
                        
                    # fetch y data
                    if self.yaxis[self.plots[plot]] == "gmro":
                        y = self.plot_gmro(length)
                    elif self.yaxis[self.plots[plot]] == "id/w":
                        y = self.plot_idw(length)
                    elif self.yaxis[self.plots[plot]] == "ft":
                        y = self.plot_ft(length)
                    elif self.yaxis[self.plots[plot]] == "ft*gmoverid":
                        y = self.plot_ft_gmoverid(length)
                    elif self.yaxis[self.plots[plot]] != "":
                        y = self.plot_simple(self.yaxis[self.plots[plot]], length)
                    
                    # check if log scale is enabled
                    if self.log_scale[self.plots[plot]] == "on":
                        axs[i, j].set_xscale("log")
                        axs[i, j].ticklabel_format(axis='y', style='sci', scilimits=(0,0))
                    else:
                        axs[i, j].ticklabel_format(axis='both', style='sci', scilimits=(0,0))
                    
                    # plot
                    if self.xaxis[self.plots[plot]] != "" and self.yaxis[self.plots[plot]] != "":
                        axs[i, j].plot(x, y)
                axs[i, j].set_xlabel(self.xaxis[self.plots[plot]], loc="left")
                axs[i, j].set_ylabel(self.yaxis[self.plots[plot]])
                axs[i, j].set_title("Plot ({})".format(self.plots[plot]), y=0.98)
                axs[i, j].grid()
                plot += 1
        
        # ----------- UPDATE CANVAS ------------
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()

    def quit(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":
    CTK_Window = py_analog_designer()