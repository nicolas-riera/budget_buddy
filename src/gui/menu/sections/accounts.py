import customtkinter as ctk
from src.gui.color_palette import *

def render_accounts(frame, mock_accounts):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Header ─────────────────────────────────────────────────────────────
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(fill="x", padx=30, pady=(25, 10))

    ctk.CTkLabel(header_frame, text="Accounts",
                 font=("Arial", 28, "bold"), text_color=COLOR_TEXT_LIGHT).pack(side="left")

    # ── Content Area (Scrollable Accounts List) ─────────────────────────────
    list_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                             border_width=1, border_color=COLOR_BORDER)
    list_card.pack(fill="both", expand=True, padx=30, pady=(0, 20))
    
    scroll = ctk.CTkScrollableFrame(list_card, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=15, pady=15)

    for i, acc in enumerate(mock_accounts):
        row_frame = ctk.CTkFrame(scroll, fg_color="#6E5B58", corner_radius=8, height=65)
        row_frame.pack(fill="x", pady=6)
        row_frame.pack_propagate(False)
        
        # Name
        ctk.CTkLabel(row_frame, text=acc["name"], font=("Arial", 18, "bold"),
                     text_color=COLOR_TEXT_LIGHT, anchor="w").pack(side="left", padx=(15, 15))
        
        # Number
        ctk.CTkLabel(row_frame, text=acc["number"], font=("Arial", 14),
                     text_color="#C0B0AE", anchor="w").pack(side="left", padx=10)
        
        # Date
        ctk.CTkLabel(row_frame, text=f"Opened: {acc['date']}", font=("Arial", 12),
                     text_color="#C0B0AE").pack(side="left", padx=10)
                     
        # Balance
        ctk.CTkLabel(row_frame, text=acc["balance"], font=("Arial", 20, "bold"),
                     text_color="#C8F0C0", anchor="e").pack(side="right", padx=20)

    # ── Footer Buttons ─────────────────────────────────────────────────────
    footer_frame = ctk.CTkFrame(frame, fg_color="transparent")
    footer_frame.pack(fill="x", padx=30, pady=(0, 30))

    btn_create = ctk.CTkButton(
        footer_frame, text="Create Account", font=("Arial", 16, "bold"),
        fg_color="#A8D8FF", text_color="#183652", hover_color="#6BA4D8",
        height=45, corner_radius=8
    )
    btn_create.pack(side="left", expand=True, fill="x", padx=(0, 10))

    btn_delete = ctk.CTkButton(
        footer_frame, text="Delete Existing Account", font=("Arial", 16, "bold"),
        fg_color="#FF9E9E", text_color="#4A1C1C", hover_color="#E87272",
        height=45, corner_radius=8
    )
    btn_delete.pack(side="right", expand=True, fill="x", padx=(10, 0))
