import pandas as pd
import numpy as np
import os

class dataHandler:    
    def load_model(self, model):
        self.active_model = model
        if model == "nch":
            filename = ("nch_full_sim." + self.dataformat)
        elif model == "nch_25":
            filename = ("nch_25_full_sim." + self.dataformat)
        elif model == "nch_hvt":
            filename = ("nch_hvt_full_sim." + self.dataformat)
        elif model == "nch_lvt":
            filename = ("nch_lvt_full_sim." + self.dataformat)
        elif model == "pch":
            filename = ("pch_full_sim." + self.dataformat)
        elif model == "pch_25":
            filename = ("pch_25_full_sim." + self.dataformat)
        elif model == "pch_hvt":
            filename = ("pch_hvt_full_sim." + self.dataformat)
        elif model == "pch_lvt":
            filename = ("pch_lvt_full_sim." + self.dataformat)
        
        filename = os.path.join(self.modeldir, filename)
        if self.dataformat == "csv":
            self.modelDF = pd.read_csv(filename)
        elif self.dataformat == "pkl":
            self.modelDF = pd.read_pickle(filename)
        else:
            print("Unsupported data format.")
            exit()
            
        # self.get_resolution()
        
    def get_resolution(self):
        # find resolution of loaded model
        titles = []
        for title in self.modelDF.columns:
            if "gmoverid" in title and "X" in title:
                titles.append(title)
        self.vds_vals = []
        self.len_vals = []
        for title in titles:
            self.vds_vals.append(float(title.split(',')[0].split('=')[1]))
            self.len_vals.append(float(title.split(',')[1].split('=')[1].split(')')[0]))
            self.vds_vals = list(set(self.vds_vals))
            self.len_vals = list(set(self.len_vals))
            self.vds_vals.sort()
            self.len_vals.sort()
            
    def get_gmoverid_mode(self, gmoverid, vds, length):
        gmid_vals = self.get_axis("gmoverid", vds, length).tolist()
        gmid_fit = gmid_vals[min(range(len(gmid_vals)), key = lambda i: abs(gmid_vals[i]-gmoverid))]
        gmid_arg = gmid_vals.index(gmid_fit)
        
        params = ["vgs", "gmro", "vdsat", "id/w", "ft"]
        res = []
        for param in params:
            data = self.get_axis(param, vds, length).tolist()
            res.append("{:.2e}".format(data[gmid_arg], 2))
        id = float(self.id_entry.get()) * 1e-9 / float(res[3])
        id = "{:.2e}".format(id, 2)
        self.gmid_text.configure(state="normal")
        self.gmid_text.delete("0.0", "end")
        self.gmid_text.insert("0.0", "gm/ID:   {0}\n     vgs:   {1}\n  gmro:   {2}\n  vdsat:   {3}\n  id/w:   {4}\n    ft:   {5}\n     w:   {6}".format(gmid_fit, res[0], res[1], res[2], res[3], res[4], id))
        self.gmid_text.configure(state="disabled")
            
        
    def fit_vds_len(self, vds, length):
        # vds = self.vds_vals[min(range(len(self.vds_vals)), key = lambda i: abs(self.vds_vals[i]-vds))]
        # length = self.len_vals[min(range(len(self.len_vals)), key = lambda i: abs(self.len_vals[i]-length))]
        return "{:.2e}".format(vds), "{:.2e}".format(length)
            
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
        retval = self.modelDF[data[1]]
        return retval