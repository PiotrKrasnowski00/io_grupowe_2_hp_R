def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    knuty = 0
    galeon = 0
    sykl = 0
    if (odleglosc == "lokalna") and (typ == "list"):
        knuty += 2
    elif (odleglosc == "lokalna") and (typ == "paczka"):
        knuty += 7

    if (odleglosc == "krajowa") and (typ == "list"):
        knuty += 12
    elif (odleglosc == "krajowa") and (typ == "paczka"):
        sykl += 1
        knuty += 2

    if (odleglosc == "dalekobiezna") and (typ == "list"):
        knuty += 20
    elif (odleglosc == "dalekobiezna") and (typ == "paczka"):
        sykl += 2
        knuty += 1

    if potwierdzenie_odbioru:
        knuty += 7

    if specjalna == "wyjec":
        knuty += 4
    elif specjalna == "list gonczy":
        knuty += 1

    print(f"Galeon: ", galeon)
    print(f"Sykl: ", sykl)
    print(f"Knut: ", knuty)


wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')    