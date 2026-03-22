import customtkinter as ctk
import re

from src.gui.color_palette import *
from src.FinanceManager import FinanceManager

def render_transactions(root, frame):

    def validate_amount(new_value):

        #reset labels
        success_label.configure(text="")
        error_label.configure(text="")

        if new_value == "":
            return False 
        try:
            float(new_value)
            if new_value.count(".") > 1:
                return False
            return True
        except ValueError:
            return False
        
    def process_description(description):
        if description:
            return description.strip()[:255]
        else:
            return ""

    def on_deposit_confirm(values):
        if validate_amount(values["Amount"]):
            FinanceManager.deposit(root, values["Amount"], int(re.search(r'\d+', values["Account"]).group()), values["Category"] ,process_description(values["Description"]))
            success_label.configure(text=f"€ {values["Amount"]} has been deposited.")
        else:
            error_label.configure(text="Invalid Amount.")

    def on_withdrawal_confirm(values):
        if validate_amount(values["Amount"]):
            if FinanceManager.check_balance(root, int(re.search(r'\d+', values["Account"]).group()), values["Amount"]):
                FinanceManager.withdraw(root, values["Amount"], int(re.search(r'\d+', values["Account"]).group()), values["Category"] ,process_description(values["Description"]))
                success_label.configure(text=f"€ {values["Amount"]} has been withdrawn.")
            else:
                error_label.configure(text="Not enough balance on account.")
        else:
            error_label.configure(text="Invalid Amount.")

    def on_transfer_confirm(values):
        print("Transfer:", values)

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

    success_label = ctk.CTkLabel(
    header_frame,
    text="",
    text_color=COLOR_AMOUNT_GREEN,
    fg_color="transparent",
    font=("Helvetica", 15, "bold")
    )
    success_label.place(relx=0.5, rely=1.0, anchor="s")

    error_label = ctk.CTkLabel(
    header_frame,
    text="",
    text_color=COLOR_RED,
    fg_color="transparent",
    font=("Helvetica", 15, "bold")
    )
    error_label.place(relx=0.5, rely=1.0, anchor="s")

    # ── Content Area ───────────────────────────────────────────────────────
    tab_frames = {}

    def switch_tab(name):
        for f in tab_frames.values():
            f.pack_forget()
        tab_frames[name].pack(fill="both", expand=True, padx=30, pady=(0, 30))
        
    seg_btn.configure(command=switch_tab)

    widgets = {}

    # Helper function to create forms
    def create_form(parent, fields_config, confirm_color, confirm_text_color, hover_color, on_confirm):
        t_frame = ctk.CTkFrame(parent, fg_color=COLOR_CARD, border_width=1, border_color=COLOR_BORDER, corner_radius=12)
        container = ctk.CTkFrame(t_frame, fg_color="transparent")
        container.place(relx=0.5, rely=0.5, anchor="center")
        
        widgets = {}
        
        for i, config in enumerate(fields_config):
            lbl_text = config["label"]
            f_type = config["type"]
            lbl = ctk.CTkLabel(container, text=lbl_text + " :", font=("Arial", 16, "bold"), text_color=COLOR_TEXT_LIGHT)
            lbl.grid(row=i, column=0, pady=10, padx=(0, 20), sticky="e")
            
            if f_type == "entry":
                w = ctk.CTkEntry(container, width=300, height=40,
                                fg_color="#6E5B58", border_color=COLOR_BORDER,
                                text_color=COLOR_TEXT_LIGHT, font=("Arial", 14))
            elif f_type == "select":
                values = config.get("values", [])
                default = config.get("default", values[0] if values else "")
                var = ctk.StringVar(value=default)
                w = ctk.CTkOptionMenu(container, width=300, height=40,
                                    variable=var, values=values,
                                    fg_color="#6E5B58", button_color="#5D4C4A",
                                    button_hover_color="#4F403E", text_color=COLOR_TEXT_LIGHT, font=("Arial", 14))
                w.var = var 
            w.grid(row=i, column=1, pady=10, sticky="w")
            widgets[lbl_text] = w

        def button_command():
            result = {}
            for k, widget in widgets.items():
                if isinstance(widget, ctk.CTkEntry):
                    result[k] = widget.get()
                elif isinstance(widget, ctk.CTkOptionMenu):
                    result[k] = widget.var.get()
            on_confirm(result)

            for k, widget in widgets.items():
                if isinstance(widget, ctk.CTkEntry):
                    widget.delete(0, "end") 
                elif isinstance(widget, ctk.CTkOptionMenu):
                    default = fields_config[[f["label"] for f in fields_config].index(k)].get("default", "")
                    widget.var.set(default)  

        btn = ctk.CTkButton(container, text="Confirm", font=("Arial", 16, "bold"),
                            fg_color=confirm_color, text_color=confirm_text_color,
                            hover_color=hover_color, height=45, width=200,
                            corner_radius=8, command=button_command)
        btn.grid(row=len(fields_config), column=0, columnspan=2, pady=(30, 0))

        return t_frame

    # ── Field Definitions ──────────────────────────────────────────────────

    active_acc_name = ""
    account_names = []

    for enum, acc in enumerate(FinanceManager.get_user_accounts(root)):

        account_names.append(f"Account N°{acc[0]}")   

        if enum == root.account_active_id:
            active_acc_name = f"Account N°{acc[0]}"

    categories = ["Income", "Groceries", "Dining", "Bills", "Entertainment", "Transport", "Health", "Shopping", "Education", "Transfer", "Other"]

    deposit_fields = [
    {"label": "Account", "type": "select", "values": account_names, "default": active_acc_name},
    {"label": "Amount", "type": "entry"},
    {"label": "Category", "type": "select", "values": categories, "default": categories[0]},
    {"label": "Description", "type": "entry"}
    ]

    withdrawal_fields = [
        {"label": "Account", "type": "select", "values": account_names, "default": active_acc_name},
        {"label": "Amount", "type": "entry"},
        {"label": "Category", "type": "select", "values": categories, "default": categories[0]},
        {"label": "Description", "type": "entry"}
    ]

    transfer_fields = [
        {"label": "Account", "type": "select", "values": account_names, "default": active_acc_name},
        {"label": "Amount", "type": "entry"},
        {"label": "Description", "type": "entry"},
        {"label": "Beneficiary", "type": "entry"}
]

    # Deposits form (Green)
    tab_frames["Deposit"] = create_form(
        frame, deposit_fields, 
        confirm_color="#C8F0C0", confirm_text_color="#2C3E2A", hover_color="#72C87B",
        on_confirm=on_deposit_confirm
    )

    # Withdrawals form (Red)
    tab_frames["Withdrawal"] = create_form(
        frame, withdrawal_fields, 
        confirm_color="#FF9E9E", confirm_text_color="#4A1C1C", hover_color="#E87272",
        on_confirm=on_withdrawal_confirm
    )

    # Transfers form (Blue)
    tab_frames["Transfer"] = create_form(
        frame, transfer_fields, 
        confirm_color="#A8D8FF", confirm_text_color="#183652", hover_color="#6BA4D8",
        on_confirm=on_transfer_confirm
    )

    # Initialize first tab
    switch_tab("Deposit")
