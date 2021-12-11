telkek = []
paratlan = []

def feladat1():
    global telkek
    file = open("kerites.txt")
    for i in file:
        stripline = i.strip()
        line = []
        line.append(int(stripline.split(" ")[0]))
        line.append(int(stripline.split(" ")[1]))
        line.append(str(stripline.split(" ")[2]))
        telkek.append(line)
    print(telkek)

def feladat2():
    print("2. feladat")
    print("Az eladott telkek száma:", len(telkek))

def feladat3():
    print("3. feladat")
    print("A ", end="")
    if telkek[len(telkek)-1][0] == 0:
        print("páros ", end="")
    else:
        print("páratlan ", end="")
    print("oldalon adták el az utolsó telket.")
    print("Az utolsó telek házszáma: ", end="")
    if telkek[len(telkek)-1][0] == 0:
        print(sum(x.count(0) for x in telkek)*2)
    else:
        print(sum(x.count(1) for x in telkek)*2-1)

def feladat4():
    print("4. feladat")
    paratlan = []
    for i in range(len(telkek)):
        if telkek[i][0] == 1:
            paratlan.append(telkek[i])
    for i in range(len(paratlan)-1):
        if paratlan[i][0] == 1 and paratlan[i+1][0] == 1 and paratlan[i][2] != "#" and paratlan[i][2] != ":" and paratlan[i][2] == paratlan[i+1][2]:
            print("A szomszédossal egyezik a kerítés színe:", i*2-1)
            break

def feladat5():
    print("5. feladat")
    #hazszam = input("Adjon meg egy házszámot! ")
    #hazszam = int(hazszam)
    hazszam = 3
    paros = []
    for i in range(len(telkek)):
        if telkek[i][0] == 1:
            paratlan.append(telkek[i])
        else:
            paros.append(telkek[i])
    helyzet = 0
    szin = ""
    szinek = []
    for i in range(65, 91):
        szinek.append(chr(i))
    #paros
    if hazszam % 2 == 0:
        szin = paros[int(hazszam/2)-1][2]
        helyzet = int(hazszam/2-1)
        for i in szinek:
            if hazszam == 2:
                if paros[0][2] != i and paros[1][2] != i:
                    print(i)
                    break
            elif hazszam > 2 and helyzet < len(paros):
                if paros[helyzet-1][2] != i and paros[helyzet][2] != i and paros[helyzet+1][2] != i:
                    print(i)
                    break
            elif helyzet == len(paros):
                if paros[helyzet-1][2] != i and paros[helyzet][2] != i:
                    print(i)
                    break
    #paratlan
    if hazszam % 2 == 1:
        szin = paratlan[int(hazszam / 2)][2]
        helyzet = int(hazszam / 2)
        for i in szinek:
            if hazszam == 1:
                if paratlan[0][2] != i and paratlan[1][2] != i:
                    print(i)
                    break
            elif hazszam > 1 and helyzet < len(paratlan):
                if paratlan[helyzet-1][2] != i and paratlan[helyzet][2] != i and paratlan[helyzet+1][2] != i:
                    print(i)
                    break
            elif helyzet == len(paratlan):
                if paratlan[helyzet-1][2] != i and paratlan[helyzet][2] != i:
                    print(i)
                    break

def feladat6():
    file = open("utcakep.txt", mode="w")
    utcakep = ""
    for i in range(len(paratlan)):
        for j in range(paratlan[i][1]):
            utcakep = utcakep + (paratlan[i][2])
    utcakep = utcakep + ("\n")
    hazszam = 1
    for i in range(len(paratlan)):
        utcakep = utcakep + str(hazszam)
        if hazszam < 10:
            for j in range(paratlan[i][1]-1):
                utcakep = utcakep + (" ")
        elif hazszam < 100:
            for j in range(paratlan[i][1]-2):
                utcakep = utcakep + (" ")
        else:
            for j in range(paratlan[i][1]-3):
                utcakep = utcakep + (" ")
        hazszam += 2
    print(utcakep)
    file.write(utcakep)
    file.close()







def main():
    feladat1()
    feladat2()
    feladat3()
    feladat4()
    feladat5()
    feladat6()

main()