import customtkinter as ctk

def menu_page(root):

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 36))
    title.place(relx=0.5, rely=0.1, anchor='center')

    nav_frame = ctk.CTkFrame(root, fg_color="transparent")
    nav_frame.place(relx=0.22, rely=0.55, anchor="center")

    nav_frame.grid_columnconfigure((0, 1), weight=1, uniform="nav")
    nav_frame.grid_rowconfigure((0, 1), weight=1, uniform="nav")

    HOVER_COLOR = "#AAAAAA"
    TEXT_COLOR  = "white"

    def add_hover(btn):
        btn.bind("<Enter>", lambda e: btn.configure(text_color=HOVER_COLOR))
        btn.bind("<Leave>", lambda e: btn.configure(text_color=TEXT_COLOR))

    btn1 = ctk.CTkButton(nav_frame, text="General", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 24), text_color=TEXT_COLOR)
    btn1.grid(row=0, column=0, padx=5, pady=0)
    btn2 = ctk.CTkButton(nav_frame, text="History", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 24), text_color=TEXT_COLOR)
    btn2.grid(row=1, column=0, padx=5, pady=0)
    btn3 = ctk.CTkButton(nav_frame, text="Transactions", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 24), text_color=TEXT_COLOR)
    btn3.grid(row=2, column=0, padx=5, pady=0)
    btn4 = ctk.CTkButton(nav_frame, text="Accounts", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 24), text_color=TEXT_COLOR)
    btn4.grid(row=3, column=0, padx=5, pady=0)
    btn5 = ctk.CTkButton(nav_frame, text="Settings", fg_color="transparent", hover=False, width=150, height=80, font=("Arial", 24), text_color=TEXT_COLOR)
    btn5.grid(row=4, column=0, padx=5, pady=0)

    for btn in [btn1, btn2, btn3, btn4, btn5]:
        add_hover(btn)