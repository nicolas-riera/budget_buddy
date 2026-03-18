from src.gui.color_palette import *
import customtkinter as ctk
from customtkinter import CTkFont

def menu_page(root):

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 36), text_color=COLOR_TEXT_LIGHT)
    title.place(relx=0.5, rely=0.1, anchor='center')

    # ── Colors ────────────────────────────────────────────────────────────
    ACTIVE_FONT  = CTkFont(family="Arial", size=28, underline=True)
    NORMAL_FONT  = CTkFont(family="Arial", size=28, underline=False)

    # ── Nav frame ──────────────────────────────────────────────────
    nav_frame = ctk.CTkFrame(root, fg_color="transparent")
    nav_frame.place(relx=0.15, rely=0.55, anchor="center")

    # ── Content frame ──────────────────────────────────────────────
    content_frame = ctk.CTkFrame(root, width=850, height=450, corner_radius=16, fg_color=COLOR_SECTION, border_width=2, border_color=COLOR_TEXT_LIGHT)
    content_frame.place(relx=0.62, rely=0.55, anchor="center")
    content_frame.pack_propagate(False)

    content_label = ctk.CTkLabel(
        content_frame,
        text="Select a category",
        font=("Arial", 20),
        text_color=COLOR_TEXT_LIGHT,
        
    )
    content_label.pack(expand=True)

    # ── Sections ─────────────────────────────────────────────────
    sections = {
        "General":      "Budget overview\n\n• Total balance\n• Monthly summary\n• Alerts",
        "History":      "Transaction history\n\n• All past transactions\n• Date filters",
        "Transactions": "Manage transactions\n\n• Add / Edit / Delete\n• Categorization",
        "Accounts":     "My accounts\n\n• Checking account\n• Savings\n• Balances",
        "Settings":     "Settings\n\n• User profile\n• Currency\n• Notifications",
    }

    current_btn = {"ref": None}

    def select(btn, name):
        # Reset button
        if current_btn["ref"] is not None:
            current_btn["ref"].configure(font=NORMAL_FONT, text_color=COLOR_TEXT_LIGHT)
        # Active Button
        btn.configure(font=ACTIVE_FONT, text_color=COLOR_TEXT_LIGHT)
        current_btn["ref"] = btn
        # Update
        content_label.configure(text=sections[name], text_color=COLOR_TEXT_LIGHT)

    def make_btn(name, row):
        btn = ctk.CTkButton(
            nav_frame,
            text=name,
            fg_color="transparent",
            hover=False,
            width=180,
            height=60,
            font=NORMAL_FONT,
            text_color=COLOR_TEXT_LIGHT,
            anchor="center",
        )
        btn.configure(command=lambda b=btn, n=name: select(b, n))
        btn.bind("<Enter>", lambda e, b=btn: b.configure(text_color=COLOR_HOVER) if current_btn["ref"] is not b else None)
        btn.bind("<Leave>", lambda e, b=btn: b.configure(text_color=COLOR_TEXT_LIGHT)  if current_btn["ref"] is not b else None)
        btn.grid(row=row, column=0, padx=5, pady=12, sticky="w")
        return btn

    btn1 = make_btn("General",      0)
    btn2 = make_btn("History",      1)
    btn3 = make_btn("Transactions", 2)
    btn4 = make_btn("Accounts",     3)
    btn5 = make_btn("Settings",     4)

    # Select by default
    select(btn1, "General")