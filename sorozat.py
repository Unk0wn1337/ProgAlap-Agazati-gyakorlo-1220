import random


def masosdikFeladat():
    print("II/A,B,C: ")
    szamLista = []
    index = 0
    while index < 8:
        randomSzam = random.randint(-100,859)
        szamLista.append(randomSzam)
        index+=1
    index = 0
    while index < len(szamLista):
            if index == 0:
                print("\t",szamLista[index], end="")
            else:
                print(f";{szamLista[index]}", end="")
            index+=1
    index = 0
    print("")
    print("II/D,E")
    index = 0
    tizzeloszhatoak = 0
    while index < len(szamLista):
        if szamLista[index] % 10 == 0:
            tizzeloszhatoak+=1
        index+=1
    print(f"\tTizeloszthatóak: {tizzeloszhatoak}")
    return  f"\tTizeloszthatóak: {tizzeloszhatoak}"



def fileKiir():
    f = open("vegeredmeny.txt","w",encoding="utf-8")
    f.write("II/F")
    f.write(masosdikFeladat())
    f.close()


