import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 

file_path = "nmos-idw-gmid.csv"
data = pd.read_csv(file_path)

# set theme and figure size
sns.set_theme(style="darkgrid", palette='tab10', rc={'figure.figsize':(15,6)})

def plot():
    fig, ax = plt.subplots()

    X_data = [title for title in data.columns if 'X' in title]
    Y_data = [title for title in data.columns if 'Y' in title]

    sns.lineplot(x=X_data[0], y=Y_data[0], data=data, ax=ax)

    plt.xscale('log')
    plt.title('$g_m/I_D$ Versus $I_N$')
    plt.xlabel('Reference Current $I_N = I_D/W$')
    plt.ylabel('$g_m/I_D$')

    canvas = FigureCanvasTkAgg(fig, 
                               master = window)   
    canvas.draw() 
  
    # placing the canvas on the Tkinter window 
    canvas.get_tk_widget().pack() 
  
    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                   window) 
    toolbar.update() 
  
    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 

window = Tk()

window.title("NMOS IDW GMID")

window.geometry('1200x800')

# button that displays the plot 
plot_button = Button(master = window,  
                     command = plot, 
                     height = 2,  
                     width = 10, 
                     text = "Plot") 

# place the button  
# in main window 
plot_button.pack() 
  
# run the gui 
window.mainloop() 