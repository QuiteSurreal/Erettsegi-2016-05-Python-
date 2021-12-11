versenyzőkszáma = 0
sor = []
kód = ""
jóeredmény = ""
pontszám = []

def feladat1():
    print("1. feladat: Az adatok beolvasása\n")
    global jóeredmény
    global versenyzőkszáma
    global sor
    fájl = open("valaszok.txt")
    for sor in fájl:
        táblasor = []
        pucérsor = sor.strip()
        if versenyzőkszáma == 0:
            jóeredmény = pucérsor.split(" ")[0]
        else:
            azonosító = pucérsor.split(" ")[0]
            válasz = pucérsor.split(" ")[1]
            táblasor.append(azonosító)
            táblasor.append(válasz)
            sorok.append(táblasor)
        versenyzőkszáma += 1

def feladat2():
    global versenyzőkszáma
    versenyzőkszáma -= 1
    print("2. feladat: A vetélkedőn ", versenyzőkszáma, " versenyző indult\n")

def feladat3():
    global kód
    kód = input("3. feladat: A versenyző azonosítója = ")
    global sor
    global versenyzőkszáma
    for i in range(versenyzőkszáma):
        if sorok[i][0] == kód:
            print(sorok[i][1], " (a versenyző válasza)\n")

def feladat4():
    print("4. feladat:")
    global sor
    global kód
    global jóeredmény
    global versenyzőkszáma
    válasz = ""
    for i in range(versenyzőkszáma):
        if sorok[i][0] == kód:
            válasz = sorok[i][1]
    print(jóeredmény, "\t(a helyes megoldás)")
    for i in range(0,14):
        if válasz[i] == jóeredmény[i]:
            print("+", end="")
        else:
            print(" ", end="")
    print("\t(a versenyző helyes válaszai)\n")

def feladat5():
    sorszám = int(input("5. feladat: A feladat sorszáma = "))
    global sor
    global versenyzőkszáma
    global jóeredmény
    jópontokkiír = 0
    jópontok = 0
    for i in range(versenyzőkszáma):
        if sorok[i][1][sorszám] == jóeredmény[sorszám]:
            jópontok += 1
    jópontokkiír = jópontok/versenyzőkszáma*100
    print("A feladatra ", jópontok, " fő, a versenyzők ", "%5.2f"% jópontokkiír, "%-a adott helyes választ\n")

def feladat6():
    print("6. Feladat: A versenyzők pontszámának meghatározása\n")
    global jóeredmény
    global sor
    global versenyzőkszáma
    sorokkiír = []
    global pontszám
    for i in range(versenyzőkszáma):
        tábla = []
        pont = 0
        for j in range(0,14):
            if sorok[i][1][j] == jóeredmény[j]:
                if j <= 4:
                    pont += 3
                elif j >= 5 and j <= 9:
                    pont += 4
                elif j >= 10 and j <= 12:
                    pont += 5
                elif j == 13:
                    pont += 6
        tábla.append(sorok[i][0])
        tábla.append(pont)
        pontszám.append(tábla)
    fájl = open("pontok.txt", mode="w")
    for sor in range(versenyzőkszáma):
        fájl.write(pontszám[sor][0])
        fájl.write(" ")
        fájl.write(str(pontszám[sor][1]))
        fájl.write("\n")
    fájl.close()

def feladat7():
    global jóeredmény
    global sor
    global versenyzőkszáma
    global pontszám
    díj = 1
    sor=0

    print("7. Feladat: A verseny legjobbjai:")
    pontszám.sort( key=lambda pontszám: pontszám[1], reverse=True)
    while (1):
        print(díj, ". díj", "(", pontszám[sor][1], "pont) : ", pontszám[sor][0])
        if pontszám[sor][1] == pontszám[sor+1][1]:
            sor += 1
        else:
            sor += 1
            díj += 1
        if díj > 3:
            break


def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()

if __name__ == "__main__":
    main()