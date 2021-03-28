class AnaUrl():
    altUrller = []
    altUrller_skor = {}
    altUrller_skor_reverse = {}
    esAnlamli = []
    def __init__(self, url,sozluk,frekans,skor,seviye):
        self.anaUrl = url
        self.altUrller = []
        self.sozluk = sozluk
        self.frekans = frekans
        self.skor = skor
        self.seviye = seviye
    def alturl_ekle(self,altUrl):
        self.altUrller.append(altUrl)
    
    def esAnlamli_ekle(self,esAnlamli):
        self.esAnlamli = esAnlamli
        
    def sortSkor(self,reverse):
        self.altUrller_skor_reverse = reverse
        
    def seviye(self):
        return self.seviye
    
    def altUrller(self):
        return self.altUrller
    
    def anaUrl(self):
        return self.anaUrl
    
    def alturl_görüntüle(self):
        print('Personel listesi:')
        for url in self.alturl:
            print(url)

    

   