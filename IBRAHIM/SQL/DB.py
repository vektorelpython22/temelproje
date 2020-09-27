import sqlite3 as sql


class DB:
    def __init__(self,dbAdres,tabloAdi):
        self.dbAdres = dbAdres
        self.tabloAdi = tabloAdi
        self.db = sql.connect(self.dbAdres)
        self.cur = self.db.cursor()

    def insert(self,**kwargs):
        try:
            listAlan = []
            listValue = []
            for key,value in kwargs.items():
                if key == "alan":
                    listAlan = value
                if key == "deger":
                    listValue = value

            sorgu = f"""INSERT INTO 
            {self.tabloAdi} ({",".join(listAlan)})
            VALUES  ({",".join(listValue)}) """

            self.cur.execute(sorgu)
            self.db.commit()
            return 1
        except:
            self.db.rollback()
            return -1


    def __del__(self):
        self.cur.close()
        self.db.close()
        

    
