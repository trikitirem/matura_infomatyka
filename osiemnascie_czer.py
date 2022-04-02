def find_last(plik):
    items = []
    for line in plik.readlines():
        item = line.split(" ")[-1]
        items.append(item)

    return items


def zad1():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")

    ost1 = find_last(plik1)
    ost2 = find_last(plik2)

    ilosc = 0
    for i, item in enumerate(ost1):
        if item == ost2[i]:
            ilosc += 1

    plik1.close()
    plik2.close()

    zapis = open("18_czer/wynik4_1.txt", "w")
    zapis.write(str(ilosc))
    zapis.close()


def pom2(linia):
    splitted = linia.split()
    odd = 0
    even = 0
    for number in splitted:
        if(int(number) % 2) == 0:
            even += 1
        else:
            odd += 1

    if odd == 5 and even == 5:
        return True
    else:
        return False


def zad2():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")

    ilosc = 0
    for line1, line2 in zip(plik1, plik2):
        l1 = pom2(line1)
        l2 = pom2(line2)
        if l1 == True and l2 == True:
            ilosc += 1

    plik1.close()
    plik2.close()


def zad3():
    plik1 = open("./18_czer/przyklad1.txt", "r")
    plik2 = open("./18_czer/przyklad2.txt", "r")



    plik1.close()
    plik2.close()

