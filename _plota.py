import numpy as np

class plot:
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self.xaxis: str = ""
        self.yaxis: str = ""
        self.model: str = ""
        self.logx: bool = False
        self.invx: bool = False
        
        self.vdsrc: list[int] = [0] # vds input
        self.gateL: list[int] = [0] # gate length input
        
    def getaxis(self, axis: str) -> np.ndarray:
        retval = []
        if axis   == "gmro":        retval = self.get_gmro(vds, length)
        elif axis == "id/w":        retval = self.get_idw(vds, length)
        elif axis == "ft":          retval = self.get_ft(vds, length)
        elif axis == "ft*gmoverid": retval = self.get_ft_gmoverid(vds, length)
        elif axis != "":            retval = self.get_simple(axis, vds, length)
        return retval
        
    def getx(self) -> np.ndarray:
        retval = self.getaxis(self.xaxis)
        return retval
    
    def gety(self) -> np.ndarray:
        retval = self.getaxis(self.yaxis)
        return retval