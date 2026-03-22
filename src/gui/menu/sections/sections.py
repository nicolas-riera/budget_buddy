from src.gui.menu.sections.general import render_general
from src.gui.menu.sections.history import render_history
from src.gui.menu.sections.transactions import render_transactions
from src.gui.menu.sections.accounts import render_accounts
from src.gui.menu.sections.settings import render_settings

# ── ROUTING ────────────────────────────────────────────────────────────────
SECTIONS = {
    # general computes the graph internally so we pass the full transaction list
    "General":      lambda root, frame: render_general(root, frame),
    # history gets the entire list of transactions
    "History":      lambda root, frame: render_history(root, frame),
    "Transactions": lambda root, frame: render_transactions(root, frame),
    "Accounts":     lambda root, frame: render_accounts(root, frame),
    "Settings":     lambda root, frame: render_settings(root, frame),
}
