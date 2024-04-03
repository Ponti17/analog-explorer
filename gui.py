import pandas as pd
import customtkinter as ctk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

class ctkApp:
    def __init__(self):
        # ctk setup
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("1600x800")
        self.root.title("analog-py-designer")

        # ----------- FRAME ------------
        
        self.frame = ctk.CTkFrame(master=self.root,
                            height =self.root.winfo_height()*0.95,
                            width  =self.root.winfo_width()*1.36,
                            fg_color="darkblue")

        self.frame.place(relx=0.33, rely=0.025)
        
        # ----------- BUTTONS ------------
        
        self.button = ctk.CTkButton(master=self.root,
                                    text="Plot",
                                    width=100,
                                    height=50,
                                    command=self.update_plot)
        self.button.place(relx=0.9,rely=0.5)
        
        self.quit_button = ctk.CTkButton(master=self.root,
                                    text="Quit",
                                    width=100,
                                    height=50,
                                    command=self.quit)
        self.quit_button.place(relx=0.9,rely=0.6)
        
        self.freq = 1 #tmp
        
        self.active_plot = "plot (a)"
        self.xaxis      = {"a": "gm/id", "b": "gm/id", "c": "gm/id", "d": "gm/id"}
        self.yaxis      = {"a": "gm", "b": "gm", "c": "gm", "d": "gm"}
        self.vds        = {"a": "1", "b": "1", "c": "1", "d": "1"}
        self.L          = {"a": "1", "b": "1", "c": "1", "d": "1"}
        self.log_scale  = {"a": "off", "b": "off", "c": "off", "d": "off"}
        
        self.plot_data = {
            "a_x": "1",
            "a_y": "1",
            "b_x": "1",
            "b_y": "1",
            "c_x": "1",
            "c_y": "1",
            "d_x": "1",
            "d_y": "1",
        }
                
        # ----------- PLOT DROPDOWN ------------

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.125)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                   values=["a", "b", "c", "d"],
                                   command=self.set_active_plot)
        self.xaxis_dropdown.place(relx=0.9,rely=0.13)
        self.xaxis_dropdown.set("a")

        # ----------- X/Y AXIS DROPDOWN ------------
        
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.175)
        self.axis_text.insert("0.0", "X-axis")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.225)
        self.axis_text.insert("0.0", "Y-axis")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                   values=["gm/id", "gm", "vgs"],
                                   command=self.set_xaxis)
        self.xaxis_dropdown.place(relx=0.9,rely=0.18)
        self.xaxis_dropdown.set("gm/id")

        self.yaxis_dropdown = ctk.CTkComboBox(master=self.root,
                            values=["gm/id", "gm", "vgs"],
                            command=self.set_yaxis)
        self.yaxis_dropdown.place(relx=0.9,rely=0.23)
        self.yaxis_dropdown.set("gm/id")
        
        # ----------- L ENTRY FIELD ------------

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
        
        # ----------- VDS ENTRY FIELD ------------
        
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
        
        # ----------- LOG CHECKBOX ------------
        
        self.log_scale_checkbox = ctk.CTkCheckBox(master=self.root, text="Log Scale", command=self.set_log_scale, onvalue="on", offvalue="off")
        self.log_scale_checkbox.place(relx=0.9, rely=0.375)
        
        # ----------- PLOT READOUT ------------
        
        self.axis_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.axis_entry.place(relx=0.025,rely=0.70)
        
        self.readout_button = ctk.CTkButton(master=self.root,
                            text="Readout",
                            width=100,
                            height=50,
                            command=self.readout)
        self.readout_button.place(relx=0.025,rely=0.80)
        
        self.axis_readout = ctk.CTkTextbox(master=self.root, width=130, height=10, corner_radius=10)
        self.axis_readout.place(relx=0.025, rely=0.75)
        self.axis_readout.insert("0.0", "")
        self.axis_readout.configure(state="disabled") # READONLY after insert

        # ----------- START ------------
        self.init_plot()
        self.root.mainloop()
        
    def readout(self):
        plot_key = "a_x"  # Extracting the key from title
        X_data = self.plot_data.get(plot_key)  # Fetching X_data from dictionary
        entry_value = float(self.axis_entry.get())
        
        for key, value in X_data.items():
            print(key)
        
        # closest_value = min(X_data, key=lambda x: abs(x - entry_value))
        
        self.axis_readout.configure(state="normal")
        self.axis_readout.insert("0.0", "testtest")
        self.axis_readout.configure(state="disabled") # READONLY after insert

    def init_plot(self):
        t = np.arange(0, 3, .01)
        fig, axs = plt.subplots(2, 2) # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        fig.tight_layout(pad=2.5)
        axs[0, 0].plot(t, np.sin(2 * np.pi * t), 'tab:orange')
        axs[0, 0].set_title("Plot (a)")
        axs[0, 1].plot(t, np.sin(2 * np.pi * t), 'tab:blue')
        axs[0, 1].set_title("Plot (a)")
        axs[1, 0].plot(t, np.sin(2 * np.pi * t), 'tab:red')
        axs[1, 0].set_title("Plot (a)")
        axs[1, 1].plot(t, np.sin(2 * np.pi * t), 'tab:green')
        axs[1, 1].set_title("Plot (a)")
        
        canvas = FigureCanvasTkAgg(fig,master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0.025)
        self.root.update()
    
    def set_log_scale(self):
        self.log_scale = self.log_scale_checkbox.get()
        print(self.log_scale)
    
    def set_active_plot(self, value):
        self.active_plot = value
        self.vds_text.insert("0.0", "VDS: {0}".format(self.vds[value]))
        print(self.active_plot)
        
    def set_xaxis(self, value):
        self.xaxis = value
        print(self.xaxis)
    
    def set_yaxis(self, value):
        self.yaxis = value
        print(self.yaxis)

    def update_plot(self):
        self.vds[self.active_plot] = self.vds_entry.get()
        self.L[self.active_plot] = self.L_entry.get()
        
        # fix the factor for L if less than 1u
        if float(self.L[self.active_plot]) < 1:
            L_factor = "e-07"
            self.L = str(int(float(self.L[self.active_plot]) * 10))
        else:
            L_factor = "e-06"
        
        # ----------- LOAD DATA ------------
        
        # replace print with data path
        if self.xaxis == "gm/id":
            print("gm/id")
        elif self.xaxis == "gm":
            print("gm")
        elif self.xaxis == "vgs":
            print("vgs")
        
        if self.yaxis == "gm/id":
            print("gm/id")
        elif self.yaxis == "gm":
            print("gm")
        elif self.yaxis == "vgs":
            print("vgs")
        
        data_path = "nmos-gmid-idw-vds-test.csv"
        data = pd.read_csv(data_path)
        
        X_data = [title for title in data.columns if 'X' in title and "VDS={})".format(self.vds) in title and "L_sweep={0}{1}".format(self.L, L_factor) in title]
        Y_data = [title for title in data.columns if 'Y' in title and "VDS={}".format(self.vds) in title and "L_sweep={0}{1}".format(self.L, L_factor) in title]
        
        if self.active_plot == "plot (a)":
            self.plot_data["a_x"] = data[X_data]
            self.plot_data["a_y"] = data[Y_data]
        elif self.active_plot == "plot (b)":
            self.plot_data["b_x"] = data[X_data]
            self.plot_data["b_y"] = data[Y_data]
        elif self.active_plot == "plot (c)":
            self.plot_data["c_x"] = data[X_data]
            self.plot_data["c_y"] = data[Y_data]
        elif self.active_plot == "plot (d)":
            self.plot_data["d_x"] = data[X_data]
            self.plot_data["d_y"] = data[Y_data]
        
        t = np.arange(0, 3, .01)
        fig, axs = plt.subplots(2, 2) # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        fig.tight_layout(pad=2.5)
        
        titles = ["a", "b", "c", "d"]
        count = 0
        for i in range(2):
            for j in range(2):
                plot_key = titles[count] + "_x"  # Extracting the key from title
                X_data = self.plot_data.get(plot_key)  # Fetching X_data from dictionary
                plot_key = titles[count] + "_y"  # Extracting the key from title
                Y_data = self.plot_data.get(plot_key)  # Fetching Y_data from dictionary
                
                axs[i, j].plot(X_data, Y_data, 'tab:orange')  # Plotting data
                axs[i, j].set_title(titles[count])
                count += 1
                if self.log_scale == "on":
                    print("log scale on")
                    axs[i, j].set_xscale('log')
        
        
        canvas = FigureCanvasTkAgg(fig,master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0.025)
        self.root.update()

    def quit(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":        
    CTK_Window = ctkApp()