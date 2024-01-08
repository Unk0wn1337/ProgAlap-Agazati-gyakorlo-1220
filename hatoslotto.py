import Lotto

f = open("huzasok.txt","r",encoding="utf-8")
f.readline()
sorok = f.readlines()
f.close()

def harmasAB():
    index = 0
    while index < len(sorok):
        index+=1
    print(f"III/A,B:\n\tA huzasok szama: {index}")

def harmasC():
    huzottSzamokOsszeg = 0
    huzottSzamokOsztando = 0
    index = 0
    while index < len(sorok):
        Lottok = Lotto.Lotto(sorok[index])
        if Lottok.het == 43:
            huzottSzamokOsszeg += Lottok.szam
            huzottSzamokOsztando += 1
        index+=1
    nemKerekitettAtlag = huzottSzamokOsszeg / huzottSzamokOsztando
    print(f"III/C:\n\tA 43. heten huzott szamok atlaga: {round(nemKerekitettAtlag, 2)}")

def harmasD():
    legnagyobbKihuzottSzam = 0
    legnagyobbKihuzottSzamEv = 0
    legnagyobbKihuzottSzamHet = 0
    legnagyobbKihuzottSzamHuzas = 0

    index = 0
    while index < len(sorok):
        Lottok = Lotto.Lotto(sorok[index])
        if Lottok.szam > legnagyobbKihuzottSzam:
            legnagyobbKihuzottSzam = Lottok.szam
            legnagyobbKihuzottSzamEv = Lottok.ev
            legnagyobbKihuzottSzamHet = Lottok.het
            legnagyobbKihuzottSzamHuzas = Lottok.huzas
        index+=1
    print(f"III/D:\n\tAz elso legnagyobb kihuzott szam erteke: {legnagyobbKihuzottSzam}, {legnagyobbKihuzottSzamEv}-ben, a {legnagyobbKihuzottSzamHet}. heten huztak ki, ez volt a {legnagyobbKihuzottSzamHuzas}. huzas.")



