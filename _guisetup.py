import customtkinter as ctk

class gui:
    def setup_frame(self):
        self.frame = ctk.CTkFrame(master=self.root,
                            height =self.root.winfo_height()*0.9,
                            width  =self.root.winfo_width()*1.6,
                            fg_color="darkblue")
        self.frame.place(relx=0.025, rely=0.025)