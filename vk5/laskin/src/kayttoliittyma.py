from enum import Enum
from tkinter import ttk, constants, StringVar
from sovelluslogiikka import Sovelluslogiikka

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa():
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, new_value):
        self.sovelluslogiikka.plus(new_value)
        return self.sovelluslogiikka.tulos

class Erotus():
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self, new_value):
        self.sovelluslogiikka.miinus(new_value)
        return self.sovelluslogiikka.tulos

class Nollaus():
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
    
    def suorita(self, new_value):
        self.sovelluslogiikka.nollaa()
        return self.sovelluslogiikka.tulos

class Kumoa():
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka
        
    def suorita(self, new_value):
        self.sovelluslogiikka.kumoa()
        return self.sovelluslogiikka.tulos


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._root = root
        self._sovellus = sovellus
        self.arvo = sovellus.tulos

        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus),
            Komento.EROTUS: Erotus(self._sovellus),
            Komento.NOLLAUS: Nollaus(self._sovellus),
            Komento.KUMOA: Kumoa(self._sovellus)
        }

    
    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        try:
            retrun_val = int(self._syote_kentta.get())
            return retrun_val
        except Exception:
            pass
    
    def tee_toiminto(self, komento):
        self.arvo = self._lue_syote()
        komento_olio = self._komennot[komento]
        result = komento_olio.suorita(self.arvo)
        self._sovellus.tulos = result

    def _suorita_komento(self, komento):
        self.tee_toiminto(komento);

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL
        
        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)

    
