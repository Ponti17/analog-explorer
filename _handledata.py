import pandas as pd
import numpy as np
import numpy.typing as npt
import os

class DataHandler:
    def __init__(self) -> None:
        self.df: pd.DataFrame = pd.DataFrame()
        
    def load(self, model: str) -> None:
        modeldir  =     "models"
        modellist =    {"nch":        "nch_full_sim",
                        "nch_25":     "nch_25_full_sim",
                        "nch_hvt":    "nch_hvt_full_sim",
                        "nch_lvt":    "nch_lvt_full_sim",
                        "pch":        "pch_full_sim",
                        "pch_25":     "pch_25_full_sim",
                        "pch_hvt":    "pch_hvt_full_sim",
                        "pch_lvt":    "pch_lvt_full_sim"}

        try:
            file = os.path.join(modeldir, modellist[model] + ".pkl")
            self.df = pd.read_pickle(file)
        except:
            print("Invalid model or model not found: {}".format(model))
            exit()

    def getAxis(self, ax: str, vdsrc: str, gateL: str) -> npt.NDArray[np.float32]:
        match ax:
            case "gmro":
                return self.__get_gmro(vdsrc, gateL)
            case _:
                return self.__get_simple(ax, vdsrc, gateL)
    
    def __get_simple(self, ax: str, vdsrc: str, gateL: str) -> npt.NDArray[np.float32]:
        regex_str: str = "(?=.*M0:{})(?=.*vds={})(?=.*length={})(?=.*Y)".format(ax, vdsrc, gateL).replace("+", "\\+")
        return self.df.filter(regex=regex_str).to_numpy()
    
    def __get_gmro(self, vdsrc: str, gateL: str) -> npt.NDArray[np.float32]:
        gm:  npt.NDArray[np.float32] = self.__get_simple("gm ", vdsrc, gateL)
        gds: npt.NDArray[np.float32] = self.__get_simple("gds", vdsrc, gateL)
        return gm / gds

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