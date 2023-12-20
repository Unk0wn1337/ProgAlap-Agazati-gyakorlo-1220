class Lotto:
    def __init__(self, sor:str):
        adatok = sor.strip().split("@")
        self.huzas = int(adatok[0])
        self.ev = int(adatok[1])
        self.het = int(adatok[2])
        self.szam = int(adatok[3])

    def __str__(self):
        return f"huzas:{self.huzas}, ev:{self.ev}, het:{self.het}, szam: {self.szam}"