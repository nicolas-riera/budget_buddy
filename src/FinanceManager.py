class FinanceManager:
    @staticmethod
    def deposit(root, amount, account_id, type, description):
        query_transation = "INSERT INTO transactions (id_account, amount, type, description) VALUES (%s, %s, %s, %s)"
        query_account = "UPDATE account SET balance = balance + %s WHERE id = %s"
        
        root.database.run_request(query_transation, (account_id, amount, type, description))
        root.database.run_request(query_account, (amount, account_id))

    @staticmethod
    def withdraw(root, amount):
        # todo : add overdrown check
        query = ""
        root.database.run_request(query, (amount, root.account_id))

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