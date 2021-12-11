from datetime import datetime

sorozatok = []

def feladat1():
    global sorozatok
    heresorozat = []
    file = open("lista.txt")
    for i in file:
        stripline = i.strip()
        heresorozat.append(stripline)
    i = 0
    while i < len(heresorozat):
        sor = []
        for j in range(5):
            if j == 0 and heresorozat[i] != "NI":
                nezesdatum = datetime.strptime(heresorozat[i], '%Y.%m.%d')
                sor.append(nezesdatum)
            elif j == 3:
                sor.append(int(heresorozat[i]))
            else:
                sor.append(heresorozat[i])
            i += 1
        sorozatok.append(sor)
    print(sorozatok)

def feladat2():
    print("2. feladat")
    global sorozatok
    szami = 0
    for i in range(len(sorozatok)):
        if sorozatok[i][0] != "NI":
            szami += 1
    print("A listában", szami, "db vetítési dátummal rendelkező epizód van\n")

def feladat3():
    print("3. feladat")
    global sorozatok
    latottak = 0
    for i in range(len(sorozatok)):
        if sorozatok[i][4] == "1":
            latottak += 1
    print("A listában lévő epizódok", round(latottak/len(sorozatok)*100, 2), "%-át látta.\n")

def feladat4():
    print("4. feladat")
    global sorozatok
    nezes = 0
    for i in range(len(sorozatok)):
        if sorozatok[i][4] == "1":
            nezes += int(sorozatok[i][3])
    hours = nezes // 60
    minutes = nezes % 60
    days = hours // 24
    hours = hours % 24
    print(days, hours, minutes, "\n")

def feladat5():
    print("5. feladat")
    global sorozatok
    bekeres = input("Adjon meg egy dátumot! Dátum= ")
    datum = datetime.strptime(bekeres, '%Y.%m.%d')
    for i in range(len(sorozatok)):
        if sorozatok[i][0] != "NI":
            if sorozatok[i][0] <= datum and sorozatok[i][4] == "0":
                print(sorozatok[i][2], "\t", sorozatok[i][1])

def Hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sz", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev-1
    hetnapja = napok[(ev + ev//4 - ev//100 + ev //400 + honapok[ho-1] + nap) % 7]
    return hetnapja

def feladat7():
    print("7. feladat")
    global sorozatok
    valasztottnap = input("Adja meg a hét egy napját (például cs)! Nap= ")
    megoldasok = []
    for i in range(len(sorozatok)):
        if sorozatok[i][0] != "NI":
            sorozatnap = Hetnapja((sorozatok[i][0].year), sorozatok[i][0].month, sorozatok[i][0].day)
            if sorozatnap == valasztottnap:
                megoldasok.append(sorozatok[i][1])
    megoldasok = set(megoldasok)
    for i in megoldasok:
        print(i)

def feladat8():
    global sorozatok
    cim = []
    for i in range(len(sorozatok)):
        cim.append(sorozatok[i][1])
    cim = set(cim)
    megoldasok = []
    for i in cim:
        ido = 0
        epizodok = 0
        sor = []
        sor.append(i)
        for j in range(len(sorozatok)):
            if i == sorozatok[j][1]:
                epizodok += 1
                ido = ido + sorozatok[j][3]
        sor.append(ido)
        sor.append(epizodok)
        megoldasok.append(sor)
    file = open("summa.txt", mode="w")
    for i in range(len(megoldasok)):
        file.write(megoldasok[i][0])
        file.write(" ")
        file.write(str(megoldasok[i][1]))
        file.write(" ")
        file.write(str(megoldasok[i][2]))
        file.write("\n")
    file.close()

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat7()
    feladat8()

if __name__ == '__main__':
    main()