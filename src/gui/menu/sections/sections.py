from src.gui.menu.sections.general import render_general
from src.gui.menu.sections.history import render_history
from src.gui.menu.sections.transactions import render_transactions
from src.gui.menu.sections.accounts import render_accounts
from src.gui.menu.sections.settings import render_settings

# ── CENTRALIZED MOCK DATA (To be replaced by backend) ──────────────────────
MOCK_BALANCE = "€ 4,820.50"
MOCK_ACCOUNT_NAME = "Personnal"
MOCK_ACCOUNT_ID = "1"

MOCK_TRANSACTIONS = [
    ("Grocery store",    "-€ 52.30",  "#FF9E9E", "03/19/2026"),
    ("Salary",           "+€ 2,100.00", "#C8F0C0", "03/18/2026"),
    ("Netflix",          "-€ 15.99",  "#FF9E9E", "03/17/2026"),
    ("Freelance invoice","+€ 50.00",  "#C8F0C0", "03/17/2026"),
    ("Electric bill",    "-€ 78.00",  "#FF9E9E", "03/14/2026"),
    ("Restaurant",       "-€ 34.50",  "#FF9E9E", "03/12/2026"),
    ("Transfer in",      "+€ 200.00", "#C8F0C0", "03/10/2026"),
    ("Amazon",           "-€ 24.90",  "#FF9E9E", "03/05/2026"),
    ("Gym membership",   "-€ 29.99",  "#FF9E9E", "03/01/2026"),
    ("Freelance invoice","+€ 450.00", "#C8F0C0", "02/28/2026"),
    ("Grocery store",    "-€ 89.20",  "#FF9E9E", "02/25/2026"),
    ("Steam games",      "-€ 45.00",  "#FF9E9E", "02/20/2026"),
    ("Salary",           "+€ 2,100.00", "#C8F0C0", "02/18/2026"),
    ("Dinner out",       "-€ 85.00",  "#FF9E9E", "02/15/2026"),
    ("Spotify",          "-€ 10.99",  "#FF9E9E", "02/13/2026"),
]

MOCK_ACCOUNTS = [
    {"number": "FR76 1234 5678 9012", "name": "Personal Checking", "balance": "€ 4,820.50", "date": "01/01/2026"},
    {"number": "FR76 0987 6543 2109", "name": "Emergency Savings", "balance": "€ 12,300.00", "date": "05/02/2025"},
    {"number": "FR76 1122 3344 5566", "name": "Business Account",  "balance": "€ 8,450.00",  "date": "10/12/2025"}
]

MOCK_USER = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "accounts_count": 3
}

# ── ROUTING ────────────────────────────────────────────────────────────────
SECTIONS = {
    # general computes the graph internally so we pass the full transaction list
    "General":      lambda frame: render_general(frame, MOCK_BALANCE, MOCK_ACCOUNT_NAME, MOCK_ACCOUNT_ID, MOCK_TRANSACTIONS),
    # history gets the entire list of transactions
    "History":      lambda frame: render_history(frame, MOCK_TRANSACTIONS),
    "Transactions": render_transactions,
    "Accounts":     lambda frame: render_accounts(frame, MOCK_ACCOUNTS),
    "Settings":     lambda frame: render_settings(frame, MOCK_USER),
}
