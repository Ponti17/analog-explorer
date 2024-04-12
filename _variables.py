class py_designer_var:
    def init_variables(self):
        self.active_plot = "a"
        self.yaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis_title = {"a": "",
                            "b": "",
                            "c": "",
                            "d": ""}
        self.yaxis_title = {"a": "",
                            "b": "",
                            "c": "",
                            "d": ""}
        self.models = ["nch"]
        self.axis_variables = ["gmoverid", "gm", "vgs", "gds", "gmro", "id/w", "ft", "ft*gmoverid"]
        self.plots = ["a", "b", "c", "d"]
        
        # user inputs
        self.model      = {"a": "nch",
                           "b": "nch",
                           "c": "nch",
                           "d": "nch"}
        self.vds        = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.L          = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.pros_L     = {"a": "1",
                           "b": "1",
                           "c": "1",
                           "d": "1"}
        self.log_scale  = {"a": "off",
                           "b": "off",
                           "c": "off",
                           "d": "off"}