class FinanceManager:
    @staticmethod
    def deposit(account_id, amount):
        query = "UPDATE transactions SET amount = amount + %s WHERE account_id = %s"
        DatabaseManager.db.run_request(query, (amount, account_id))

    @staticmethod
    def withdraw(account_id, amount):
        query = "UPDATE transactions SET amount = amount - %s WHERE account_id = %s"
        DatabaseManager.db.run_request(query, (amount, account_id))