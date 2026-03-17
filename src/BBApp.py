import customtkinter as ctk

from src.gui.background import background

class BBApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget Buddy")
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")

        background(self)