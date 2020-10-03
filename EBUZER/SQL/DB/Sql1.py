import sqlite3 as sql
def VeriGetir():
    try:
        db = sql.connect(r"IBRAHIM\SQL\DB\chinook.db")
        cur = db.cursor()
        artiz = input("artist id giriniz:")
        sorgu = f""" SELECT * FROM albums 
        where ArtistId = {artiz}
        """
        cur.execute(sorgu)
        liste = cur.fetchall()
        print(liste)
        return liste
    except Exception as hata:
        print(hata)
    finally:
        cur.close()
        db.close()



def VeriEkle():
    try:
        db = sql.connect(r"IBRAHIM\SQL\DB\chinook.db")
        cur = db.cursor()
        artiz = input("artist id giriniz:")
        sorgu = f""" INSERT INTO artists (Name) 
        values ('{artiz}')
        """
        cur.execute(sorgu)
        db.commit()
        return 1
    except Exception as hata:
        db.rollback()
        print(hata)
        return -1 
    finally:
        cur.close()
        db.close()