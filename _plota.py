class plot:
    def __init__(self) -> None:
        self.xaxis: str = ""
        self.yaxis: str = ""
        self.model: str = ""
        self.logx: bool = False
        self.invx: bool = False
        
        # string types to allow for multiple values delimited by :
        self.vdsrc: str = 0 # vds input
        self.gateL: str = 0 # gate length input