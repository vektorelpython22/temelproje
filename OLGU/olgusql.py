# veritabanı oluşturmak
#sqlite3 modülünü dahil ediyoruz
import sqlite3 as sql

vt = sql.connect('il_ilce.sqlite') # bağlanacak olduğumuz veri tabanının adını yazıyoruz eğer sistemde adını yazdığımız veri tabanı yoksa yazılan adda bir veri tabanı oluşturuluyor

imlec = vt.cursor() # veri tabanı üzerinde işlem yapmak için imleç oluşturuyoruz



def addatabes2():
    imlec.execute("SELECT * FROM ilceler")
    allitems2=imlec.fetchall()
    b=[]
    for i in allitems2:
        b.append(str(i))
    return b


def addatabase():
        imlec.execute("SELECT * FROM iller")
        allitems=imlec.fetchall()
        a=[]
        for i in allitems:
            a.append(str(i))

        return a



vt.commit() # veri tabanına hafızadaki bilgiyi kaydetmek için
#vt.close() # veri tabanını kapatmak için
