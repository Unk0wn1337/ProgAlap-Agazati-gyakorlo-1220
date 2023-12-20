import Lotto

def hatosLotto():
    f = open("huzasok.txt", "r", encoding="utf-8")
    f.readline()
    eredetiSorok = f.readlines()
    f.close()

    feldolgozottSorok = []
    index = 0
    huzasokSzama = 0
    szamokOsszege = 0
    hetenLevoHuzasok = 0
    legnagyobbHuzasMax = 0
    legnagyobbHuzasHet = 0
    legnagyobbHuzasEv = 0
    legnagyobbHuzasHuzas = 0
    while index < len(eredetiSorok):
        lottokOsszesen = Lotto.Lotto(eredetiSorok[index])
        feldolgozottSorok.append(lottokOsszesen)
        huzasokSzama += 1
        if lottokOsszesen.het == 43:
            szamokOsszege += lottokOsszesen.szam
            hetenLevoHuzasok += 1
        if lottokOsszesen.szam > legnagyobbHuzasMax:
            legnagyobbHuzasMax = lottokOsszesen.szam
            legnagyobbHuzasHet = lottokOsszesen.het
            legnagyobbHuzasEv = lottokOsszesen.ev
            legnagyobbHuzasHuzas = lottokOsszesen.huzas

        index += 1
    szamokAtlag = szamokOsszege / hetenLevoHuzasok
    szamokAtlag = round(szamokAtlag, 2)
    print(f"III/A,B\n\t A húzások száma: {huzasokSzama}")
    print(f"III/C\n\t 43.-dik héten húzott számok átlaga: {szamokAtlag}")
    print(f"III/D\n\tAz első legnagyobb kihúzott szám értéke: {legnagyobbHuzasMax}, {legnagyobbHuzasEv}-ben a {legnagyobbHuzasHet}. héten húzták ki , ez volt a {legnagyobbHuzasHuzas}. húzás.")