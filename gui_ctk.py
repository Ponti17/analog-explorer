import customtkinter as ctk

class ctk_setup:
    def init_ctk(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("1600x800")
        self.root.title("analog-py-designer")