import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker
import numpy as np

class guiplot:
    def save(self):
        print("Saving as plot.png")
        plt.savefig("plot.png")
    
    # returns requested data for axis
    def get_axis(self, axis, length):
        retval = []
        if axis == "gmro":
            retval = self.get_gmro(length)
        elif axis == "id/w":
            retval = self.get_idw(length)
        elif axis == "ft":
            retval = self.get_ft(length)
        elif axis == "ft*gmoverid":
            retval = self.get_ft_gmoverid(length)
        elif axis == "1/gds":
            retval = self.get_1_gds(length)
        elif axis != "":
            retval = self.get_simple(axis, length)
        return retval
    
    def parse_input(self):
        # parse length input
        self.L[self.active_plot] = self.L_entry.get()
        if ':' in self.L[self.active_plot]:
            self.L[self.active_plot] = self.L[self.active_plot].split(":")
        else:
            self.L[self.active_plot] = [self.L[self.active_plot]]
        
        # parse vds input
        self.vds[self.active_plot] = "{:.2e}".format(float(self.vds_entry.get()))
        
        # fetch log scale checkbox
        self.log_scale[self.active_plot] = self.log_scale_checkbox.get()
        
        # fetch single plot checkbox
        if self.single_plot_checkbox.get() == "on":
            self.single_plot = True
        else:
            self.single_plot = False
        
        # fetch axis from dropdowns
        self.xaxis[self.active_plot] = self.xaxis_dropdown.get()
        self.yaxis[self.active_plot] = self.yaxis_dropdown.get()
        
    def plot(self):
        if self.single_plot:
            plot_size = {"rows": 1, "columns": 1}
        else:
            plot_size = {"rows": 2, "columns": 2}
            
        # init matplotlib figure
        fig, axs = plt.subplots(plot_size["rows"], plot_size["columns"]) # four subplots in a 2x2 grid
        
        # this is kind of retarded, but the for loop fails when there is only one plot since it is not a numpy array
        axs = np.array(axs)
        fig.set_size_inches(10*self.x_scale, 5*self.y_scale)
        fig.set_dpi(100)
        fig.tight_layout(pad=2.5)
        
        plot = 0
        for axis in axs.reshape(-1):
            for k in range(len(self.L[self.active_plot])):
                length = "{:.2e}".format(float(self.L[self.active_plot][k]) * 1e-6)
                # fetch x data
                x = self.get_axis(self.xaxis[self.plots[plot]], length)

                # fetch y data
                y = self.get_axis(self.yaxis[self.plots[plot]], length)

                # check if log scale is enabled
                if self.log_scale[self.active_plot] == "on":
                    axis.set_xscale("log")
                    locmaj = matplotlib.ticker.LogLocator(base=10,numticks=12) 
                    axis.xaxis.set_major_locator(locmaj)
                    locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=12)
                    axis.xaxis.set_minor_locator(locmin)
                    axis.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
                    axis.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
                else:
                    axis.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
                
                # plot
                if self.xaxis[self.plots[plot]] != "" and self.yaxis[self.plots[plot]] != "":
                    axis.plot(x, y, label="L = {} m".format(length))
                if self.legend_checkbox.get() == "on":
                    axis.legend()
            axis.set_xlabel(self.xaxis[self.plots[plot]], loc="left")
            axis.set_ylabel(self.yaxis[self.plots[plot]])
            axis.set_title("Plot ({})".format(self.plots[plot]), y=0.98)
            axis.grid()
            plot += 1
                
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()