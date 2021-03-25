class AnaUrl():
    altUrller = []
    altUrller_skor = {}
    altUrller_skor_reverse = {}
    def __init__(self, url,sozluk,frekans,skor):
        self.anaUrl = url
        self.altUrller = []
        self.sozluk = sozluk
        self.frekans = frekans
        self.skor = skor
    def alturl_ekle(self,altUrl):
        self.altUrller.append(altUrl)
    
    def sortSkor(self,reverse):
        self.altUrller_skor_reverse = reverse

    def alturl_görüntüle(self):
        print('Personel listesi:')
        for url in self.alturl:
            print(url)

    

   