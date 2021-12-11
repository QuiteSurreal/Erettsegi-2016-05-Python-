autók = []
rendszámok = []

def feladat1():
    global autók
    global rendszámok
    rendszám = []
    fájl = open("autok.txt")
    for i in fájl:
        sor = []
        pucérsor = i.strip()
        sor.append(int(pucérsor.split(" ")[0]))
        sor.append(pucérsor.split(" ")[1])
        sor.append(pucérsor.split(" ")[2])
        rendszám.append(pucérsor.split(" ")[2])
        sor.append(int(pucérsor.split(" ")[3]))
        sor.append(int(pucérsor.split(" ")[4]))
        sor.append(int(pucérsor.split(" ")[5]))
        autók.append(sor)
    rendszámok = list(set(rendszám))
    rendszámok.sort()
    print(autók)
    print(rendszámok)

def feladat2():
    print("2. feladat")
    global autók
    for i in range(len(autók)-1, 0, -1):
        if autók[i][5] == 0:
            print(autók[i][0], ". nap rendszám: ", autók[i][2])
            break


def feladat3():
    print("\n3. feladat")
    global autók
    nap = int(input("Nap: "))
    print("Forgalom a(z) ", nap, ". napon:")
    for i in range(len(autók)):
        if autók[i][0] == nap:
            if autók[i][5] == 0:
                print(autók[i][1], autók[i][2], autók[i][3], "ki")
            else:
                print(autók[i][1], autók[i][2], autók[i][3], "be")
    print("\n")

def feladat4():
    print("4. feladat")
    visszahozatlan = 0
    kibe = 0
    global rendszámok
    global autók
    for i in rendszámok:
        for j in range(len(autók)):
            if i == autók[j][2]:
                kibe = autók[j][5]
        if kibe == 0:
            visszahozatlan += 1

    print("A hónap végén ", visszahozatlan, " autót nem hoztak vissza.\n")

def feladat5():
    print("5. feladat")
    global rendszámok
    global autók
    km1 = 0
    km2 = 0
    for i in range(len(rendszámok)):
        for j in range(len(autók)):
            if rendszámok[i] == autók[j][2]:
                km1 = autók[j][4]
                for k in range(len(autók)-1, 0, -1):
                    if rendszámok[i] == autók[k][2]:
                        km2 = autók[k][4]
                        break
                break
        print(rendszámok[i], km2-km1, " km")


def feladat6():
    print("\n6. feladat")
    global autók
    rendszám = ""
    kmki = 0
    kmbe = 0
    távolság = 0
    sofőr = 0
    for i in range(len(autók)):
        if autók[i][5] == 0:
            kmki = autók[i][4]
            rendszám = autók[i][2]
            for j in range(i+1, len(autók)):
                if autók[j][2] == rendszám:
                    kmbe = autók[j][4]
                    if kmbe-kmki > távolság:
                        sofőr = autók[j][3]
                        távolság = kmbe-kmki
                    break
    print("Leghosszabb út: ", távolság, " km, " "személy: ", sofőr)

def feladat7():
    print("\n7. feladat")
    global autók
    rendszám = input("Rendszám: ")
    menetlevél = []
    for i in range(len(autók)):
        sor = []
        if rendszám == autók[i][2]:
            if autók[i][5] == 1:
                continue
            sor.append(autók[i][3])
            sor.append(autók[i][0])
            sor.append(autók[i][1])
            sor.append(autók[i][4])
            for j in range(i+1, len(autók)):
                if autók[j][2] == rendszám:
                    sor.append(autók[j][0])
                    sor.append(autók[j][1])
                    sor.append(autók[j][4])
                    menetlevél.append(sor)
                    break
                if j+1 == len(autók):
                    menetlevél.append(sor)

    fájl = open(rendszám+"_menetlevel.txt", mode="w")
    for j in range(0, len(menetlevél)):
        if len(menetlevél[j]) > 4:
            fájl.write(str(menetlevél[j][0]))
            fájl.write("\t")
            fájl.write(str(menetlevél[j][1]))
            fájl.write(". ")
            fájl.write(str(menetlevél[j][2]))
            fájl.write("\t")
            fájl.write(str(menetlevél[j][3]))
            fájl.write(" km\t")
            fájl.write(str(menetlevél[j][4]))
            fájl.write(". ")
            fájl.write(str(menetlevél[j][5]))
            fájl.write("\t")
            fájl.write(str(menetlevél[j][6]))
            fájl.write(" km")
            fájl.write("\n")
        else:
            fájl.write(str(menetlevél[j][0]))
            fájl.write("\t")
            fájl.write(str(menetlevél[j][1]))
            fájl.write(". ")
            fájl.write(str(menetlevél[j][2]))
            fájl.write("\t")
            fájl.write(str(menetlevél[j][3]))
            fájl.write(" km")
    fájl.close()
    print("Menetlevél kész.")

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
