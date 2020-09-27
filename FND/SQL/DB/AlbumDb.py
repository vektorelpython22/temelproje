from DB import DB

class AlbumDb:

    def __init__(self):
        self.db=DB(r"FND\SQL\DB\chinook.db","albums")

    def albumEkle(Self):
        sonuc=self.db.insert(alaln=["Title","ArtistId"],deger=["'bombabomba.com'"])
        if sonuc==1:
            return True
        else:
            return False