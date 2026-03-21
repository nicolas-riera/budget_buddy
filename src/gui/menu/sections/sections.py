from src.gui.menu.sections.general import render_general
from src.gui.menu.sections.history import render_history
from src.gui.menu.sections.transactions import render_transactions
from src.gui.menu.sections.accounts import render_accounts
from src.gui.menu.sections.settings import render_settings

# ── CENTRALIZED MOCK DATA (To be replaced by backend) ──────────────────────
ACTIVE_ACCOUNT_INDEX = 0

def set_active_account(idx, frame):
    global ACTIVE_ACCOUNT_INDEX
    ACTIVE_ACCOUNT_INDEX = idx
    render_accounts(frame, MOCK_ACCOUNTS, set_active_account, ACTIVE_ACCOUNT_INDEX)

MOCK_ACCOUNTS = [
    {
        "number": "1", 
        "name": "Personal Checking", 
        "balance": "€ 4,820.50", 
        "date": "01/01/2026",
        "transactions": [
            ("Grocery store",    "-€ 52.30",  "#FF9E9E", "03/19/2026", "Groceries", "Withdrawal"),
            ("Salary",           "+€ 2,100.00", "#C8F0C0", "03/18/2026", "Salary", "Deposit"),
            ("Netflix",          "-€ 15.99",  "#FF9E9E", "03/17/2026", "Entertainment", "Withdrawal"),
            ("Electric bill",    "-€ 78.00",  "#FF9E9E", "03/14/2026", "Bills", "Withdrawal"),
            ("Restaurant",       "-€ 34.50",  "#FF9E9E", "03/12/2026", "Dining", "Withdrawal"),
            ("Amazon",           "-€ 24.90",  "#FF9E9E", "03/05/2026", "Entertainment", "Withdrawal"),
            ("Gym membership",   "-€ 29.99",  "#FF9E9E", "03/01/2026", "Entertainment", "Withdrawal"),
            ("Grocery store",    "-€ 89.20",  "#FF9E9E", "02/25/2026", "Groceries", "Withdrawal"),
            ("Steam games",      "-€ 45.00",  "#FF9E9E", "02/20/2026", "Entertainment", "Withdrawal"),
            ("Salary",           "+€ 2,100.00", "#C8F0C0", "02/18/2026", "Salary", "Deposit"),
            ("Dinner out",       "-€ 85.00",  "#FF9E9E", "02/15/2026", "Dining", "Withdrawal"),
            ("Spotify",          "-€ 10.99",  "#FF9E9E", "02/13/2026", "Entertainment", "Withdrawal"),
        ]
    },
    {
        "number": "2", 
        "name": "Emergency Savings", 
        "balance": "€ 12,300.00", 
        "date": "05/02/2025",
        "transactions": [
            ("Transfer in",      "+€ 200.00", "#C8F0C0", "03/10/2026", "Transfer", "Transfer"),
            ("Pot-de-vin",       "-€ 500.00", "#FF9E9E", "01/15/2026", "Bribe", "Withdrawal"),
        ]
    },
    {
        "number": "3", 
        "name": "Business Account",  
        "balance": "€ 8,450.00",  
        "date": "10/12/2025",
        "transactions": [
            ("Freelance invoice","+€ 50.00",  "#C8F0C0", "03/17/2026", "Income", "Deposit"),
            ("Freelance invoice","+€ 450.00", "#C8F0C0", "02/28/2026", "Income", "Deposit"),
            ("Client lunch",     "-€ 120.00", "#FF9E9E", "02/25/2026", "Dining", "Withdrawal"),
        ]
    }
]

MOCK_USER = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "accounts_count": 3
}

# ── ROUTING ────────────────────────────────────────────────────────────────
SECTIONS = {
    # general computes the graph internally so we pass the full transaction list
    "General":      lambda frame: render_general(frame, MOCK_ACCOUNTS[ACTIVE_ACCOUNT_INDEX]["balance"], MOCK_ACCOUNTS[ACTIVE_ACCOUNT_INDEX]["name"], MOCK_ACCOUNTS[ACTIVE_ACCOUNT_INDEX]["number"], MOCK_ACCOUNTS[ACTIVE_ACCOUNT_INDEX]["transactions"]),
    # history gets the entire list of transactions
    "History":      lambda frame: render_history(frame, MOCK_ACCOUNTS[ACTIVE_ACCOUNT_INDEX]["transactions"]),
    "Transactions": lambda frame: render_transactions(frame, MOCK_ACCOUNTS, ACTIVE_ACCOUNT_INDEX),
    "Accounts":     lambda frame: render_accounts(frame, MOCK_ACCOUNTS, set_active_account, ACTIVE_ACCOUNT_INDEX),
    "Settings":     lambda frame: render_settings(frame, MOCK_USER),
}
