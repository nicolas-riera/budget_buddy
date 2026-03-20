import mysql.connector #import required module
import os 
import dotenv

class DatabaseManager: 

    def __init__(self):
        dotenv.load_dotenv()
        try:
            self.db_connect = mysql.connector.connect(
                host = os.getenv("DB_HOST"),
                user = os.getenv("DB_USER"),
                password = os.getenv("DB_PASSWORD"),
                db = os.getenv("DB_NAME")
            )
            self.successful_connection = True
        except Exception as error:
            self.successful_connection = False
            self.connection_error = error


    def run_request(self, request, data=None): #takes as param the query and the data
        self.cursor = self.db_connect.cursor()
        try: 
            self.cursor.execute(request, data) #execute
            if request.lower().startswith(("insert", "update", "delete")): #handle commits if CUD query
                self.db_connect.commit()
            if request.lower().startswith(("desc", "show", "select")): #handle fetch if READ query
                return self.cursor.fetchall()
        except mysql.connector.Error as error :
            print("DB Error: ", error)

    def desc_tables(self):
        data = "DESC ACCOUNT"
        return data
    
    def get_user(self):
        rqst = "SELECT id_user FROM account WHERE id = %s" #%s is a placeholder
        return self.run_request(rqst, (0,))

    def close_db(self):
        self.cursor.close()
        self.db_connect.close()