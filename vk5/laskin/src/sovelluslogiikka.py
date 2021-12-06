class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.edellinen = 0
        self.tulos = tulos

    def miinus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

    def kumoa(self):
        if self.edellinen == 0:
            return
        
        self.aseta_arvo(self.edellinen)
        self.edellinen = 0
