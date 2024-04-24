import customtkinter as ctk

class gui:
    def setup_frame(self):
        self.frame = ctk.CTkFrame(master=self.root, height =self.root.winfo_height()*0.9,
                                width=self.root.winfo_width()*1.6, fg_color="darkblue")
        self.frame.place(relx=0.025, rely=0.025)
        
    def setup_buttons(self):
        self.button = ctk.CTkButton(master=self.root, text="Plot", width=100, height=50,
                                        command=self.new_plot)
        self.button.place(relx=0.9,rely=0.65)
        
        self.save_button = ctk.CTkButton(master=self.root, text="Save Fig", width=100, height=50,
                                        command=self.save)
        self.save_button.place(relx=0.9,rely=0.75)
        
        self.quit_button = ctk.CTkButton(master=self.root, text="Quit", width=100, height=50,
                                        command=self.quit)
        self.quit_button.place(relx=0.9,rely=0.85)
        
    def setup_textboxes(self):
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.075)
        self.axis_text.insert("0.0", "Plot:")
        self.axis_text.configure(state="disabled")
        
        self.model_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.model_text.place(relx=0.85, rely=0.125)
        self.model_text.insert("0.0", "Model:")
        self.model_text.configure(state="disabled")
        
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.175)
        self.axis_text.insert("0.0", "X-axis")
        self.axis_text.configure(state="disabled")
        
        self.axis_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.axis_text.place(relx=0.85, rely=0.225)
        self.axis_text.insert("0.0", "Y-axis")
        self.axis_text.configure(state="disabled")
        
        self.L_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.L_text.place(relx=0.85, rely=0.275)
        self.L_text.insert("0.0", "L (u):")
        self.L_text.configure(state="disabled")
        
        self.vds_text = ctk.CTkTextbox(master=self.root, width=60, height=10, corner_radius=10)
        self.vds_text.place(relx=0.85, rely=0.325)
        self.vds_text.insert("0.0", "VDS:")
        self.vds_text.configure(state="disabled")
        
        # For gm/ID mode
        self.gmid_text = ctk.CTkTextbox(master=self.root, width=960, height=240, corner_radius=10)
        self.gmid_text.place(relx=0.025, rely=0.675)
        self.gmid_text.insert("0.0", "gm/ID:   {0}\n     vgs:   {1}\n  gmro:   {2}\n  vdsat:   {3}".format("0", "0", "0", "0"))
        self.gmid_text.configure(state="disabled")
        
        
    def setup_dropdowns(self):
        self.active_plot_dropdown = ctk.CTkComboBox(master=self.root, values=self.plots)
        self.active_plot_dropdown.place(relx=0.9,rely=0.08)
        self.active_plot_dropdown.set("a")

        self.model_dropdown = ctk.CTkComboBox(master=self.root, values=self.models)
        self.model_dropdown.place(relx=0.9,rely=0.13)
        self.model_dropdown.set("nch")

        self.xaxis_dropdown = ctk.CTkComboBox(master=self.root, values=self.axis_variables)
        self.xaxis_dropdown.place(relx=0.9,rely=0.18)
        self.xaxis_dropdown.set("vgs")

        self.yaxis_dropdown = ctk.CTkComboBox(master=self.root, values=self.axis_variables)
        self.yaxis_dropdown.place(relx=0.9,rely=0.23)
        self.yaxis_dropdown.set("gmoverid")
        
    def setup_entries(self):
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
        
        
        self.gmid_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.gmid_entry.place(relx=0.65,rely=0.70)
        
        self.id_entry = ctk.CTkEntry(self.root, 
            placeholder_text="",
            height=30,
            width=130,
            font=("Helvetica", 12),
            corner_radius=10,
            text_color="black",
            fg_color=("darkblue","white"),  # outer, inner
            state="normal",
        )
        self.id_entry.place(relx=0.65,rely=0.75)
        
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
        
        # gmoverid mode
        self.gmoverid_checkbox = ctk.CTkCheckBox(master=self.root, text="gm/ID Mode", onvalue="on", offvalue="off")
        self.gmoverid_checkbox.place(relx=0.9, rely=0.575)