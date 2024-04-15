import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.ticker

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
        fig.set_size_inches(10*self.x_scale, 5*self.y_scale)
        fig.set_dpi(100)
        fig.tight_layout(pad=2.5)
        
        plot = 0
        for i in range(plot_size["rows"]):
            for j in range(plot_size["columns"]):
                for k in range(len(self.L[self.active_plot])):
                    length = "{:.2e}".format(float(self.L[self.active_plot][k]) * 1e-6)
                    # fetch x data
                    x = self.get_axis(self.xaxis[self.plots[plot]], length)

                    # fetch y data
                    y = self.get_axis(self.yaxis[self.plots[plot]], length)

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
                
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()