import customtkinter as ctk

from src.gui.color_palette import *

def render_history(root, frame, transactions):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Header ─────────────────────────────────────────────────────────────
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(fill="x", padx=30, pady=(25, 10))

    ctk.CTkLabel(header_frame, text="Transaction History",
                 font=("Arial", 24, "bold"), text_color=COLOR_TEXT_LIGHT).pack(side="left")

    # ── Scrollable List ────────────────────────────────────────────────────
    list_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                             border_width=1, border_color=COLOR_BORDER)
    list_card.pack(fill="both", expand=True, padx=30, pady=(0, 30))
    list_card.pack_propagate(False)

    scroll = ctk.CTkScrollableFrame(list_card, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=15, pady=15)

    for i, (label, amount, color, date) in enumerate(transactions):
        # Transaction item container
        row_frame = ctk.CTkFrame(scroll, fg_color="#6E5B58", corner_radius=8, height=45)
        row_frame.pack(fill="x", pady=4)
        row_frame.pack_propagate(False)

        # Date
        ctk.CTkLabel(row_frame, text=date, font=("Arial", 12),
                     text_color="#C0B0AE", width=80, anchor="w").pack(side="left", padx=(15, 10))
        
        # Details / Label
        ctk.CTkLabel(row_frame, text=label, font=("Arial", 14),
                     text_color=COLOR_TEXT_LIGHT, anchor="w").pack(side="left", padx=10, fill="x", expand=True)
                     
        # Amount
        ctk.CTkLabel(row_frame, text=amount, font=("Arial", 14, "bold"),
                     text_color=color, anchor="e").pack(side="right", padx=15)
