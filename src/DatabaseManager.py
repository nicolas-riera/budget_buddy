import mysql.connector
import os 
import dotenv

class DatabaseManager: 
        
    def request(self):
        self.connect_db()

        self.cursor.execute("SHOW TABLES")
        print(self.cursor.fetchall())
        
        self.close_db()

    def connect_db(self):
        dotenv.load_dotenv()
        self.db_connect = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            db = os.getenv("DB_NAME")
        )
        self.cursor = self.db_connect.cursor()


    def close_db(self):
        self.cursor.close()
        self.db_connect.close()


db = DatabaseManager()
db.request()

db.request()