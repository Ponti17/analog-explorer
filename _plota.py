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
        
    def setx(self, x: str) -> None:
        self.xaxis = x
        
    def sety(self, y: str) -> None:
        self.yaxis = y
        
    def setmodel(self, m: str) -> None:
        self.model = m
    
    def setlogx(self, logx: bool) -> None:
        self.logx = logx
        
    def setinvx(self, invx: bool) -> None:
        self.invx = invx
        
    def setvdsrc(self, v: list[int]) -> None:
        self.vdsrc = v
        
    def setgateL(self, g: list[int]) -> None:
        self.gateL = g
        
    def getx(self) -> str:
        return self.xaxis
    
    def gety(self) -> str:
        return self.yaxis
    
    def getmodel(self) -> str:
        return self.model
    
    def getlogx(self) -> bool:
        return self.logx
    
    def getinvx(self) -> bool:
        return self.invx
    
    def getvdsrc(self) -> list[int]:
        return self.vdsrc
    
    def getgateL(self) -> list[int]:
        return self.gateL