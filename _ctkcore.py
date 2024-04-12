import customtkinter as ctk

class ctk_core:
    def init_ctk(self):
        ctk.set_appearance_mode("dark")
        self.root = ctk.CTk()
        self.root.geometry("1600x800")
        self.root.title("analog-py-designer")
        
    def ctk_run(self):
        self.load_model()
        self.root.mainloop()
        
    def quit(self):
        self.root.quit()
        self.root.destroy()