import customtkinter as ctk

def login_page(root):

    def handle_login():
        email = email_entry.get()
        pwd = pwd_entry.get()
        # send that to hashing and database
        # todo: add "incorrect email or password" message if wrong

    color_text_light = "#E8E2E1"
    color_button_bg = "#F7EBEA" 
    color_button_text = "#4A3F3D"
    color_hover = "#756865"
    color_bg_left = "#93807C"
    color_bg_right = "#857471"

    root.grid_columnconfigure(0, weight=1, uniform="group1")
    root.grid_columnconfigure(1, weight=1, uniform="group1")
    root.grid_rowconfigure(0, weight=1)

    left_panel = ctk.CTkFrame(root, fg_color=color_bg_left, corner_radius=0)
    left_panel.grid(row=0, column=0, sticky="nsew")
    left_panel.grid_columnconfigure(0, weight=1)
    left_panel.grid_rowconfigure(0, weight=1)

    title = ctk.CTkLabel(
        left_panel, 
        text="BUDGET\nBUDDY", 
        font=("Arial", 80, "bold"), 
        text_color="white",
        justify="center"
    )
    title.grid(row=0, column=0)

    right_panel = ctk.CTkFrame(root, fg_color=color_bg_right, corner_radius=0)
    right_panel.grid(row=0, column=1, sticky="nsew")
    right_panel.grid_columnconfigure(0, weight=1)
    right_panel.grid_rowconfigure(0, weight=1) 
    right_panel.grid_rowconfigure(8, weight=1) 

    email_label = ctk.CTkLabel(right_panel, text="Email", font=("Helvetica", 14), text_color=color_text_light)
    email_label.grid(row=1, column=0, pady=(0, 5))  

    email_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=color_text_light, border_width=1, text_color="#FFFFFF",
        placeholder_text="john.doe@mail.com", placeholder_text_color="#9C9290"
    )
    email_entry.grid(row=2, column=0, pady=(0, 20))

    pwd_label = ctk.CTkLabel(right_panel, text="Password", font=("Arial", 14), text_color=color_text_light)
    pwd_label.grid(row=3, column=0, pady=(0, 5))

    pwd_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=color_text_light, border_width=1, text_color="#FFFFFF", show="*",
        placeholder_text="********", placeholder_text_color="#9C9290"
    )
    pwd_entry.grid(row=4, column=0, pady=(0, 35))

    login_btn = ctk.CTkButton(
        right_panel, text="Login", width=160, height=45,
        fg_color=color_button_bg, text_color=color_button_text,
        hover_color="#E5D6D5", font=("Arial", 16, "bold"), corner_radius=8,
        command=handle_login
    )
    login_btn.grid(row=5, column=0, pady=(0, 15))

    register_btn = ctk.CTkButton(
        right_panel, text="Register", fg_color="transparent",
        text_color=color_text_light, hover_color=color_hover,
        font=("Arial", 13, "underline"),
        command=lambda: root.show_page("register")
    )   
    register_btn.grid(row=7, column=0)