import abc
from abc import ABC


class Zviratko(ABC):
    def __init__(self, jmeno):
        self.jmeno = jmeno

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi chutná!")

    @abc.abstractmethod
    def udelej_zvuk(self):
        pass


class Kotatko(Zviratko):
    def udelej_zvuk(self):
        pass

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} mi vůbec nechutná!")
        super().snez(jidlo)


class Stenatko(Zviratko):
    def zastekej(self):
        print(f"{self.jmeno}: Haf!")

    def udelej_zvuk(self):
        pass


class Hadatko(Zviratko):
    def __init__(self, jmeno):
        jmeno = jmeno.replace('s', 'sss')
        jmeno = jmeno.replace('S', 'Sss')
        super().__init__(jmeno)

    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} HAD!")
        super().snez(jidlo)

    def udelej_zvuk(self):
        pass


standa = Hadatko('Stanislav')
standa.snez('myš')

zviratka: list[Zviratko] = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('flákota')


class HadoKocka(Hadatko, Kotatko):
    def snez(self, jidlo):
        print(f"{self.jmeno}: {jidlo} HadoKocka!")
        super().snez(jidlo)


hk = HadoKocka("Moje Jmeno")
hk.snez("JIDLO")
