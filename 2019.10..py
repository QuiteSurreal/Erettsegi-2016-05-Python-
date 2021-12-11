utasok = []

def feladat1():
    fájl = open("utasadat.txt")
    global utasok
    for i in fájl:
        sor = []
        csupaszsor = i.strip()
        sor.append(int(csupaszsor.split(" ")[0]))
        dátum = int(csupaszsor.split(" ")[1][0:8])
        óra = csupaszsor.split(" ")[1][9:]
        sor.append(dátum)
        sor.append(óra)
        sor.append(int(csupaszsor.split(" ")[2]))
        sor.append(csupaszsor.split(" ")[3])
        sor.append(int(csupaszsor.split(" ")[4]))
        utasok.append(sor)
    fájl.close()

def feladat2():
    global utasok
    print("2. feladat")
    print("A buszra", len(utasok), "utas akart felszállni.")

def feladat3():
    global utasok
    print("3. feladat")
    elutasítások = 0
    for i in range(len(utasok)):
        if utasok[i][5] == 0:
            elutasítások += 1
        if utasok[i][5] < utasok[i][1] and utasok[i][5] > 10:
            elutasítások += 1
    print("A buszra", elutasítások, "utas nem szállhatott fel.")

def feladat4():
    global utasok
    print("4. feladat")
    megállók = []
    legtöbb = 0
    hol = 0
    for i in range(len(utasok)):
        megállók.append(utasok[i][0])
    for i in range(len(megállók)):
        if  megállók.count(i) > legtöbb:
            legtöbb = megállók.count(i)
            hol = i
    print("A legtöbb utas (" , legtöbb, " fő) a ", hol, ". megállóban próbált felszállni.", sep="")

def feladat5():
    global utasok
    print("5. feladat")
    kedvezményes = 0
    ingyenes = 0
    for i in range(len(utasok)):
        if utasok[i][5] != 0:
            if utasok[i][5] >= utasok[i][1] and utasok[i][5] > 10:
                if utasok[i][4] == "TAB" or utasok[i][4] == "NYB":
                    kedvezményes += 1
                if utasok[i][4] == "NYP" or utasok[i][4] == "RVS" or utasok[i][4] == "GYK":
                    ingyenes += 1
    print("Ingyenesen utazók száma:", ingyenes, "fő")
    print("A kedvezményesen utazók száma:", kedvezményes, "fő")

def feladat7():
    global utasok
    fájl = open("figyelmeztetes.txt", mode="w")
    for i in range(len(utasok)):
        if utasok[i][5] <= 10:
            continue
        dátum1 = str(utasok[i][1])
        dátum2 = str(utasok[i][5])
        e1 = int(dátum1[0:4])
        h1 = int(dátum1[5:6])
        n1 = int(dátum1[6:8])
        e2 = int(dátum2[0:4])
        h2 = int(dátum2[5:6])
        n2 = int(dátum2[6:8])
        elteltnapok = napokszama(e1, h1, n1, e2, h2, n2)
        if elteltnapok <= 3 and elteltnapok >= 0:
            fájl.write(str((utasok[i][3])))
            fájl.write(" ")
            fájl.write(str(e2))
            fájl.write("-0")
            fájl.write(str(h2))
            fájl.write("-")
            fájl.write(str(n2))
            fájl.write("\n")
    fájl.close()

def napokszama(e1, h1, n1, e2, h2, n2):
    h1 = (h1 + 9) % 12
    e1 = e1 - h1 // 10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    return d2-d1

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat7()


if __name__ == main():
    main()