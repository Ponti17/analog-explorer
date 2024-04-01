import tkinter
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

        self.frame = ctk.CTkFrame(master=self.root,
                            height =self.root.winfo_height()*0.95,
                            width  =self.root.winfo_width()*1.36,
                            fg_color="darkblue")

        self.frame.place(relx=0.33, rely=0.025)
        
        self.button = ctk.CTkButton(master=self.root,
                                    text="Plot",
                                    width=100,
                                    height=50,
                                    command=self.update_plot)
        self.button.place(relx=0.9,rely=0.4)
        
        self.quit_button = ctk.CTkButton(master=self.root,
                                    text="Quit",
                                    width=100,
                                    height=50,
                                    command=self.quit)
        self.quit_button.place(relx=0.9,rely=0.5)
        
        self.freq = 1
        
        
        self.active_plot = "plot (a)"
        self.xaxis = "gm/id"
        self.yaxis = "gm"
                
        # ----------- PLOT DROPDOWN ------------

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.125)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled") # READONLY after insert

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                   values=["plot (a)", "plot (b)", "plot (c)", "plot (d)"],
                                   command=self.set_active_plot)
        self.xaxis_dropdown.place(relx=0.9,rely=0.13)
        self.xaxis_dropdown.set("plot (a)")

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

        self.my_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.my_entry.place(relx=0.9,rely=0.28)
        
        # ----------- VDS ENTRY FIELD ------------
        
        self.L_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.L_text.place(relx=0.85, rely=0.325)
        self.L_text.insert("0.0", "VDS:")
        self.L_text.configure(state="disabled") # READONLY after insert

        self.my_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.my_entry.place(relx=0.9,rely=0.33)

        # ----------- START ------------
        
        self.root.mainloop()
        
    def set_active_plot(self, value):
        self.active_plot = value
        print(self.active_plot)
        
    def set_xaxis(self, value):
        self.xaxis = value
        print(self.xaxis)
    
    def set_yaxis(self, value):
        self.yaxis = value
        print(self.yaxis)
        
    def submit(self):
        self.freq = self.my_entry.get()
        self.update_plot()

    def update_plot(self):
        print(self.active_plot)
        t = np.arange(0, 3, .01)
        fig, axs = plt.subplots(2, 2) # four subplots in a 2x2 grid
        fig.set_size_inches(10, 5)
        fig.tight_layout(pad=2.5)
    
        axs[0, 0].plot(t, 2 * np.sin(2 * np.pi * t * int(self.freq)), 'tab:orange')
        axs[0, 0].set_title("Plot (a)")
        axs[0, 1].plot(t, 2 * np.sin(2 * np.pi * t * int(self.freq)), 'tab:green')
        axs[0, 1].set_title("Plot (b)")
        axs[1, 0].plot(t, 2 * np.sin(2 * np.pi * t * int(self.freq)), 'tab:red')
        axs[1, 0].set_title("Plot (c)")
        axs[1, 1].plot(t, 2 * np.sin(2 * np.pi * t * int(self.freq)), 'tab:blue')
        axs[1, 1].set_title("Plot (d)")
        
        # fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
        canvas = FigureCanvasTkAgg(fig,master=self.root)
        canvas.draw()
        canvas.get_tk_widget().place(relx=0, rely=0.025)
        self.root.update()

    def quit(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":        
    CTK_Window = ctkApp()

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.