import customtkinter as ctk

from src.gui.login_page import login_page
from src.gui.clear_frame import clear_frame

def landing_page(root):

    clear_frame(root)

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 65))
    title.place(relx=0.5, rely=0.2, anchor='center')

    button_frame = ctk.CTkFrame(root, fg_color="transparent")
    button_frame.place(relx=0.5, rely=0.55, anchor="center")

    login_button = ctk.CTkButton(
        button_frame,
        text="LOGIN",
        font=("Arial", 20),
        fg_color="#645552",
        hover_color="#756865",
        width=250,
        height=70,
        command=lambda:login_page(root)
    )
    login_button.pack(pady=(0, 40))  

    register_button = ctk.CTkButton(
        button_frame,
        text="REGISTER",
        font=("Arial", 20),
        fg_color="#645552",
        hover_color="#756865",
        width=250,
        height=70,
    )
    register_button.pack()