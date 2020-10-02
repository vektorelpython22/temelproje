from DB import DB 

class AlbumDB:
    def __init__(self):
        self.db = DB(r"FND\SQL\DB\chinook.db","albums")


    def albumEkle(self,degerListesi):
        self.db.tabloAdi = "albums"
        sonuc = self.db.insert(alan=["Title","ArtistId"],deger=degerListesi)
        if sonuc==1:
            return True
        else:
            return False

    def artistGetir(self):
        self.db.tabloAdi = "artists"
        liste = self.db.select()
        return liste