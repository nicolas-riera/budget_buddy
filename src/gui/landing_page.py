import customtkinter as ctk

from src.gui.color_palette import COLOR_BUTTON_LANDING, COLOR_HOVER

def landing_page(root):

    root.clear_frame()

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 65))
    title.place(relx=0.5, rely=0.2, anchor='center')

    button_frame = ctk.CTkFrame(root, fg_color="transparent")
    button_frame.place(relx=0.5, rely=0.55, anchor="center")

    login_button = ctk.CTkButton(
        button_frame,
        text="LOGIN",
        font=("Arial", 20),
        fg_color=COLOR_BUTTON_LANDING,
        hover_color=COLOR_HOVER,
        width=250,
        height=70,
        command=lambda: root.show_page("login")
    )
    login_button.pack(pady=(0, 40))  

    register_button = ctk.CTkButton(
        button_frame,
        text="REGISTER",
        font=("Arial", 20),
        fg_color=COLOR_BUTTON_LANDING,
        hover_color=COLOR_HOVER,
        width=250,
        height=70,
        command=lambda:root.show_page("register")
    )
    register_button.pack()