import customtkinter as ctk
from src.gui.color_palette import *


def render_general(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame, text="• Total balance", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Monthly summary", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Alerts", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)


def render_history(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame, text="• All past transactions", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Date filters", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)


def render_transactions(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame, text="• Add / Edit / Delete", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Categorization", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)


def render_accounts(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame, text="• Checking account", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Savings", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Balances", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)


def render_settings(frame):
    for widget in frame.winfo_children():
        widget.destroy()
    ctk.CTkLabel(frame, text="• User profile", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Currency", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)
    ctk.CTkLabel(frame, text="• Notifications", font=("Arial", 18), text_color=COLOR_TEXT_LIGHT).pack(anchor="w", padx=40)


SECTIONS = {
    "General":      render_general,
    "History":      render_history,
    "Transactions": render_transactions,
    "Accounts":     render_accounts,
    "Settings":     render_settings,
}
