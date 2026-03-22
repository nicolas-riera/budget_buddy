class FinanceManager:

    @staticmethod
    def get_account_balance(root, account_id):
        query = "SELECT balance FROM account WHERE id = %s"
        return root.database.run_request(query, (account_id,))[0][0]

    @staticmethod
    def get_transactions(root, account_id):
        query = "SELECT description, amount, date, type FROM transactions WHERE id_account = %s ORDER BY date DESC"
        return root.database.run_request(query, (account_id,))

    @staticmethod
    def deposit(root, amount, account_id, type, description):
        query_transation = "INSERT INTO transactions (id_account, amount, type, description) VALUES (%s, %s, %s, %s)"
        query_account = "UPDATE account SET balance = balance + %s WHERE id = %s"

        root.database.run_request(query_transation, (account_id, amount, type, description))
        root.database.run_request(query_account, (amount, account_id))

    @staticmethod
    def withdraw(root, amount, account_id, type, description):
        query_transation = "INSERT INTO transactions (id_account, amount, type, description) VALUES (%s, -%s, %s, %s)"
        query_account = "UPDATE account SET balance = balance - %s WHERE id = %s"

        root.database.run_request(query_transation, (account_id, amount, type, description))
        root.database.run_request(query_account, (amount, account_id))

    @staticmethod
    def check_account_can_overdrawn(root, account_id):
        query = "SELECT can_overdrawn FROM account WHERE id = %s"
        if root.database.run_request(query, (account_id,))[0][0] == 0:
            return False
        else:
            return True

    @staticmethod
    def check_balance(root, account_id, amount):
        if FinanceManager.check_account_can_overdrawn(root, account_id):
            return True
        query = "SELECT balance FROM account WHERE id = %s"
        balance = root.database.run_request(query, (account_id,))[0][0]
        if balance - float(amount) >= 0:
            return True
        else:
            return False
        
    @staticmethod
    def check_account_existence(root, account_id):
        query = "SELECT 1 FROM account WHERE id = %s"
        result = root.database.run_request(query, (account_id,))

        if result and len(result) > 0:
            return True
        return False

    @staticmethod
    def get_user_accounts(root):
        query = "SELECT * FROM account WHERE id_user = %s"
        return root.database.run_request(query, (root.account_id,))
    
    @staticmethod
    def create_account(root):
        query = "INSERT INTO account (id_user, balance, can_overdrawn) VALUES (%s, 0, 0)"
        root.database.run_request(query, (root.account_id,))

    @staticmethod
    def delete_account(root, id):
        query = "DELETE FROM account WHERE id=%s"
        root.database.run_request(query, (id,))

    @staticmethod
    def get_user_name(root):
        query = "SELECT firstname, lastname FROM users WHERE id = %s"
        return root.database.run_request(query, (root.account_id,))[0]
    
    @staticmethod
    def get_user_email(root):
        query = "SELECT email FROM users WHERE id = %s"
        return root.database.run_request(query, (root.account_id,))[0]

    @staticmethod
    def get_user_accounts_count(root):
        query = "SELECT COUNT(*) FROM account WHERE id_user = %s"
        return root.database.run_request(query, (root.account_id,))[0][0]
    
    @staticmethod
    def get_user_creation_date(root):
        query = "SELECT creation_date FROM users WHERE id = %s"
        return root.database.run_request(query, (root.account_id,))[0][0]

    @staticmethod
    def disconnect_user(root):
        root.account_id = None
        root.show_page("landing")

    @staticmethod
    def delete_user(root):
        query = "DELETE FROM users WHERE id=%s"
        root.database.run_request(query, (root.account_id,))
        FinanceManager.disconnect_user(root)