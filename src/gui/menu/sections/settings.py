import customtkinter as ctk

from src.gui.color_palette import *
from src.FinanceManager import FinanceManager

def render_settings(root, frame):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Header ─────────────────────────────────────────────────────────────
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(fill="x", padx=30, pady=(25, 10))

    ctk.CTkLabel(header_frame, text="Settings",
                 font=("Arial", 28, "bold"), text_color=COLOR_TEXT_LIGHT).pack(side="left")

    # ── Content Area (User Profile Card) ───────────────────────────────────
    profile_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                                border_width=1, border_color=COLOR_BORDER)
    profile_card.pack(fill="both", expand=True, padx=30, pady=(0, 20))

    # Inner container to center everything
    info_container = ctk.CTkFrame(profile_card, fg_color="transparent")
    info_container.place(relx=0.5, rely=0.45, anchor="center")

    # Avatar placeholder
    avatar_label = ctk.CTkLabel(info_container, text="👤", font=("Arial", 80))
    avatar_label.pack(pady=(0, 20))

    # Name
    ctk.CTkLabel(info_container, text=FinanceManager.get_user_name(root), font=("Arial", 24, "bold"),
                 text_color=COLOR_TEXT_LIGHT).pack(pady=5)
    
    # Email
    ctk.CTkLabel(info_container, text=FinanceManager.get_user_email(root), font=("Arial", 16),
                 text_color="#C0B0AE").pack(pady=5)

    # Number of accounts
    accounts_label = ctk.CTkLabel(info_container, text=f"Bank Accounts: {FinanceManager.get_user_accounts_count(root)}", 
                                  font=("Arial", 16, "bold"), text_color="#A8D8FF")
    accounts_label.pack(pady=15)

    # ── Footer Buttons ─────────────────────────────────────────────────────
    footer_frame = ctk.CTkFrame(frame, fg_color="transparent")
    footer_frame.pack(fill="x", padx=30, pady=(0, 30))

    btn_disconnect = ctk.CTkButton(
        footer_frame, text="Disconnect", font=("Arial", 16, "bold"),
        fg_color="#A8D8FF", text_color="#183652", hover_color="#6BA4D8",
        height=45, corner_radius=8,
        command=lambda: FinanceManager.disconnect_user(root)
    )
    btn_disconnect.pack(side="left", expand=True, fill="x", padx=(0, 10))

    btn_delete = ctk.CTkButton(
        footer_frame, text="Delete Account", font=("Arial", 16, "bold"),
        fg_color="#FF9E9E", text_color="#4A1C1C", hover_color="#E87272",
        height=45, corner_radius=8,
        command=lambda: FinanceManager.delete_user(root)
    )
    btn_delete.pack(side="right", expand=True, fill="x", padx=(10, 0))
