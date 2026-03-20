class FinanceManager:
    @staticmethod
    def deposit(root, amount):
        query = "UPDATE transactions SET amount = amount + %s WHERE account_id = %s"
        root.database.run_request(query, (amount, root.account_id))

    @staticmethod
    def withdraw(root, amount):
        # todo : add overdrown check
        query = "UPDATE transactions SET amount = amount - %s WHERE account_id = %s"
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