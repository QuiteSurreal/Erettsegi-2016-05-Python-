import random

szintek = 0
csapatok = 0
igeny = 0
keresek = []
kerdes = 0
randomszam = 0


def feladat1():
    file = open("igeny.txt")
    global szintek, csapatok, igeny, keresek
    text = []
    for i in file:
        stripline = i.strip()
        text.append(stripline)
    i = 0
    szintek = int(text[i])
    i += 1
    csapatok = int(text[i])
    i += 1
    igeny = int(text[i])
    i += 1
    for j in range(i, len(text), 1):
        sor = []
        sor.append(int(text[j].split(" ")[0]))
        sor.append(int(text[j].split(" ")[1]))
        sor.append(int(text[j].split(" ")[2]))
        sor.append(int(text[j].split(" ")[3]))
        sor.append(int(text[j].split(" ")[4]))
        sor.append(int(text[j].split(" ")[5]))
        keresek.append(sor)
    print(szintek)
    print(csapatok)
    print(igeny)
    print(keresek)

def feladat2():
    global szintek, csapatok, igeny, keresek, kerdes
    #kerdes = input("2. feladat\n Kérem a lift indulási helyét!")
    kerdes = 32

def feladat3():
    global keresek
    print("\n3. feladat\nA lift a ", keresek[len(keresek)-1][5], ". szinten áll az utolsó igény teljesítése után.", sep="")

def feladat4():
    global keresek
    minimum = 100
    maximum = 0
    for i in range(len(keresek)):
        if keresek[i][4] > maximum:
            maximum = keresek[i][4]
        if keresek[i][4] < minimum:
            minimum = keresek[i][4]
        if keresek[i][5] > maximum:
            maximum = keresek[i][5]
        if keresek[i][5] < minimum:
            minimum = keresek[i][5]
    print("\n4. feladat \nA legalacsonyabb sorszáú szint: ", minimum, "\n", "A legmagasabb sorszámú szint: ", maximum, sep="")

def feladat5():
    global keresek
    emberrel = 0
    nelkul = 0
    for i in range(1, len(keresek),1):
        if keresek[i-1][5] > keresek[i-1][4]:
            emberrel += 1
        if keresek[i-1][5] < keresek[i][4]:
            nelkul += 1
    print("\n5. feladat")
    print("A lift ennyiszer indult felfelé emberrel:", emberrel)
    print("A lift ennyiszer indult felfelé ember nélkül:", nelkul)

def feladat6():
    global keresek, csapatok
    csapatszamok = []
    for i in range(1, csapatok+1):
        csapatszamok.append(i)
    for i in range(len(keresek)):
        if keresek[i][3] in csapatszamok:
            csapatszamok.remove(keresek[i][3])
    print("\n6. feladat")
    for i in csapatszamok:
        print(i, end=" ")

def feladat7():
    global keresek, csapatok, randomszam
    print("\n\n7. feladat")
    randomszam = random.randint(1, csapatok)
    print(randomszam)
    csapatkeres = []
    for i in range(len(keresek)):
        if randomszam == keresek[i][3]:
            sor = []
            sor.append(keresek[i][4])
            sor.append(keresek[i][5])
            csapatkeres.append(sor)
    csalas = False
    for i in range(1, len(csapatkeres),1):
        if csapatkeres[i-1][1] != csapatkeres[i][0]:
            csalas = True
            print("A ", csapatkeres[i-1][1], ". és a ", csapatkeres[i][0], ". szint közötti utat tették meg gyalog", "\n", sep="")
    if csalas == False:
        print("Nem bizonyítható szabálytalanság\n")

def feladat8():
    global keresek, randomszam
    file = open("blokkol.txt", mode="w")
    for i in range(len(keresek)):
        if keresek[i][3] == randomszam:
            print("A befejezés ideje: ", keresek[i][0], ":", keresek[i][1], ":", keresek[i][2], sep="")
            indulas = input("Kérem adja meg az indulási emeletet!")
            cel = input("Kérem adja meg a célemeletet!")
            kod = input("Kérem adja meg a feladatkódot!")
            siker = input("Kérem adja meg a feladat sikerességét!")
            file.write("Indulási emelet: " + indulas)
            file.write("\nCélemelet: " + cel)
            file.write("\nFeladatkód: " + kod)
            file.write("\nBefejezés ideje: " + str(keresek[i][0]) + ":" + str(keresek[i][1]) + ":" + str(keresek[i][2]))
            file.write("\nSikeresség: " + siker)
            file.write("\n-----\n")

def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()
    feladat7()
    feladat8()
main()