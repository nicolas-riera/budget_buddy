import customtkinter as ctk

def menu_page(root):

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 36))
    title.place(relx=0.5, rely=0.1, anchor='center')

    button_frame = ctk.CTkFrame(root, fg_color="transparent")
    button_frame.place(relx=0.5, rely=0.55, anchor="center")

    button_frame.grid_columnconfigure((0, 1), weight=1, uniform="nav")
    button_frame.grid_rowconfigure((0, 1), weight=1, uniform="nav")

    btn1 = ctk.CTkButton(button_frame, text="General", fg_color="transparent", hover=20, width=150, height=80, font=("Arial", 20))
    btn1.grid(row=0, column=0, padx=10, pady=10)
    btn2 = ctk.CTkButton(button_frame, text="History", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 20))
    btn2.grid(row=1, column=0, padx=10, pady=10)
    btn3 = ctk.CTkButton(button_frame, text="Transactions", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 20))
    btn3.grid(row=2, column=0, padx=10, pady=10)
    btn4 = ctk.CTkButton(button_frame, text="Accounts", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 20))
    btn4.grid(row=3, column=0, padx=10, pady=10)
    btn5 = ctk.CTkButton(button_frame, text="Settings", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 20))
    btn5.grid(row=3, column=0, padx=10, pady=10)