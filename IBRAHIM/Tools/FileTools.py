class FileTool:
    tur = ".csv"
    def __init__(self,*args, **kwargs):
        self.isim = "defter" + FileTool.tur
        self.alan = ["Adı","Soyadı","Telefon"]
        for key,value in kwargs.items():
            if key == "isim":
                self.isim = value + FileTool.tur
            if key == "alan":
                self.alan = value
        self.dosya = None
        self.dosyaLines = None
        self.dosyaAc()
    
    def dosyaAc(self):
        """
        dosyayı açar ve kayıtları okur
        """
        from os import path
        if path.exists(self.isim):
            self.dosya = open(self.isim,"r+")
        else:
            self.dosya = open(self.isim,"w+")
        self.dosyaLines = self.dosya.readlines()
    
    def listeleme(self,liste=[]):
        """
        Gelen Listeyi ekrana belirli bir düzende yazar
        Args:
            liste (list, optional): [description]. Defaults to [].
        """
        if not liste:
            liste = self.dosyaLines
        indis = 0
        for item in liste:
            print(f"{indis+1}",*item.split(";"),end="")
    

    def girisYap(self):
        liste = []
        for item in self.alan:
            liste.append(input(f"{item} Giriniz:"))
        return ";".join(liste) +"\n"


    def ekleme(self):
        self.dosyaLines.append(self.girisYap())
    
    def guncelleme(self):
        self.listeleme()
        kayit = int(input("Güncellemek istediğiniz kaydı seçiniz:"))
        self.dosyaLines[kayit-1] = self.girisYap()

    def silme(self):
        self.listeleme()
        kayit = int(input("Güncellemek istediğiniz kaydı seçiniz:"))
        del self.dosyaLines[kayit-1]

    def kaydet(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writeline(self.dosyaLines)
        self.dosya.flush()
    

    def __del__(self):
        self.dosya.seek(0)
        self.dosya.truncate()
        self.dosya.writeline(self.dosyaLines)
        self.dosya.close()

    
