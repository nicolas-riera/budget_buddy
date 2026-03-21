import customtkinter as ctk
from src.gui.color_palette import *
from datetime import datetime

def render_history(frame, transactions):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Header ─────────────────────────────────────────────────────────────
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(fill="x", padx=30, pady=(20, 5))

    ctk.CTkLabel(header_frame, text="Transaction History",
                 font=("Arial", 24, "bold"), text_color=COLOR_TEXT_LIGHT).pack(side="left")

    # ── Filters/Sorting Grid ───────────────────────────────────────────────
    filter_frame = ctk.CTkFrame(frame, fg_color="#6E5B58", corner_radius=8)
    filter_frame.pack(fill="x", padx=30, pady=(0, 10))
    filter_frame.columnconfigure((0,1,2), weight=1)

    # Date Start
    ctk.CTkLabel(filter_frame, text="Start Date (MM/DD/YYYY):", font=("Arial", 12), text_color=COLOR_TEXT_LIGHT).grid(row=0, column=0, padx=10, pady=(5,0), sticky="w")
    start_date_var = ctk.StringVar()
    ctk.CTkEntry(filter_frame, textvariable=start_date_var, font=("Arial", 12), fg_color="#5D4C4A", border_color="#4F403E", text_color=COLOR_TEXT_LIGHT).grid(row=1, column=0, padx=10, pady=(0,5), sticky="ew")

    # Date End
    ctk.CTkLabel(filter_frame, text="End Date (MM/DD/YYYY):", font=("Arial", 12), text_color=COLOR_TEXT_LIGHT).grid(row=0, column=1, padx=10, pady=(5,0), sticky="w")
    end_date_var = ctk.StringVar()
    ctk.CTkEntry(filter_frame, textvariable=end_date_var, font=("Arial", 12), fg_color="#5D4C4A", border_color="#4F403E", text_color=COLOR_TEXT_LIGHT).grid(row=1, column=1, padx=10, pady=(0,5), sticky="ew")

    # Category
    ctk.CTkLabel(filter_frame, text="Category:", font=("Arial", 12), text_color=COLOR_TEXT_LIGHT).grid(row=0, column=2, padx=10, pady=(5,0), sticky="w")
    cat_var = ctk.StringVar(value="All")
    ctk.CTkOptionMenu(filter_frame, variable=cat_var, values=["All", "Alimentation", "Salaire", "Loisir", "Factures", "Repas", "Transfert", "Pot-de-vin", "Revenu"], fg_color="#5D4C4A", button_color="#4F403E", button_hover_color="#4F403E").grid(row=1, column=2, padx=10, pady=(0,5), sticky="ew")

    # Type
    ctk.CTkLabel(filter_frame, text="Type:", font=("Arial", 12), text_color=COLOR_TEXT_LIGHT).grid(row=2, column=0, padx=10, pady=(0,0), sticky="w")
    type_var = ctk.StringVar(value="All")
    ctk.CTkOptionMenu(filter_frame, variable=type_var, values=["All", "Deposit", "Withdrawal", "Transfer"], fg_color="#5D4C4A", button_color="#4F403E", button_hover_color="#4F403E").grid(row=3, column=0, padx=10, pady=(0,10), sticky="ew")

    # Sort
    ctk.CTkLabel(filter_frame, text="Sort by:", font=("Arial", 12), text_color=COLOR_TEXT_LIGHT).grid(row=2, column=1, padx=10, pady=(0,0), sticky="w")
    sort_var = ctk.StringVar(value="Date (Newest)")
    ctk.CTkOptionMenu(filter_frame, variable=sort_var, values=["Date (Newest)", "Date (Oldest)", "Price (High to Low)", "Price (Low to High)", "Vendor (A-Z)", "Vendor (Z-A)"], fg_color="#5D4C4A", button_color="#4F403E", button_hover_color="#4F403E").grid(row=3, column=1, padx=10, pady=(0,10), sticky="ew")

    current_txs = list(transactions)

    # ── Scrollable List ────────────────────────────────────────────────────
    list_card = ctk.CTkFrame(frame, fg_color=COLOR_CARD, corner_radius=12,
                             border_width=1, border_color=COLOR_BORDER)
    list_card.pack(fill="both", expand=True, padx=30, pady=(0, 20))
    list_card.pack_propagate(False)

    scroll = ctk.CTkScrollableFrame(list_card, fg_color="transparent")
    scroll.pack(fill="both", expand=True, padx=15, pady=15)

    def populate_list():
        for widget in scroll.winfo_children():
            widget.destroy()
            
        for i, tx in enumerate(current_txs):
            label = tx[0]
            amount = tx[1]
            color = tx[2]
            date = tx[3]
            category = tx[4] if len(tx) > 4 else "Unknown"

            row_frame = ctk.CTkFrame(scroll, fg_color="#6E5B58", corner_radius=8, height=45)
            row_frame.pack(fill="x", pady=4)
            row_frame.pack_propagate(False)

            ctk.CTkLabel(row_frame, text=date, font=("Arial", 12),
                         text_color="#C0B0AE", width=80, anchor="w").pack(side="left", padx=(15, 10))
            
            ctk.CTkLabel(row_frame, text=category, font=("Arial", 10, "italic"),
                         text_color="#A8D8FF", width=70, anchor="w").pack(side="left", padx=5)
                         
            ctk.CTkLabel(row_frame, text=label, font=("Arial", 14),
                         text_color=COLOR_TEXT_LIGHT, anchor="w").pack(side="left", padx=10, fill="x", expand=True)
                         
            ctk.CTkLabel(row_frame, text=amount, font=("Arial", 14, "bold"),
                         text_color=color, anchor="e").pack(side="right", padx=15)

    def apply_filters():
        nonlocal current_txs
        filtered = []

        def parse_date(d_str):
            try:
                return datetime.strptime(d_str, "%m/%d/%Y")
            except:
                return datetime.min

        d_s_str = start_date_var.get().strip()
        d_e_str = end_date_var.get().strip()
        
        d_start = parse_date(d_s_str) if d_s_str else datetime.min
        d_end = parse_date(d_e_str) if d_e_str else datetime.max

        # Ensure inclusive matching if one day is specified
        if d_end == datetime.min: d_end = datetime.max

        cat = cat_var.get()
        t_type = type_var.get()
        
        for tx in transactions:
            ctg = tx[4] if len(tx) > 4 else "Unknown"
            typ = tx[5] if len(tx) > 5 else "Unknown"
            
            tx_date = parse_date(tx[3])
            
            if tx_date < d_start or tx_date > d_end:
                continue
            if cat != "All" and ctg != cat:
                continue
            if t_type != "All" and typ != t_type:
                continue
                
            filtered.append(tx)

        def parse_price(p_str):
            val = p_str.replace("€", "").replace(",", "").replace("+", "").replace(" ", "")
            try:
                return float(val)
            except:
                return 0.0

        choice = sort_var.get()
        if choice == "Date (Newest)":
            filtered.sort(key=lambda x: parse_date(x[3]), reverse=True)
        elif choice == "Date (Oldest)":
            filtered.sort(key=lambda x: parse_date(x[3]))
        elif choice == "Price (High to Low)":
            filtered.sort(key=lambda x: parse_price(x[1]), reverse=True)
        elif choice == "Price (Low to High)":
            filtered.sort(key=lambda x: parse_price(x[1]))
        elif choice == "Vendor (A-Z)":
            filtered.sort(key=lambda x: x[0].lower())
        elif choice == "Vendor (Z-A)":
            filtered.sort(key=lambda x: x[0].lower(), reverse=True)

        current_txs.clear()
        current_txs.extend(filtered)
        populate_list()

    # Apply Button in the empty spot of row 3
    ctk.CTkButton(filter_frame, text="Apply Filters", command=apply_filters, fg_color="#A8D8FF", text_color="#183652", hover_color="#6BA4D8").grid(row=3, column=2, padx=10, pady=(0,10), sticky="ew")

    # Initial sort and populate
    apply_filters()
