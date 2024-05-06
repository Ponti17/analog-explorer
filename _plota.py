class Plot:
    def __init__(self) -> None:
        self.reset()
        
    def reset(self) -> None:
        self.xaxis: str = ""
        self.yaxis: str = ""
        self.model: str = ""
        self.logx: int = 0
        self.invx: int = 0
        
        self.vdsrc: str = "" # vds input
        self.gateL: str = "" # gate length input
        
    def setx(self, x: str) -> None:
        self.xaxis = x
        
    def sety(self, y: str) -> None:
        self.yaxis = y
        
    def setmodel(self, m: str) -> None:
        self.model = m
    
    def setlogx(self, logx: int) -> None:
        self.logx = logx
        
    def setinvx(self, invx: int) -> None:
        self.invx = invx
        
    def setvdsrc(self, v: str) -> None:
        self.vdsrc = v
        
    def setgateL(self, g: str) -> None:
        self.gateL = g
        
    def getx(self) -> str:
        return self.xaxis
    
    def gety(self) -> str:
        return self.yaxis
    
    def getmodel(self) -> str:
        return self.model
    
    def getlogx(self) -> int:
        return self.logx
    
    def getinvx(self) -> int:
        return self.invx
    
    def getvdsrc(self) -> str:
        return self.vdsrc
    
    def getgateL(self) -> str:
        return self.gateL