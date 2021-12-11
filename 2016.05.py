pénztár = []
sorszám = 0
név = ""
darabszám = 0
vásárlások = []

def feladat1():
    global vásárlások
    global pénztár
    fájl = open("penztar.txt")
    sor = []
    for i in fájl:
        pucérsor = i.strip()
        pénztár.append(pucérsor)
    for i in range(len(pénztár)):
        if pénztár[i] != "F":
            sor.append(pénztár[i])
        else:
            vásárlások.append(sor)
            sor = []
            continue
    print(pénztár)
    print(vásárlások)

def feladat2():
    print("2. Feladat")
    global pénztár
    fizetések = 0

    for i in range(len(pénztár)):
        if pénztár[i] == "F":
            fizetések += 1
    print("A fizetések száma: ", fizetések,"\n")

def feladat3():
    print("3. feladat")
    global pénztár
    darab = 0


    for i in range(len(pénztár)):
        if pénztár[i] != "F":
            darab += 1
        else:
            break
    print("Az első vásárló ", darab, (" darab árucikjket vásárolt.\n"))

def feladat4():
    print("4. feladat\n")
    global darabszám
    global pénztár
    global sorszám
    global név
    sorszám = 2
    név = "kefe"
    darabszám = 2

def feladat5():
    print("5. feladat")
    global név
    global vásárlások
    global pénztár
    kefe = 0
    kosár = 0
    kosárminusz = 0
    for i in range(len(vásárlások)-1,0,-1):
        for j in range(len(vásárlások[i])):
            if vásárlások[i][j] == név:
                kosárminusz = i+1
    for i in range(len(vásárlások)):
        for j in range(len(vásárlások[i])):
            if vásárlások[i][j] == név:
                kefe += 1
                kosár = i+1
                break
    print("Az első vásárlás sorszáma: ", kosárminusz)
    print("Az utolsó vásárlás sorszáma: ", kosár)
    print(kefe, " vásárlás során vettek belőle.\n")


def feladat6():
    print("6. Feladat")
    global darabszám
    ár = ertek(darabszám)
    print(darabszám, " darab vételekor fizetendő: ", ár, "\n")


def feladat7():
    print("7. Feladat")
    global vásárlások
    global sorszám
    tömb = []
    tömb2 = []
    for i in range(len(vásárlások[sorszám-1])):
        tömb.append(vásárlások[sorszám-1][i])
    tömb2 = list(set(tömb))
    for i in range(len(tömb2)):
        print(tömb.count(tömb2[i]), tömb2[i])

def feladat8():
    print("8. Feladat")
    global vásárlások
    fizetések = []
    tömb2 = []
    tömb3 = []
    ár = 0
    for i in range(len(vásárlások)):
        tömb = []
        for j in range(len(vásárlások[i])):
            tömb.append(vásárlások[i][j])
        tömb2 = list(set(tömb))
        ár = 0
        sor = []
        for k in range(len(tömb2)):
            ár += ertek(tömb.count(tömb2[k]))
        sor.append(i+1)
        sor.append(ár)
        tömb3.append(sor)
    fájl = open("osszeg.txt", mode="w")
    for i in range(len(tömb3)):
        fájl.write(str(tömb3[i][0]))
        fájl.write(": ")
        fájl.write(str(tömb3[i][1]))
        fájl.write("\n")
    fájl.close()

def ertek(a):
    if a == 1:
        return 500
    if a == 2:
        return 950
    if a == 3:
        return 1350
    if a >= 4:
        return 1350 + (a - 3) * 400

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()


if __name__ == "__main__":
    main()