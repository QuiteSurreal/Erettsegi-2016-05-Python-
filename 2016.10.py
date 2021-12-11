import datetime
hivasok = []
hour12 = datetime.datetime(1, 1, 1, 12, 0, 0)
hour8 = datetime.datetime(1, 1, 1, 8, 0, 0)

def feladat2():
    global hivasok
    file = open("hivas.txt")
    text = []
    for i in file:
        line = []
        stripline = i.strip()
        line.append(int(i.split(" ")[0]))
        line.append(int(i.split(" ")[1]))
        line.append(int(i.split(" ")[2]))
        line.append(int(i.split(" ")[3]))
        line.append(int(i.split(" ")[4]))
        line.append(int(i.split(" ")[5]))
        text.append(line)
    for i in range(len(text)):
        startdate = datetime.datetime(1, 1, 1, text[i][0], text[i][1], text[i][2])
        stopdate = datetime.datetime(1, 1, 1, text[i][3], text[i][4], text[i][5])
        line = []
        line.append(startdate)
        line.append(stopdate)
        hivasok.append(line)

def feladat3():
    print("3. feladat")
    megoldasok = []
    for i in range(23):
        megoldasok.append(0)
    for i in range(len(hivasok)):
        orak = int((hivasok[i][0].hour))
        megoldasok[orak] += 1
    for i in range(len(megoldasok)):
        if megoldasok[i] > 0:
            print(i, megoldasok[i])

def feladat4():
    print("\n4. feladat")
    leghosszabb = 0
    sorszam = 0
    for i in range(len(hivasok)):
        #hivhossz = mpbe(int(hivasok[i][1].hour), int(hivasok[i][1].minute), int(hivasok[i][1].second)) - mpbe(int(hivasok[i][0].hour), int(hivasok[i][0].minute), int(hivasok[i][0].second))
        hivhossz = int((hivasok[i][1] - hivasok[i][0]).total_seconds())
        if hivhossz > leghosszabb:
            leghosszabb = hivhossz
            sorszam = i+1
    print("A leghosszabb ideig vonalban levo hivo ", sorszam, ". sorban szerepel, a hivas hossza: ", leghosszabb, " masodperc.", sep="")

def feladat5():
    print("\n5. feladat")
    #bekeres = list(input("Adjon meg egy idopontot! (ora perc masodperc) ").split(" "))
    bekeres = [10, 11, 12]
    intime = datetime.datetime(1, 1, 1, int(bekeres[0]), int(bekeres[1]), int(bekeres[2]))
    varakozok = 0
    sorszam = 0
    if hour8 <= intime < hour12:
        for i in range(len(hivasok)):
            if hivasok[i][1] >= intime and hivasok[i][0] < intime:
                sorszam = i+1
                j = i+1
                while hivasok[i][1] > hivasok[j][1]:
                    varakozok += 1
                    j += 1
                break
            elif hivasok[i][1] >= intime and hivasok[i][0] > intime:
                print("Nem volt beszélő.")
                break
        print("A varakozok szama: ", varakozok," a beszelo a ",  sorszam, ". hivo.", sep="")

def feladat6():
    print("\n6. feladat")
    elozo = hour8
    legnagyobb = hour8
    sorszam = 0
    varakozas = hour8
    for i in range(len(hivasok)):
        if hivasok[i][0] < hour12 and hivasok[i][1] >= legnagyobb:
            elozo = legnagyobb
            legnagyobb = hivasok[i][1]
            sorszam = i+1
            var = mpbe(int(hivasok[i][1].hour), int(hivasok[i][1].minute), int(hivasok[i][1].second))
            var = var - mpbe(int(hivasok[i][0].hour), int(hivasok[i][0].minute), int(hivasok[i][0].second))
            var2 = mpbe(int(hivasok[i][1].hour), int(hivasok[i][1].minute), int(hivasok[i][1].second)) - mpbe(int(elozo.hour), int(elozo.minute), int(elozo.second))
            varakozas = var - var2
    print("Az utolso telefonalo adatai a(z) ", sorszam, ". sorban vannak, ", varakozas, " masodpercig vart.", sep="")

def feladat7():
    print("7. feladat")
    file = open("sikeres.txt", mode='w')
    megoldasok = []
    jelenlegi = hour8
    for i in range(len(hivasok)):
        if hivasok[i][1] >= hour8 and hivasok[i][0] < hour12:
            if hivasok[i][1] >= jelenlegi:
                line = []
                line.append(i+1)
                line.append(hivasok[i][0])
                line.append(hivasok[i][1])
                megoldasok.append(line)
                jelenlegi = hivasok[i][1]
    for i in range(len(megoldasok)):
        file.write(str(megoldasok[i][0]))
        file.write(" ")
        file.write(str(megoldasok[i][1].hour))
        file.write(" ")
        file.write(str(megoldasok[i][1].minute))
        file.write(" ")
        file.write(str(megoldasok[i][1].second))
        file.write(" ")
        file.write(str(megoldasok[i][2].hour))
        file.write(" ")
        file.write(str(megoldasok[i][2].minute))
        file.write(" ")
        file.write(str(megoldasok[i][2].second))
        file.write("\n")

    file.close()




def mpbe(o, p, mp):
    return(o*3600+p*60+mp)

def sectohour(s):
    m = s// 60
    s = s-m*60
    h = m// 60
    m = m-h*60
    print(h, m, s)

def main():
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    sectohour(3667)



main()