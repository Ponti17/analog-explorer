class py_designer_var:
    def init_variables(self):
        self.x_scale = 1.0
        self.y_scale = 1.0
        self.dataformat = "csv"
        self.pmos = True
        self.single_plot = False
        self.active_model = "nch"
        self.active_plot = "a"
        self.yaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.models = ["nch", "pch", "pch_25", "pch_hvt"]
        self.axis_variables = ["vgs", "gmoverid", "gmro", "id/w", "ft", "vdsat", "ft*gmoverid", "gm", "id "]
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