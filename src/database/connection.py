import pg8000
from dotenv import load_dotenv
import os

class Connection:
    def __init__(self,  DataBase: str) -> None:
        self.cursor = None
        self.DB = DataBase
        self.connection = None
        self.connect()

    def connect(self):
        try:
            load_dotenv()
            HOST = os.getenv("DB_HOST")
            USER = os.getenv("DB_USER")
            PASSWORD = os.getenv("DB_PASSWORD")
            print("Connecting to DataBase: ", self.DB)
            self.connection = pg8000.connect(host=HOST, 
                                             user=USER, 
                                             password=PASSWORD, 
                                             database=self.DB,
                                             port=5432)
            print("Connection Succesful")
            self.cursor = self.connection.cursor()

        except Exception as e:
            print("Connection Error: ", e)

    def close(self):
        self.connection.close()
        print("Connection Closed")

    def addUser(self, name, ci, gender, phone, civil_status, birth_date, address):
        values = (name, ci, gender, phone, civil_status, birth_date, address)
        insertStatement = '''INSERT INTO public."Users" 
                             values (%s, %s, %s, %s, %s, %s, %s);'''
        self.cursor.execute(insertStatement, values)
        self.connection.commit()

    def getUsersData(self):
        self.cursor.execute('SELECT * FROM public."Users";')
        return self.cursor.fetchall()

    def searchUser(self, ci):
        self.cursor.execute('''SELECT * FROM public."Users" WHERE "CI" = %s;''', (ci))
        return self.cursor.fetchone()
    
    def getUserGender(self, ci):
        self.cursor.execute('''SELECT gender FROM public."Users" WHERE "CI" = %s;''', (ci))
        return self.cursor.fetchone()

    def updateUser(self, phone, civil_status, ci):
        self.cursor.execute('''UPDATE public."Users" SET phone = %s, civil_status = %s 
                               WHERE "CI" = %s;''', (phone, civil_status, ci))
        self.connection.commit()
        print("User Updated")

    def deleteUser(self, ci):
        self.cursor.execute('''DELETE FROM public."Users" WHERE CI = %s;''', (ci))
        self.connection.commit()
        print("User Deleted")