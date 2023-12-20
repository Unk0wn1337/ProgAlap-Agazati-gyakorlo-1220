def elsoFeladat():
    print("I/A,B")
    hetNap = input("\n\tHét napja: ")
    oraNeve = input("\tÓra neve: ")
    ertekeles = int(input("\tÉrtékelés (0-5):"))
    print("")
    if ertekeles < 0:
        print("Az értékelés nem lehet negatív!")
    elif ertekeles > 5:
        print("Az 5 pont feletti értékelés nem elfogadható!")
    else:
        print("I/C")
        print("")
        print("\tKöszönjük az értékelést")
        print("\tÖsszefoglaló:",hetNap,oraNeve,ertekeles)