class py_designer_var:
    def init_variables(self):
        # stores possible values from model
        self.vds_vals = []
        self.len_vals = []
        
        # scales plot depending on resolution
        self.x_scale = 1.0
        self.y_scale = 1.0
        
        # stores app settings
        self.dataformat = ""
        self.modeldir = ""
        
        # stores plot settings
        self.single_plot = False
        self.active_plot = "a"
        
        # possible values for dropdowns
        self.models         = ["nch", "nch_25", "nch_hvt", "nch_lvt", "pch", "pch_25", "pch_hvt", "pch_lvt"]
        self.axis_variables = ["vgs", "gmoverid", "gmro", "id/w", "ft", "vdsat", "ft*gmoverid", "gm", "id "]
        self.plots = ["a", "b", "c", "d"]
        
        # plot settings for each plot
        self.active_model = ""
        self.modelDF    = 0
        self.gmoverid_mode   = False
        self.yaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
        self.xaxis      = {"a": "",
                           "b": "",
                           "c": "",
                           "d": ""}
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
        self.invert_x   = {"a": "off",
                           "b": "off",
                           "c": "off",
                           "d": "off"}
        