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
    

    