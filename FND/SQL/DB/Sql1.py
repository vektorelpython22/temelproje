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

VeriGetir()