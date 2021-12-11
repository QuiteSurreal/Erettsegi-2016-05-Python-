ajtó = []
azonosítók = []
személy = 0



def feladat1():
    global ajtó
    global azonosítók
    fájl = open("ajto.txt")
    for i in fájl:
        sor= []
        csupaszsor = i.strip()
        sor.append(int(csupaszsor.split(" ")[0]))
        sor.append(int(csupaszsor.split(" ")[1]))
        sor.append(int(csupaszsor.split(" ")[2]))
        azonosítók.append(int(csupaszsor.split(" ")[2]))
        sor.append(csupaszsor.split(" ")[3])
        ajtó.append(sor)
    print(ajtó)
    azonosítók = list(set(azonosítók))
    azonosítók.sort()
    print(azonosítók)

def feladat2():
    global ajtó
    print("2. feladat")
    print("Az első belépő:" , ajtó[0][2])
    for i in range(len(ajtó)-1, 0, -1):
        if ajtó[i][3] == "ki":
            print("Az utolsó kilépő:" , ajtó[i][2])
            break

def feladat3():
    global ajtó
    global azonosítók
    fájl = open("athaladas.txt", mode="w")
    for i in range(len(azonosítók)):
        menetel = 0
        for j in range(len(ajtó)):
            if azonosítók[i] == ajtó[j][2]:
                menetel += 1
        fájl.write(str(azonosítók[i]))
        fájl.write(" ")
        fájl.write(str(menetel))
        fájl.write("\n")

def feladat4():
    global ajtó
    global azonosítók
    bennszülöttek = []
    print("\n4. feladat")
    for i in range(len(azonosítók)):
        for j in range(len(ajtó)-1, 0, -1):
            if azonosítók[i] == ajtó[j][2]:
                if ajtó[j][3] == "be":
                    bennszülöttek.append(ajtó[j][2])
                    break
                else:
                    break
    print("A végén a társalgóban voltak: ", end=" ")
    for i in range(len(bennszülöttek)):
        print(bennszülöttek[i], end=" ")

def feladat5():
    global ajtó
    print("\n\n5. feladat")
    létszám = 0
    létszámmax = 0
    óra = 0
    perc = 0
    for i in range(len(ajtó)):
        if ajtó[i][3] == "be":
            létszám += 1
            if létszám > létszámmax:
                létszámmax = létszám
                óra = ajtó[i][0]
                perc = ajtó[i][1]
        else:
            létszám -= 1
    print("Például ", óra,":", perc,"-kor voltak a legtöbben a társalgóban", sep="")

def feladat6():
    global személy
    print("\n6. feladat")
    személy = int(input("Adja meg a személy azonosítóját! "))

def feladat7():
    global ajtó
    global személy
    print("\n7. feladat")
    for i in range(len(ajtó)):
        if ajtó[i][2] == személy:
            if ajtó[i][3] == "be":
                print(ajtó[i][0], ":", ajtó[i][1], "-", sep="", end="")
            else:
                print(ajtó[i][0], ":", ajtó[i][1], sep="")

def feladat8():
    global ajtó
    global személy
    print("\n\n8. feladat")
    összesperc = 0
    beperc = 0
    kiperc = 0
    bennszülött = False
    for i in range(len(ajtó)):
        if ajtó[i][2] == személy:
            if ajtó[i][3] == "be":
                beperc += ajtó[i][0]*60
                beperc += ajtó[i][1]
                bennszülött = True
            else:
                kiperc += ajtó[i][0]*60
                kiperc += ajtó[i][1]
                bennszülött = False
                összesperc += kiperc-beperc
                beperc = 0
                kiperc = 0
    print("A(z) ", személy, ". személy összesen ", összesperc, " percet volt bent, a megfigyelés végén a társalgóban volt.", sep="")










def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()

if __name__ == main():
    main()