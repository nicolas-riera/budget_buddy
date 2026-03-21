import customtkinter as ctk
import tkinter as tk
from src.gui.color_palette import *

def render_general(frame, balance, account_name, account_id, all_transactions):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── chart building logic (mock aid only) ──────────────
    def _compute_chart(txs):
        if not txs:
            return [("N/A", 0, 0)]
        from collections import defaultdict
        data = defaultdict(lambda: {"exp": 0.0, "inc": 0.0})
        for tx in txs:
            amt_str = tx[1]
            date = tx[3]
            val_str = amt_str.replace("€", "").replace(",", "").replace("+", "").replace(" ", "")
            val = float(val_str)
            if val < 0:
                data[date]["exp"] += abs(val)
            else:
                data[date]["inc"] += val
                
        sorted_dates = sorted(data.keys())[-7:]
        return [("/".join(d.split("/")[:2]) if "/" in d else d, data[d]["exp"], data[d]["inc"]) for d in sorted_dates]

    chart_data = _compute_chart(all_transactions)
    recent_transactions = all_transactions[:7]

    # ── main grid ──────────────────────────────────────────────────────────
    PAD = 12
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)

    # Overdraft Detection
    val_str = balance.replace("€", "").replace(",", "").replace("+", "").replace(" ", "")
    try:
        bal_val = float(val_str)
    except:
        bal_val = 0.0

    has_alert = bal_val < 0
    start_row = 1 if has_alert else 0

    if has_alert:
        frame.rowconfigure(0, weight=0)
        alert_frame = ctk.CTkFrame(frame, fg_color="#FF9E9E", corner_radius=8)
        alert_frame.grid(row=0, column=0, columnspan=2, padx=PAD, pady=(PAD, 0), sticky="ew")
        
        ctk.CTkLabel(alert_frame, text="⚠️ ALERT: This account is currently in overdraft. Please add funds to avoid fees.",
                     font=("Arial", 14, "bold"), text_color="#4A1C1C").pack(pady=10)

    frame.rowconfigure(start_row, weight=0)       # fixed header
    frame.rowconfigure(start_row + 1, weight=1)   # expanding body

    # ─────────────────────────── TOP-LEFT : Balance ────────────────────────
    balance_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                                border_width=1, border_color=COLOR_BORDER)
    balance_card.grid(row=start_row, column=0, padx=(PAD, PAD//2), pady=(PAD, PAD//2), sticky="nsew")

    ctk.CTkLabel(balance_card, text="Balance",
                 font=("Arial", 13, "bold"), text_color=COLOR_TEXT_LIGHT,
                 anchor="w").pack(anchor="w", padx=14, pady=(10, 2))

    ctk.CTkLabel(balance_card, text=balance,
                 font=("Arial", 26, "bold"), text_color="#C8F0C0" if not has_alert else "#FF9E9E",
                 anchor="w").pack(anchor="w", padx=14, pady=(0, 10))

    # ─────────────────────────── TOP-RIGHT : Account ───────────────────────
    account_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                                border_width=1, border_color=COLOR_BORDER)
    account_card.grid(row=start_row, column=1, padx=(PAD//2, PAD), pady=(PAD, PAD//2), sticky="nsew")

    ctk.CTkLabel(account_card, text="Account",
                 font=("Arial", 13, "bold"), text_color=COLOR_TEXT_LIGHT,
                 anchor="w").pack(anchor="w", padx=14, pady=(10, 2))

    ctk.CTkLabel(account_card, text=account_name,
                 font=("Arial", 18, "bold"), text_color="#A8D8FF",
                 anchor="w").pack(anchor="w", padx=14)
    ctk.CTkLabel(account_card, text=account_id,
                 font=("Arial", 10), text_color=COLOR_TEXT_LIGHT,
                 anchor="w").pack(anchor="w", padx=14, pady=(0, 10))

    # ─────────────────── BOTTOM-LEFT : Recent History ──────────────────────
    recent_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                                border_width=1, border_color=COLOR_BORDER)
    recent_card.grid(row=start_row + 1, column=0, padx=(PAD, PAD//2), pady=(PAD//2, PAD), sticky="nsew")
    recent_card.rowconfigure(1, weight=1)
    recent_card.columnconfigure(0, weight=1)

    ctk.CTkLabel(recent_card, text="Recent",
                 font=("Arial", 13, "bold"), text_color=COLOR_TEXT_LIGHT,
                 anchor="w").grid(row=0, column=0, sticky="w", padx=14, pady=(10, 6))

    # scrollable list
    scroll = ctk.CTkScrollableFrame(recent_card, fg_color="transparent")
    scroll.grid(row=1, column=0, sticky="nsew", padx=8, pady=(0, 8))
    scroll.columnconfigure(0, weight=1)

    for i, tx in enumerate(recent_transactions):
        label = tx[0]
        amount = tx[1]
        color = tx[2]
        date = tx[3]
        row_frame = ctk.CTkFrame(scroll, fg_color="#6E5B58", corner_radius=8)
        row_frame.grid(row=i, column=0, sticky="ew", padx=4, pady=3)
        row_frame.columnconfigure(1, weight=1)

        ctk.CTkLabel(row_frame, text=date, font=("Arial", 10),
                     text_color="#C0B0AE", width=80).grid(row=0, column=0, padx=(8, 4), pady=6)
        ctk.CTkLabel(row_frame, text=label, font=("Arial", 12),
                     text_color=COLOR_TEXT_LIGHT, anchor="w").grid(row=0, column=1, sticky="w", padx=4)
        ctk.CTkLabel(row_frame, text=amount, font=("Arial", 12, "bold"),
                     text_color=color, anchor="e").grid(row=0, column=2, sticky="e", padx=(4, 10))

    # ─────────────────── BOTTOM-RIGHT : Transaction Chart ──────────────────
    chart_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                              border_width=1, border_color=COLOR_BORDER)
    chart_card.grid(row=start_row + 1, column=1, padx=(PAD//2, PAD), pady=(PAD//2, PAD), sticky="nsew")
    chart_card.rowconfigure(1, weight=1)
    chart_card.columnconfigure(0, weight=1)

    ctk.CTkLabel(chart_card, text="Transactions (last 7 days)",
                 font=("Arial", 13, "bold"), text_color=COLOR_TEXT_LIGHT,
                 anchor="w").grid(row=0, column=0, sticky="w", padx=14, pady=(10, 6))

    canvas_frame = ctk.CTkFrame(chart_card, fg_color="transparent")
    canvas_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))
    canvas_frame.rowconfigure(0, weight=1)
    canvas_frame.columnconfigure(0, weight=1)

    canvas = tk.Canvas(canvas_frame, bg="#6E5B58", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    def draw_chart(event=None):
        canvas.delete("all")
        w = canvas.winfo_width()
        h = canvas.winfo_height()
        if w < 10 or h < 10:
            return

        # margins
        ml, mr, mt, mb = 30, 10, 10, 28
        cw = w - ml - mr
        ch = h - mt - mb

        max_val = max((max(exp, inc) for _, exp, inc in chart_data), default=0) or 1
        bar_count = len(chart_data) or 1
        group_w = cw / bar_count
        bar_w = max(4, group_w * 0.3)

        # horizontal axis
        canvas.create_line(ml, mt + ch, w - mr, mt + ch,
                           fill="#9E8C89", width=1)

        for i, (day, exp, inc) in enumerate(chart_data):
            x_center = ml + i * group_w + group_w / 2

            # expenses bar (red)
            if exp > 0:
                bh = (exp / max_val) * ch
                x0 = x_center - bar_w - 2
                canvas.create_rectangle(x0, mt + ch - bh, x0 + bar_w, mt + ch,
                                        fill="#E87272", outline="")

            # income bar (green)
            if inc > 0:
                bh = (inc / max_val) * ch
                x0 = x_center + 2
                canvas.create_rectangle(x0, mt + ch - bh, x0 + bar_w, mt + ch,
                                        fill="#72C87B", outline="")

            # day label
            canvas.create_text(x_center, mt + ch + 14,
                                text=day, fill="#E8E2E1", font=("Arial", 9))

        # legend
        canvas.create_rectangle(ml, 4, ml + 10, 14, fill="#E87272", outline="")
        canvas.create_text(ml + 14, 9, text="Expenses", anchor="w",
                           fill="#E8E2E1", font=("Arial", 8))
        canvas.create_rectangle(ml + 75, 4, ml + 85, 14, fill="#72C87B", outline="")
        canvas.create_text(ml + 89, 9, text="Income", anchor="w",
                           fill="#E8E2E1", font=("Arial", 8))

    canvas.bind("<Configure>", draw_chart)
    canvas.after(100, draw_chart)
