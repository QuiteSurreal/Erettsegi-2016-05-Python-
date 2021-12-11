szoveg = str
szotar = []
leghossz = 0


def feladat1():
    global szoveg
    print("1. feladat")
    #szoveg = input("Adja meg a szöveget: ")
    szoveg = "dawadw"
    szovegdone = []
    for i in range(len(szoveg)):
        szovegdone.append(szoveg[i])
    szovegdone = set(szovegdone)
    print(len(szovegdone), "\n")

def feladat2():
    file = open("szotar.txt")
    for i in file:
        line = i.strip()
        szotar.append(line)

def feladat3():
    file = open("abc.txt", mode='w')
    for i in range(len(szotar)):
        sorrend = sorted(szotar[i])
        for j in range(len(sorrend)):
            file.write(sorrend[j])
        file.write("\n")

def feladat4():
    print("4. feladat")
    #elso = input("Kérem adja meg az első szót: ")
    #masodik = input("Kérem adja meg a második szót: ")
    elso = "brudwah"
    masodik = "budwarh"
    if sorted(elso) == sorted(masodik):
        print("Anagramma\n")
    else:
        print("Nem anagramma\n")

def feladat5():
    print("5. feladat")
    #szo = input("Kérem adjon meg egy szót: ")
    szo = "daw"
    megoldasok = []
    for i in range(len(szotar)):
        if sorted(szo) == sorted(szotar[i]):
            megoldasok.append(szotar[i])
    if len(megoldasok) > 0:
        for i in megoldasok:
            print(i)
    else:
        print("Nincs a szótárban anagramma")
    print("\n")

def feladat6():
    global leghossz
    print("6. feladat")
    leghosszabbak = []
    leghossz = 0
    for i in range(len(szotar)):
        if len(szotar[i]) > leghossz:
            leghossz = len(szotar[i])
    for i in range(len(szotar)):
        if len(szotar[i]) == leghossz:
            leghosszabbak.append(szotar[i])
    while len(leghosszabbak) > 0:
        removal = []
        minta = sorted(leghosszabbak[0])
        for i in range(len(leghosszabbak)):
            if sorted(leghosszabbak[i]) == minta:
                print(leghosszabbak[i])
                removal.append(i)
        j = 0
        for i in removal:
            leghosszabbak.remove(leghosszabbak[i-j])
            j += 1
        print("\n")

def feladat7():
    file = open("rendezve.txt", mode='w')
    hossz = 1
    egyezok = []
    while hossz <= leghossz:
        megoldasok = []
        for i in range(len(szotar)):
            if len(szotar[i]) == hossz:
                megoldasok.append(szotar[i])
        print(megoldasok)
        hossz += 1
        while len(megoldasok) > 0:
            removal = []
            minta = sorted(megoldasok[0])
            for i in range(len(megoldasok)):
                if sorted(megoldasok[i]) == minta:
                    file.write(megoldasok[i])
                    file.write(" ")
                    removal.append(i)
            file.write("\n")
            j = 0
            for i in removal:
                megoldasok.remove(megoldasok[i - j])
                j += 1
            if len(megoldasok) == 0:
                file.write("\n")


def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()

if __name__ == main():
    main()