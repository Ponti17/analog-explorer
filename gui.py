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
        self.root.geometry("1200x800")
        self.root.title("analog-py-designer")

        self.frame = ctk.CTkFrame(master=self.root,
                            height =self.root.winfo_height()*0.95,
                            width  =self.root.winfo_width()*1.36,
                            fg_color="darkblue")

        self.frame.place(relx=0.33, rely=0.025)
        
        self.button = ctk.CTkButton(master=self.root,
                                    text="Plot",
                                    width=300,
                                    height=50,
                                    command=self.update_plot)
        self.button.place(relx=0.025,rely=0.25)
        
        self.quit_button = ctk.CTkButton(master=self.root,
                                    text="Quit",
                                    width=300,
                                    height=50,
                                    command=self.quit)
        self.quit_button.place(relx=0.025,rely=0.5)
        
        self.freq = 1
        
        # ----------- ENTRY FIELD ------------
        my_label = ctk.CTkLabel(self.root, text="", font=("Helvetica", 24))
        my_label.pack(pady=300)

        self.my_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=50,
            width=50,
            font=("Helvetica", 18),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.my_entry.pack(pady=20)
        
        my_button = ctk.CTkButton(self.root, text="Submit", command=self.submit)
        my_button.pack(pady=10)
        
        # ----------- START ------------
        
        self.root.mainloop()
        
    def submit(self):
        self.freq = self.my_entry.get()
        self.update_plot()
        

    def update_plot(self):
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
        canvas.get_tk_widget().place(relx=0.33, rely=0.025)
        self.root.update()

    def quit(self):
        self.root.quit()
        self.root.destroy()

if __name__ == "__main__":        
    CTK_Window = ctkApp()

# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.