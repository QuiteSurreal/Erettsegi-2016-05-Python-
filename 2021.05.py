melysegek =[]

def feladat1():
    global melysegek, tav
    print("1. feladat")
    file = open("melyseg.txt")
    for i in file:
        stripline = i.strip()
        melysegek.append(int(stripline))
    print("A fájl adatainak száma:", len(melysegek), "\n")

def feladat2():
    global melysegek, tav
    print("2. feladat")
    #tav = int(input("Adjon meg egy távolságértéket! "))
    tav = 9
    print("Ezen a helyen a felszín", melysegek[tav-1], "méter mélyen van.\n")

def feladat3():
    global melysegek
    print("3. feladat")
    erintetlen = 0
    for i in melysegek:
        if i == 0:
            erintetlen += 1
    arany = erintetlen/len(melysegek)*100
    print("Az érintetlen terület aránya", round(arany, 2), "%.\n")

def feladat4():
    global melysegek
    file = open("godrok.txt", mode="w")
    i = 0
    first = True
    while i < len(melysegek):
        while melysegek[i] > 0:
            if melysegek[i-1] == 0 and first == False:
                file.write("\n")
            if melysegek[i+1] > 0 and melysegek[i-1] > 0:
                file.write(" ")
            file.write(str(melysegek[i]))
            i += 1
            first = False
        i += 1

def feladat5():
    global melysegek
    print("5. feladat")
    i = 0
    godorszam = 0
    while i < len(melysegek):
        while melysegek[i] > 0:
            if melysegek[i+1] == 0:
                godorszam += 1
            i += 1
        i += 1
    print("A gödrök száma:", godorszam, "\n")

def feladat6():
    global melysegek, tav
    print("6. feladat", "\na)")
    if melysegek[tav-1] == 0:
        print("Az adott helyen nincs gödör.")
    else:
        kezdet, veg = hata(melysegek, tav)
        print(kezdet, veg, "\nb)")
        melyules = hatb(melysegek, kezdet, veg)
        print(melyules, "\nc)")
        legmelyebb = hatc(melysegek, kezdet, veg)
        print("A legnagyobb mélysége", legmelyebb, "méter.\nd)")
        terfogat = hatd(melysegek, kezdet, veg)
        print("A térfogata", terfogat, "m^3.\ne)")
        vizmennyiseg = hate(melysegek, kezdet, veg)
        print("A vízmennyiség", vizmennyiseg, "m^3")

def hata(melysegek, tav):
    kezdet = 0
    veg = 0
    i = tav-1
    while melysegek[i] > 0:
        i -= 1
    kezdet = i+2
    i = tav-1
    while melysegek[i] > 0:
        i += 1
    veg = i
    return kezdet, veg

def hatb(melysegek, kezdet, veg):
    godor = melysegek[kezdet]
    i = kezdet-1
    while godor <= melysegek[i]:
        godor = melysegek[i]
        i += 1
    while godor >= melysegek[i] > 0:
        godor = melysegek[i]
        i += 1
    if i == veg:
        melyules = True
    else:
        melyules = False
    if melyules:
        melyules = "Folyamatosan mélyül."
    else:
        melyules = "Nem mélyül folyamatosan."
    return melyules

def hatc(melysegek, kezdet, veg):
    i = kezdet-1
    legmelyebb = 0
    while i < veg-1:
        if melysegek[i] > legmelyebb:
            legmelyebb = melysegek[i]
            if legmelyebb == 30:
                break
        i += 1
    return legmelyebb

def hatd(melysegek, kezdet, veg):
    i = kezdet-1
    terfogat = 0
    szelesseg = 10
    while i < veg:
        terfogat += melysegek[i] * szelesseg
        i += 1
    return terfogat

def hate(melysegek, kezdet, veg):
    i = kezdet-1
    vizmennyiseg = 0
    szelesseg = 10
    while i < veg:
        vizmennyiseg += (melysegek[i]-1) * szelesseg
        i += 1
    return vizmennyiseg

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()


main()