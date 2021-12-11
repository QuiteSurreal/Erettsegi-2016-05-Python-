jegyekszam = 0
uthossz = 0
ar = 0
jegytar = []

def feladat1():
    global jegyekszam, uthossz, ar
    file = open("eladott.txt")
    stripfile = []
    for i in file:
        stripline = i.strip()
        stripfile.append(stripline)
    elso = True
    for i in stripfile:
        if elso == True:
            jegyekszam, uthossz, ar = int(i.split(" ")[0]), int(i.split(" ")[1]), int(i.split(" ")[2])
            elso = False
            continue
        line = []
        line.append(int(i.split(" ")[0]))
        line.append(int(i.split(" ")[1]))
        line.append(int(i.split(" ")[2]))
        jegytar.append(line)
    print(jegytar)

def feladat2():
    print("2. feladat:")
    print(jegytar[len(jegytar)-1][0], jegytar[len(jegytar)-1][2]-jegytar[len(jegytar)-1][1])

def feladat3():
    print("\n3. feladat:")
    megoldasok = []
    for i in range(len(jegytar)):
        if jegytar[i][1] == 0 and jegytar[i][2] == uthossz:
            megoldasok.append(jegytar[i])
    for i in megoldasok:
        print(i[0], " ", end="")

def feladat4():
    print("\n\n4. feladat:")
    megoldas = 0
    for i in range(len(jegytar)):
        hossz = jegytar[i][2] - jegytar[i][1]
        fizetes = hossz*ar
        szam = int(fizetes % 10)
        if szam != 0 and szam != 5:
            if szam == 1 or szam == 2 or szam == 8 or szam == 9:
                fizetes = round(fizetes, -1)
            else:
                fizetes = 5 * round(fizetes/5)
        megoldas += fizetes
    print(megoldas)


def feladat5():
    print("\n5. feladat")
    elotti = 0
    for i in range(len(jegytar)):
        if jegytar[i][2] != uthossz and jegytar[i][2] > elotti:
            elotti = jegytar[i][2]
    le = 0
    fel = 0
    for i in range(len(jegytar)):
        if jegytar[i][1] == elotti:
            fel += 1
        elif jegytar[i][2] == elotti:
            le += 1
    print(le, "ember szállt le a buszról")
    print(fel, "ember szállt fel a buszra")

def feladat6():
    print("\n6. feladat")
    megallok = []
    for i in range(len(jegytar)):
        if jegytar[i][1] not in megallok:
            megallok.append(jegytar[i][1])
        if jegytar[i][2] not in megallok:
            megallok.append(jegytar[i][2])
    print(len(megallok))

def feladat7():
    file = open("kihol.txt", mode='w')
    #indulas = int(input("Kérem adja meg az út egy pontját!"))
    indulas = 120
    megoldasok = []
    for i in range(len(jegytar)):
        if jegytar[i][1] <= indulas < jegytar[i][2]:
            sor = jegytar[i]
            sor.append(i)
            megoldasok.append(sor)
    megoldasok.sort()
    for i in range(1, 49):
        if len(megoldasok) >= i:
            if megoldasok[i-1][0] == i:
                file.write("\n")
                file.write(str(i))
                file.write(". ülés: ")
                file.write(str(megoldasok[i-1][3]))
                file.write(". utas")
            else:
                file.write("\n")
                file.write(str(i))
                file.write(". ülés: üres")
        else:
            file.write("\n")
            file.write(str(i))
            file.write(". ülés: üres")
    file.close()



def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()

main()