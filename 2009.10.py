autoszam = 0
athaladas = []

def feladat1():
    file = open("forgalom.txt")
    text = []
    for i in file:
        stripline = i.strip()
        text.append(stripline)
    elso = True
    for i in text:
        if elso == True:
            autoszam = text
            elso = False
        else:
            sor = []
            sor.append(int(i.split(" ")[0]))
            sor.append(int(i.split(" ")[1]))
            sor.append(int(i.split(" ")[2]))
            sor.append(int(i.split(" ")[3]))
            sor.append(str(i.split(" ")[4]))
            athaladas.append(sor)

def feladat2():
    sorszam = int(input("2. feladat Adja meg a jármű sorszámát"))
    if athaladas[sorszam-1][4] == "F":
        print("A vezető az Alsó város irányába közlekedett")
    else:
        print("A vezető a Felső város irányába közlekedett")

def feladat3():
    print("\n3. feladat")
    van = 0
    utolso = 0
    elotti = 0
    for i in range(len(athaladas)-1, -1, -1):
        if athaladas[i][4] == "A":
            if van == 0:
                utolso = athaladas[i][0]*3600 + athaladas[i][1]*60 + athaladas[i][2]
                van += 1
            else:
                elotti = athaladas[i][0] * 3600 + athaladas[i][1] * 60 + athaladas[i][2]
                break
    megoldas = utolso-elotti
    print("A Felső város irányába tartó utolsó két jármű", megoldas, "másodperc különbséggel érte el az útszakasz kezdetét")

def feladat4():
    print("\n4. feladat")
    orak = []
    for i in range(len(athaladas)):
        orak.append(athaladas[i][0])
    orak = set(orak)
    trashfile = athaladas.copy()
    for i in orak:
        felbelepes = 0
        albelepes = 0
        while i == trashfile[0][0]:
            if trashfile[0][4] == "F":
                felbelepes += 1
            else:
                albelepes += 1
            trashfile.remove(trashfile[0])
            if len(trashfile) == 0:
                break
        print(i, felbelepes, albelepes)

def feladat5():
    print("\n5. feladat")
    gyorsasag = []
    for i in range(len(athaladas)):
        gyorsasag.append(athaladas[i][3])
    trashfile = athaladas.copy()
    gyorsasag.sort()
    for i in range(10):
        for j in range(len(trashfile)):
            if gyorsasag[i] == trashfile[j][3]:
                if trashfile[j][4] == "F":
                    print(trashfile[j][0], trashfile[j][1], trashfile[j][2], "Felső", round(1000/gyorsasag[i], 2))
                else:
                    print(trashfile[j][0], trashfile[j][1], trashfile[j][2], "Alsó", round(1000/gyorsasag[i], 2))

                trashfile.remove(trashfile[j])
                break

def feladat6():
    file = open("also.txt", mode='w')
    ido = []
    sebesseg = []
    for i in range(len(athaladas)):
        if athaladas[i][4] == "F":
            sor = [athaladas[i][0], athaladas[i][1], athaladas[i][2]]
            ido.append(sor)
            sebesseg.append(athaladas[i][3])
    kijutas = idoszamitas(ido, sebesseg)
    elso = True
    for i in range(len(kijutas)):
        if elso == True:
            elso = False
            continue
        elotti = kijutas[i-1][0]*3600 + kijutas[i-1][1]*60 + kijutas[i-1][2]
        jelenszam = kijutas[i][0]*3600 + kijutas[i][1]*60 + kijutas[i][2]
        if elotti > jelenszam:
            kijutas[i] = kijutas[i-1]
    print(kijutas)
    for i in kijutas:
        file.write(str(i[0]))
        file.write(" ")
        file.write(str(i[1]))
        file.write(" ")
        file.write(str(i[2]))
        file.write("\n")

def idoszamitas(ido, sebesseg):
    kijutas = []
    for i in range(len(ido)):
        while sebesseg[i] > 0:
            if sebesseg[i] < 60:
                ido[i][2] += sebesseg[i]
                if ido[i][2] >= 60:
                    ido[i][2] -= 60
                    ido[i][1] += 1
                if ido[i][1] >= 60:
                    ido[i][1] -= 60
                    ido[i][0] += 1
                sebesseg[i] = 0
            else:
                szam = sebesseg[i]//60
                ido[i][1] += szam
                sebesseg[i] -= szam*60
        kijutas.append(ido[i])
    return kijutas


def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()

main()