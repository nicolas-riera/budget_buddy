import customtkinter as ctk
from src.gui.color_palette import *

def render_transactions(frame, accounts, active_account_idx):
    for widget in frame.winfo_children():
        widget.destroy()

    # ── Header ─────────────────────────────────────────────────────────────
    header_frame = ctk.CTkFrame(frame, fg_color="transparent")
    header_frame.pack(fill="x", padx=30, pady=(25, 10))

    ctk.CTkLabel(header_frame, text="Transactions",
                 font=("Arial", 28, "bold"), text_color=COLOR_TEXT_LIGHT).pack(side="left")

    tabs_var = ctk.StringVar(value="Deposit")
    
    seg_btn = ctk.CTkSegmentedButton(
        header_frame,
        values=["Deposit", "Withdrawal", "Transfer"],
        variable=tabs_var,
        font=("Arial", 16, "bold"),
        height=40,
        fg_color="#6E5B58",
        selected_color="#5D4C4A",
        selected_hover_color="#4F403E",
        unselected_color=COLOR_SECTION,
        unselected_hover_color="#6E5B58",
        text_color=COLOR_TEXT_LIGHT
    )
    seg_btn.pack(side="right")

    # ── Content Area ───────────────────────────────────────────────────────
    tab_frames = {}

    def switch_tab(name):
        for f in tab_frames.values():
            f.pack_forget()
        tab_frames[name].pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
    seg_btn.configure(command=switch_tab)

    # Helper function to create forms
    def create_form(parent, fields_config, confirm_color, confirm_text_color, hover_color):
        t_frame = ctk.CTkFrame(parent, fg_color=COLOR_CARD, border_width=1, border_color=COLOR_BORDER, corner_radius=12)
        
        container = ctk.CTkFrame(t_frame, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        for i, config in enumerate(fields_config):
            lbl_text = config["label"]
            f_type = config["type"]
            
            lbl = ctk.CTkLabel(container, text=lbl_text + " :", font=("Arial", 16, "bold"), text_color=COLOR_TEXT_LIGHT)
            lbl.grid(row=i, column=0, pady=10, padx=(0, 20), sticky="e")
            
            if f_type == "entry":
                widget = ctk.CTkEntry(
                    container, width=300, height=40,
                    fg_color="#6E5B58", border_color=COLOR_BORDER,
                    text_color=COLOR_TEXT_LIGHT, font=("Arial", 14)
                )
            elif f_type == "select":
                values = config.get("values", [])
                default = config.get("default", values[0] if values else "")
                var = ctk.StringVar(value=default)
                widget = ctk.CTkOptionMenu(
                    container, width=300, height=40,
                    variable=var, values=values,
                    fg_color="#6E5B58", button_color="#5D4C4A",
                    button_hover_color="#4F403E", text_color=COLOR_TEXT_LIGHT, font=("Arial", 14)
                )
            
            widget.grid(row=i, column=1, pady=10, sticky="w")
            
        btn = ctk.CTkButton(
            container, text="Confirm", font=("Arial", 16, "bold"),
            fg_color=confirm_color, text_color=confirm_text_color, hover_color=hover_color,
            height=45, width=200, corner_radius=8
        )
        btn.grid(row=len(fields_config), column=0, columnspan=2, pady=(30, 0))
        return t_frame

    # ── Field Definitions ──────────────────────────────────────────────────
    account_names = [acc["name"] for acc in accounts]
    active_acc_name = accounts[active_account_idx]["name"] if accounts else ""

    categories = ["Groceries", "Salary", "Entertainment", "Bills", "Dining", "Transfer", "Bribe", "Income"]

    acc_field = {"label": "Account", "type": "select", "values": account_names, "default": active_acc_name}
    cat_field = {"label": "Category", "type": "select", "values": categories, "default": categories[0]}
    amt_field = {"label": "Amount", "type": "entry"}
    desc_field = {"label": "Description", "type": "entry"}
    ben_field = {"label": "Beneficiary", "type": "entry"}

    # Deposits form (Green)
    tab_frames["Deposit"] = create_form(
        frame, [acc_field, amt_field, cat_field, desc_field], 
        confirm_color="#C8F0C0", confirm_text_color="#2C3E2A", hover_color="#72C87B"
    )

    # Withdrawals form (Red)
    tab_frames["Withdrawal"] = create_form(
        frame, [acc_field, amt_field, cat_field, desc_field], 
        confirm_color="#FF9E9E", confirm_text_color="#4A1C1C", hover_color="#E87272"
    )

    # Transfers form (Blue)
    tab_frames["Transfer"] = create_form(
        frame, [acc_field, amt_field, desc_field, ben_field], 
        confirm_color="#A8D8FF", confirm_text_color="#183652", hover_color="#6BA4D8"
    )

    # Initialize first tab
    switch_tab("Deposit")
