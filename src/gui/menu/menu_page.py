from src.gui.color_palette import *
import customtkinter as ctk
from customtkinter import CTkFont

from src.gui.menu.sections.sections import SECTIONS
from src.gui.menu.refresh_section import setup_refresh, refresh_section

def menu_page(root):

    title = ctk.CTkLabel(root, text="BUDGET BUDDY", font=("Arial", 36), text_color=COLOR_TEXT_LIGHT)
    title.place(relx=0.5, rely=0.1, anchor='center')

    # ── Fonts ──────────────────────────────────────────────────────────────
    ACTIVE_FONT = CTkFont(family="Arial", size=28, underline=True)
    NORMAL_FONT = CTkFont(family="Arial", size=28, underline=False)

    # ── Nav frame ──────────────────────────────────────────────────────────
    nav_frame = ctk.CTkFrame(root, fg_color="transparent")
    nav_frame.place(relx=0.15, rely=0.55, anchor="center")

    # ── Content frames (Cache) ─────────────────────────────────────────────
    # We create one 850x450 frame per section, all with the rounded corners and borders.
    section_frames = {}
    for section_name, render_func in SECTIONS.items():
        f = ctk.CTkFrame(
            root, width=850, height=450,
            corner_radius=16,
            fg_color=COLOR_SECTION,
            border_width=2,
            border_color=COLOR_TEXT_LIGHT,
        )
        # We place ALL frames at the exact same position right from the start
        f.place(relx=0.62, rely=0.55, anchor="center")
        f.pack_propagate(False)
        f.grid_propagate(False)
        render_func(root, f)
        section_frames[section_name] = f
    setup_refresh(SECTIONS, section_frames)

    # ── Section selection ──────────────────────────────────────────────────

    current_btn = {"ref": None}

    def select(btn, name):
        # Reset previous button
        if current_btn["ref"] is not None:
            current_btn["ref"].configure(font=NORMAL_FONT, text_color=COLOR_TEXT_LIGHT)
        # Active selected button
        btn.configure(font=ACTIVE_FONT, text_color=COLOR_TEXT_LIGHT)
        current_btn["ref"] = btn
        
        refresh_section(root, name)      

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
        btn.bind("<Leave>", lambda e, b=btn: b.configure(text_color=COLOR_TEXT_LIGHT) if current_btn["ref"] is not b else None)
        btn.grid(row=row, column=0, padx=5, pady=12, sticky="w")
        return btn

    btn1 = make_btn("General",      0)
    btn2 = make_btn("History",      1)
    btn3 = make_btn("Transactions", 2)
    btn4 = make_btn("Accounts",     3)
    btn5 = make_btn("Settings",     4)

    # Default selection
    select(btn1, "General")