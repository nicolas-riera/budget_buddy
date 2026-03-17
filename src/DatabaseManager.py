import mysql.connector #import required module
import os 
import dotenv

class DatabaseManager: 

    def connect_db(self):
        dotenv.load_dotenv()
        self.db_connect = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD"),
            db = os.getenv("DB_NAME")
        )

    def run_request(self, request, data): #takes as param the query and the data
        self.connect_db()
        self.cursor = self.db_connect.cursor()
        self.cursor.execute(request, data)
        print(self.cursor.fetchall())
        self.close_db()
        #TODO add a return fetchall()

    def show_tables(self):
        data = "SHOW TABLES"
        return data
    def close_db(self):
        self.cursor.close()
        self.db_connect.close()


db = DatabaseManager()
db.run_request(db.show_tables(), None)

