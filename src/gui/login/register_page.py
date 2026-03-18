import customtkinter as ctk

from src.AuthManager import AuthManager

from src.gui.color_palette import COLOR_HOVER, COLOR_TEXT_LIGHT, COLOR_BUTTON_BG, COLOR_BUTTON_TEXT, COLOR_BG_LEFT, COLOR_BG_RIGHT, PLACEHOLDER_TEXT_COLOR

def register_page(root):

    def handle_register():
        firstname = firstname_entry.get()
        lastname = lastname_entry.get()
        email = email_entry.get()
        pwd = pwd_entry.get()
        pwd_confirm = pwd_confirm_entry.get()
        
        if pwd != pwd_confirm:
            print("Password and Password confirm are not the same") # show message pwd and pwd_confirm not same
        elif not AuthManager.check_password_strengh(pwd):
            print("Password is not secure enough") # show message Password is not secure enough
        elif not AuthManager.check_email_format(email):
            print("Invalid email") # show message Invalid email
        elif AuthManager.check_email_in_db(root, email):
            print("Email is already in db") # show message Email is already used
        else:
            account_id = AuthManager.register_user(root, firstname, lastname, email, pwd)
            if account_id:
                root.account_id = account_id[0][0]
                root.show_page("menu")

    root.grid_columnconfigure(0, weight=1, uniform="group1")
    root.grid_columnconfigure(1, weight=1, uniform="group1")
    root.grid_rowconfigure(0, weight=1)

    left_panel = ctk.CTkFrame(root, fg_color=COLOR_BG_LEFT, corner_radius=0)
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

    right_panel = ctk.CTkFrame(root, fg_color=COLOR_BG_RIGHT, corner_radius=0)
    right_panel.grid(row=0, column=1, sticky="nsew")
    right_panel.grid_columnconfigure(0, weight=1)
    right_panel.grid_rowconfigure(0, weight=1) 
    right_panel.grid_rowconfigure(11, weight=1) 

    firstname_label = ctk.CTkLabel(right_panel, text="First Name", font=("Helvetica", 14), text_color=COLOR_TEXT_LIGHT)
    firstname_label.grid(row=1, column=0, pady=(0, 5))  

    firstname_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=COLOR_TEXT_LIGHT, border_width=1, text_color="#FFFFFF",
        placeholder_text="John", placeholder_text_color=PLACEHOLDER_TEXT_COLOR
    )
    firstname_entry.grid(row=2, column=0, pady=(0, 20))

    lastname_label = ctk.CTkLabel(right_panel, text="Last Name", font=("Helvetica", 14), text_color=COLOR_TEXT_LIGHT)
    lastname_label.grid(row=3, column=0, pady=(0, 5))  

    lastname_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=COLOR_TEXT_LIGHT, border_width=1, text_color="#FFFFFF",
        placeholder_text="Doe", placeholder_text_color=PLACEHOLDER_TEXT_COLOR
    )
    lastname_entry.grid(row=4, column=0, pady=(0, 20))

    email_label = ctk.CTkLabel(right_panel, text="Email", font=("Helvetica", 14), text_color=COLOR_TEXT_LIGHT)
    email_label.grid(row=5, column=0, pady=(0, 5))  

    email_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=COLOR_TEXT_LIGHT, border_width=1, text_color="#FFFFFF",
        placeholder_text="john.doe@mail.com", placeholder_text_color=PLACEHOLDER_TEXT_COLOR
    )
    email_entry.grid(row=6, column=0, pady=(0, 20))

    pwd_label = ctk.CTkLabel(right_panel, text="Password", font=("Arial", 14), text_color=COLOR_TEXT_LIGHT)
    pwd_label.grid(row=7, column=0, pady=(0, 5))

    pwd_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=COLOR_TEXT_LIGHT, border_width=1, text_color="#FFFFFF", show="*",
        placeholder_text="********", placeholder_text_color=PLACEHOLDER_TEXT_COLOR
    )
    pwd_entry.grid(row=8, column=0, pady=(0, 10))

    pwd_confirm_entry = ctk.CTkEntry(
        right_panel, width=320, height=45, fg_color="transparent",
        border_color=COLOR_TEXT_LIGHT, border_width=1, text_color="#FFFFFF", show="*",
        placeholder_text="********", placeholder_text_color=PLACEHOLDER_TEXT_COLOR
    )
    pwd_confirm_entry.grid(row=9, column=0, pady=(0, 35))

    button_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
    button_frame.grid(row=10, column=0, pady=(0, 35))

    register_btn = ctk.CTkButton(
        button_frame, text="Register", width=160, height=45,
        fg_color=COLOR_BUTTON_BG, text_color=COLOR_BUTTON_TEXT,
        hover_color="#E5D6D5", font=("Arial", 16, "bold"), corner_radius=8,
        command=handle_register
    )
    register_btn.grid(row=0, column=1, pady=(0, 15))

    login_btn = ctk.CTkButton(
        button_frame, text="Login", fg_color="transparent",
        text_color=COLOR_TEXT_LIGHT, hover_color=COLOR_HOVER,
        font=("Arial", 13, "underline"),
        command=lambda: root.show_page("login")
    )   
    login_btn.grid(row=0, column=0)