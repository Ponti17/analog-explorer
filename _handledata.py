import pandas as pd
import numpy as np

class dataHandler:
    def load_model(self):
        if self.active_model == "nch":
            filename = ("nch_full_sim." + self.dataformat)
        elif self.active_model == "pch":
            filename = ("pch_full_sim." + self.dataformat)
        elif self.active_model == "pch_25":
            filename = ("pch_25_full_sim." + self.dataformat)
        if "pch" in self.active_model:
            self.pmos = True
        else:
            self.pmos = False
        print("Loading model... {}".format(filename))
        
        if self.dataformat == "csv":
            self.model = pd.read_csv(filename)
        elif self.dataformat == "pkl":
            self.model = pd.read_pickle(filename)
        else:
            print("Unsupported data format.")
            exit()
        print("Done.")
        
    def get_gmro(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gds" in title])
        gmro = self.model[data[0][1]] / self.model[data[1][1]]
        return gmro
    
    def get_idw(self, length):
        search_params = [self.vds[self.active_plot], length, ":id"]
        data = [title for title in self.model.columns if all(param in title for param in search_params)]
        retval = self.model[data[1]]/(1e-6)
        if self.pmos:
            retval = -retval
        return retval
    
    def get_ft(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "cgg" in title])
        retval = self.model[data[0][1]] / (2 * np.pi * self.model[data[1][1]])
        return retval
    
    def get_ft_gmoverid(self, length):
        search_params = [self.vds[self.active_plot], length]
        data = []
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "cgg" in title])
        data.append([title for title in self.model.columns if all(param in title for param in search_params) and "gmoverid" in title])
        retval = self.model[data[0][1]] / (2 * np.pi * self.model[data[1][1]]) * self.model[data[2][1]]
        return retval
    
    def get_1_gds(self, length):
        param = "M0:" + "gds"
        search_params = [self.vds[self.active_plot], length]
        data = [title for title in self.model.columns if all(param in title for param in search_params)]
        retval = self.model[data[1]]
        return 1/retval
    
    def get_simple(self, param, length):
        param = "M0:" + param
        search_params = [self.vds[self.active_plot], length, param]
        data = [title for title in self.model.columns if all(param in title for param in search_params)]
        retval = self.model[data[1]]
        return retval