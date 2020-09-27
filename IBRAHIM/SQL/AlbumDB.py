from DB import DB 

class AlbumDB:
    def __init__(self):
        self.db = DB(r"IBRAHIM\SQL\DB\chinook.db","albums")


    def albumEkle(self,degerListesi):
        sonuc = self.db.insert(alan=["Title","ArtistId"],deger=degerListesi)
        if sonuc==1:
            return True
        else:
            return False
