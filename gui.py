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
                            height =self.root.winfo_height()*0.9,
                            width  =self.root.winfo_width()*1.6,
                            fg_color="darkblue")

        self.frame.place(relx=0.025, rely=0.025)
        
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
        
        # ----------- VARIABLES ------------
        
        self.active_plot = "a"
        self.yaxis      = {"a": "gm/id",
                           "b": "gm/id",
                           "c": "gm/id",
                           "d": "gm/id"}
        self.xaxis      = {"a": "vgs",
                           "b": "vgs",
                           "c": "vgs",
                           "d": "vgs"}
        self.models = ["nch"]
        self.axis_variables = ["gm/id", "gm", "vgs"]
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
        self.log_scale  = {"a": "off",
                           "b": "off",
                           "c": "off",
                           "d": "off"}
                
        # ----------- ACTIVE PLOT DROPDOWN ------------

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.075)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                   values=self.plots,
                                   command=self.set_active_plot)
        self.xaxis_dropdown.place(relx=0.9,rely=0.08)
        self.xaxis_dropdown.set("a")
                        
        # ----------- ACTIVE MODEL DROPDOWN ------------

        self.model_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.model_text.place(relx=0.85, rely=0.125)
        self.model_text.insert("0.0", "Model:")
        self.model_text.configure(state="disabled") # READONLY after insert

        self.model_dropdown = ctk.CTkComboBox(master=self.root,
                                   values=self.models,
                                   command=self.set_active_model)
        self.model_dropdown.place(relx=0.9,rely=0.13)
        self.model_dropdown.set("nch")

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
                                   values=self.axis_variables,
                                   command=self.set_xaxis)
        self.xaxis_dropdown.place(relx=0.9,rely=0.18)
        self.xaxis_dropdown.set("vgs")

        self.yaxis_dropdown = ctk.CTkComboBox(master=self.root,
                            values=self.axis_variables,
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

        # ----------- START ------------
        self.root.mainloop()
    
    def set_log_scale(self):
        self.log_scale = self.log_scale_checkbox.get()
        print(self.log_scale)
        
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

    def update_plot(self):
        self.vds[self.active_plot] = self.vds_entry.get()
        self.L[self.active_plot] = self.L_entry.get()
        self.log_scale[self.active_plot] = self.log_scale_checkbox.get()
        
        # ----------- UPDATE CANVAS ------------
        
        for ele in vars(self):
            print(ele, getattr(self, ele))
        
        fig, axs = plt.subplots(2, 2) # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        fig.tight_layout(pad=2.5)
        
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()

    def quit(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":        
    CTK_Window = ctkApp()