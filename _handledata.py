import pandas as pd
import numpy as np

class dataHandler:
    def load_model(self, model):
        self.active_model = model
        if model == "nch":
            filename = ("nch_full_sim." + self.dataformat)
        elif model == "nch_25":
            filename = ("nch_25_full_sim." + self.dataformat)
        elif model == "pch":
            filename = ("pch_full_sim." + self.dataformat)
        elif model == "pch_25":
            filename = ("pch_25_full_sim." + self.dataformat)
        elif model == "pch_hvt":
            filename = ("pch_hvt_full_sim." + self.dataformat)
        elif model == "pch_lvt":
            filename = ("pch_lvt_full_sim." + self.dataformat)
        if "pch" in model:
            self.pmos = True
        else:
            self.pmos = False
        
        if self.dataformat == "csv":
            self.modelDF = pd.read_csv(filename)
        elif self.dataformat == "pkl":
            self.modelDF = pd.read_pickle(filename)
        else:
            print("Unsupported data format.")
            exit()
        
    def get_gmro(self, vds, length):
        search_params = [vds, length]
        data = []
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "gds" in title])
        gmro = self.modelDF[data[0][1]] / self.modelDF[data[1][1]]
        return gmro
    
    def get_idw(self, vds, length):
        search_params = [vds, length, ":id"]
        data = [title for title in self.modelDF.columns if all(param in title for param in search_params)]
        retval = self.modelDF[data[1]]/(1e-6)
        if self.pmos:
            retval = -retval
        return retval
    
    def get_ft(self, vds, length):
        search_params = [vds, length]
        data = []
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "cgg" in title])
        retval = self.modelDF[data[0][1]] / (2 * np.pi * self.modelDF[data[1][1]])
        return retval
    
    def get_ft_gmoverid(self, vds, length):
        search_params = [vds, length]
        data = []
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "gm " in title])
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "cgg" in title])
        data.append([title for title in self.modelDF.columns if all(param in title for param in search_params) and "gmoverid" in title])
        retval = self.modelDF[data[0][1]] / (2 * np.pi * self.modelDF[data[1][1]]) * self.modelDF[data[2][1]]
        return retval
    
    def get_simple(self, param, vds, length):
        param = "M0:" + param
        search_params = [vds, length, param]
        data = [title for title in self.modelDF.columns if all(param in title for param in search_params)]
        print(data)
        retval = self.modelDF[data[1]]
        return retval