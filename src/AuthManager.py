import bcrypt
import re

class AuthManager:
        
    # Login
    @staticmethod
    def login_user(root, email, password):

        email_found = None
        for emails in root.database.run_request("SELECT email FROM users"):
            if emails[0] == email.lower():
                email_found = email.lower()
        if not email_found:
            return None
        
        stored_password = root.database.run_request("SELECT password FROM users WHERE email = %s", data=(email_found,))
        stored_password_formated = stored_password[0][0].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_formated):
            return root.database.run_request("SELECT id FROM users WHERE email = %s", data=(email_found,))
        else:
            return None

    # Register
    @staticmethod
    def hash_password(password):
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed
    
    @staticmethod
    def check_email_format(email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

    @staticmethod  
    def check_email_in_db(root, email):
        email_found = None
        for emails in root.database.run_request("SELECT email FROM users"):
            if emails[0] == email.lower():
                email_found = email.lower()
        if email_found:
            return True
        else:
            return False
        
    @staticmethod    
    def check_password_strengh(password):
        if len(password) < 10:
            return False
        
        has_upper = re.search(r"[A-Z]", password)
        has_lower = re.search(r"[a-z]", password)
        has_digit = re.search(r"\d", password)
        has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

        return all([has_upper, has_lower, has_digit, has_special])

    @staticmethod   
    def register_user(root, firstname, lastname, email, password):
        hashed = AuthManager.hash_password(password)
        root.database.run_request("INSERT INTO users (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)", (firstname, lastname, email, hashed))
        del hashed

        id = root.database.run_request("SELECT id FROM users WHERE email=%s", (email,))[0][0]
        root.database.run_request("INSERT INTO account (id_user, balance, can_overdrawn) VALUES (%s, 0, 0)", (id,))
        return id
        