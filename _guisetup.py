import customtkinter as ctk

class gui:
    def setup_frame(self):
        self.frame = ctk.CTkFrame(master=self.root, height =self.root.winfo_height()*0.9,
                                width=self.root.winfo_width()*1.6, fg_color="darkblue")
        self.frame.place(relx=0.025, rely=0.025)
        
    def setup_buttons(self):
        self.button = ctk.CTkButton(master=self.root, text="Plot", width=100, height=50,
                                        command=self.new_plot)
        self.button.place(relx=0.9,rely=0.6)
        
        self.save_button = ctk.CTkButton(master=self.root, text="Save Fig", width=100, height=50,
                                        command=self.save)
        self.save_button.place(relx=0.8,rely=0.6)
        
        self.load_button = ctk.CTkButton(master=self.root, text="Load Model", width=100, height=50,
                                        command=self.load_model)
        self.load_button.place(relx=0.8,rely=0.7)
        
        self.quit_button = ctk.CTkButton(master=self.root, text="Quit", width=100, height=50,
                                        command=self.quit)
        self.quit_button.place(relx=0.9,rely=0.7)
        
    def setup_dropdowns(self):
        # active plot
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.075)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled")

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.plots,
                                command=self.set_active_plot)
        self.xaxis_dropdown.place(relx=0.9,rely=0.08)
        self.xaxis_dropdown.set("a")
                        
        # active model
        self.model_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.model_text.place(relx=0.85, rely=0.125)
        self.model_text.insert("0.0", "Model:")
        self.model_text.configure(state="disabled")

        self.model_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.models)
        self.model_dropdown.place(relx=0.9,rely=0.13)
        self.model_dropdown.set("nch")

        # axis dropdowns
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.175)
        self.axis_text.insert("0.0", "X-axis")
        self.axis_text.configure(state="disabled")

        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.225)
        self.axis_text.insert("0.0", "Y-axis")
        self.axis_text.configure(state="disabled")

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root,
                                values=self.axis_variables,
                                command=self.set_xaxis)
        self.xaxis_dropdown.place(relx=0.9,rely=0.18)
        self.xaxis_dropdown.set("vgs")

        self.yaxis_dropdown = ctk.CTkComboBox(master=self.root,
                            values=self.axis_variables,
                            command=self.set_yaxis)
        self.yaxis_dropdown.place(relx=0.9,rely=0.23)
        self.yaxis_dropdown.set("gmoverid")
        
    def setup_entries(self):
        # length
        self.L_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.L_text.place(relx=0.85, rely=0.275)
        self.L_text.insert("0.0", "L (u):")
        self.L_text.configure(state="disabled") # READONLY after insert

        self.L_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.L_entry.place(relx=0.9,rely=0.28)
        
        # vds
        self.vds_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.vds_text.place(relx=0.85, rely=0.325)
        self.vds_text.insert("0.0", "VDS:")
        self.vds_text.configure(state="disabled") # READONLY after insert

        self.vds_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.vds_entry.place(relx=0.9,rely=0.33)
        
    def setup_checkboxes(self):
        # log scale
        self.log_scale_checkbox = ctk.CTkCheckBox(master=self.root, text="Log Scale", onvalue="on", offvalue="off")
        self.log_scale_checkbox.place(relx=0.9, rely=0.375)
        
        # single plot
        self.single_plot_checkbox = ctk.CTkCheckBox(master=self.root, text="Single Plot", onvalue="on", offvalue="off")
        self.single_plot_checkbox.place(relx=0.9, rely=0.425)
        
        # show legend
        self.legend_checkbox = ctk.CTkCheckBox(master=self.root, text="Show Legend", onvalue="on", offvalue="off")
        self.legend_checkbox.place(relx=0.9, rely=0.475)
        
        # invert x axis, needed for pmos plots
        self.invert_x_checkbox = ctk.CTkCheckBox(master=self.root, text="Invert x", onvalue="on", offvalue="off")
        self.invert_x_checkbox.place(relx=0.9, rely=0.525)