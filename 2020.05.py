időjárás = []
város = ""
településnevek = []


def feladat1():
    global időjárás
    global településnevek
    csupaszsor = []
    település = []
    fájl = open("tavirathu13.txt")
    for i in fájl:
        sor = []
        csupaszsor = i.strip()
        sor.append(csupaszsor.split(" ")[0])
        település.append(csupaszsor.split(" ")[0])
        sor.append(csupaszsor.split(" ")[1])
        sor.append(csupaszsor.split(" ")[2][0:3])
        sor.append(int(csupaszsor.split(" ")[2][3:5]))
        sor.append(int(csupaszsor.split(" ")[3]))
        időjárás.append(sor)
    fájl.close()
    településnevek = list(set(település))
    településnevek.sort()
    print(időjárás)
    print(településnevek)

def feladat2():
    print("2. feladat")
    global időjárás
    global város
    város = input("Adja meg egy település kódját! Település: "
    for i in range(len(időjárás)-1, 0, -1):
        if időjárás[i][0] == város:
            print("Az utolsó mérési adat a megadott településről ", időjárás[i][1][0:2], ":", időjárás[i][1][2:4], "-kor érkezett", sep="")
            break

def feladat3():
    print("3. feladat")
    global időjárás
    global város
    hőmérséklet = 0
    maxi = []
    for i in range(len(időjárás)):
        maxi.append(időjárás[i][4])
    index = (maxi.index(min(maxi)))
    print("A legalacsonyabb hőmérséklet: " , időjárás[index][0], " ", időjárás[index][1][0:2], ":", időjárás[index][1][2:4], " ", időjárás[index][4]," fok.", sep="")
    index = (maxi.index(max(maxi)))
    print("A legmagasabb hőmérséklet: ", időjárás[index][0], " ",  időjárás[index][1][0:2], ":", időjárás[index][1][2:4]," " ,  időjárás[index][4], " fok.", sep="")

def feladat4():
    print("4. feladat")
    global időjárás
    szélcsend = False
    for i in range(len(időjárás)):
        if időjárás[i][2] == "000" and időjárás[i][3] == 0:
            print(időjárás[i][0], " ", időjárás[i][1][0:2], ":", időjárás[i][1][2:4], sep="")
            szélcsend = True
    if szélcsend == False:
        print("Nem volt szélcsend a mérések idején.")

def feladat5():
    print("5. feladat")
    global időjárás
    napiközép = []
    global településnevek
    hőmérsékletek = []
    for i in range(len(településnevek)):
        sor = []
        hőmérsékleteksor = []
        óra01, óra07, óra13, óra19 = False, False, False, False
        for j in range(len(időjárás)):
            if időjárás[j][0] == településnevek[i]:
                hőmérsékleteksor.append(időjárás[j][4])
                óra = időjárás[j][1][0:2]
                if óra == "01":
                    sor.append(időjárás[j][4])
                    óra01 = True
                if óra == "07":
                    sor.append(időjárás[j][4])
                    óra07 = True
                if óra == "13":
                    sor.append(időjárás[j][4])
                    óra13 = True
                if óra == "19":
                    sor.append(időjárás[j][4])
                    óra19 = True
        if óra01 and  óra07 and óra13 and óra19:
            napiközép.append(sor)
        else:
            napiközép.append("NA")
        hőmérsékletek.append(hőmérsékleteksor)
    print(napiközép)
    print(hőmérsékletek)
    for i in range(len(napiközép)):
        if napiközép[i] == "NA":
            print(településnevek[i], "NA ; Hőmérséklet-ingadozás: ", max(hőmérsékletek[i])-min(hőmérsékletek[i]))
        else:
            középhő = 0
            for j in range(len(napiközép[i])):
                középhő += napiközép[i][j]
            középhő = round(középhő/len(napiközép[i]))
            print(településnevek[i], középhő , "; Hőmérséklet-ingadozás: ", max(hőmérsékletek[i]) - min(hőmérsékletek[i]))

def feladat6():
    print("6. feladat")
    global időjárás
    global településnevek
    for i in range(len(településnevek)):
        fájl = open(településnevek[i]+".txt", mode="w")
        fájl.write(településnevek[i])
        fájl.write(("\n"))
        for j in range(len(időjárás)):
            if időjárás[j][0] == településnevek[i]:
                fájl.write(időjárás[j][1][0:2]+":"+időjárás[j][1][2:4]+" ")
                for k in range(időjárás[j][3]):
                    print(k, időjárás[j][3])
                    fájl.write("#")
                fájl.write("\n")
    print("A fájlok elkészültek.")





















def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()




if __name__ == main():
    main()
