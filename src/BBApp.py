import customtkinter as ctk

from src.gui.landing_page import landing_page
from src.gui.login.login_page import login_page
from src.gui.login.register_page import register_page

class BBApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget Buddy")
        self.geometry("1280x720")
        ctk.set_appearance_mode("dark")
        self.configure(fg_color="#93807C") 

        landing_page(self)

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def show_page(self, page_name):

        self.clear_frame()

        pages = {
            "landing": landing_page,
            "login": login_page,
            "register": register_page
        }

        pages[page_name](self)

        


    