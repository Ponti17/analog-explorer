import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.ticker
import numpy as np

class guiplot:
    def save(self):
        print("Saving as plot.png")
        plt.savefig("plot.png")
    
    # returns requested data for axis
    def get_axis(self, axis, vds, length):
        retval = []
        if axis   == "gmro":        retval = self.get_gmro(vds, length)
        elif axis == "id/w":        retval = self.get_idw(vds, length)
        elif axis == "ft":          retval = self.get_ft(vds, length)
        elif axis == "ft*gmoverid": retval = self.get_ft_gmoverid(vds, length)
        elif axis != "":            retval = self.get_simple(axis, vds, length)
        return retval
    
    def parse_input(self):
        # get active plot
        self.active_plot = self.active_plot_dropdown.get()
        
        # parse length input
        self.L[self.active_plot] = self.L_entry.get()
        if ':' in self.L[self.active_plot]:
            self.L[self.active_plot] = self.L[self.active_plot].split(":")
        else:
            self.L[self.active_plot] = [self.L[self.active_plot]]
        
        # parse vds input
        self.vds[self.active_plot] = self.vds_entry.get()
        if ':' in self.vds[self.active_plot]:
            self.vds[self.active_plot] = self.vds[self.active_plot].split(":")
        else:
            self.vds[self.active_plot] = [self.vds[self.active_plot]]
        
        # active model
        self.model[self.active_plot] = self.model_dropdown.get()
        
        # fetch log scale checkbox
        self.log_scale[self.active_plot] = self.log_scale_checkbox.get()
        
        # fetch invert x checkbox
        self.invert_x[self.active_plot] = self.invert_x_checkbox.get()
        
        # fetch single plot checkbox
        if self.single_plot_checkbox.get() == "on": self.single_plot = True
        else:                                       self.single_plot = False
        
        # fetch axis from dropdowns
        self.xaxis[self.active_plot] = self.xaxis_dropdown.get()
        self.yaxis[self.active_plot] = self.yaxis_dropdown.get()
        
        # gmoverid mode
        if self.gmoverid_checkbox.get() == "on": self.gmoverid_mode = True
        else:                                    self.gmoverid_mode = False
        
        if self.gmoverid_mode:
            self.yaxis[self.active_plot] = "gmoverid"
            self.single_plot = True
            
        
    def plot(self):
        if self.single_plot:    plot_size = {"rows": 1, "columns": 1}
        else:                   plot_size = {"rows": 2, "columns": 2}
            
        # init matplotlib figure
        fig, axs = plt.subplots(plot_size["rows"], plot_size["columns"])
        
        # this is kind of retarded, but the for loop fails when there is only one plot since it is not a numpy array
        axs = np.array(axs)
        fig.set_size_inches(10*self.x_scale, 5*self.y_scale)
        fig.set_dpi(100)
        fig.tight_layout(pad=2.5)
        
        plot = 0
        for axis in axs.reshape(-1):
            for i in range(len(self.L[self.active_plot])):
                for j in range(len(self.vds[self.active_plot])):
                    length = float(self.L[self.active_plot][i]) * 1e-6
                    vds = float(self.vds[self.active_plot][j])
                    
                    # load model
                    if self.active_model != self.model[self.plots[plot]]:
                        self.load_model(self.model[self.plots[plot]])
                    
                    vds, length = self.fit_vds_len(vds, length)
                    
                    # fetch x data
                    x = self.get_axis(self.xaxis[self.plots[plot]], vds, length)

                    # fetch y data
                    y = self.get_axis(self.yaxis[self.plots[plot]], vds, length)
                    
                    if len(x) == 0 or len(y) == 0: continue
                    
                    if self.gmoverid_mode:
                        gmoverid = float(self.gmid_entry.get())
                        self.get_gmoverid_mode(gmoverid, vds, length)
                        minx = min(x.tolist())
                        maxx = max(x.tolist())
                        axis.hlines(gmoverid, minx, maxx, colors='r', linestyles='dashed')
                        
                    
                    if self.invert_x[self.active_plot] == "on": x = (-1)*x

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
                        length_title = length.split("e")[0]
                        vds_title = np.round(float(vds.split("e")[0]) * 10 ** float(vds.split("e")[1]), 1)
                        axis.plot(x, y, label="L = {0}u, vds = {1}V".format(length_title, vds_title))
                    if self.legend_checkbox.get() == "on":
                        axis.legend()
            axis.set_xlabel(self.xaxis[self.plots[plot]], loc="left")
            axis.set_ylabel(self.yaxis[self.plots[plot]])
            axis.set_title("{0}: {1} vs {2}".format(self.active_model, self.xaxis[self.plots[plot]], self.yaxis[self.plots[plot]]))
            axis.grid()
            plot += 1
                
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()

        # figures have fixed size so they are equal when saved
        canvas.get_tk_widget().place(relx=0.025, rely=0.025)
        self.root.update()