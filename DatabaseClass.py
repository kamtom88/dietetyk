import pyodbc
import ctypes
class DB(object):
    def __init__(self,server='DESKTOP-KNOMOR7',database='Diet',username="sa",password="Password123"):
        self.conn=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        self.cursor = self.conn.cursor()
        print("Polaczono z baza", database)

    def query(self,sql):
        t = []
        self.cursor.execute(sql)
        for row in self.cursor:
            t.append(row)
        return t



    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.cursor.commit()
            ctypes.windll.user32.MessageBoxW(0, "Pomyslnie dodano produkt", "!", 1)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Jakis blad", "!", 1)