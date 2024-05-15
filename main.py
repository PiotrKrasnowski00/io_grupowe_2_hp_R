import time
import random

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


def wyslij_sowe(adresat, tresc):
    print(f"Wysyłanie sowy do: {adresat}")
    print("Treść listu:")
    print(tresc)
    time.sleep(1) 


    if random.random() < 0.1:
        return False  
    else:
        return True   


# adresat = "Pierwszy adresat"
# tresc_listu = "Przykładowa treść."
# wynik = wyslij_sowe(adresat, tresc_listu)
# print("Operacja powiodła się:", wynik)

def sumuj_fundusze(fundusz):
    suma_knut = sum(fundusz.get("galeon", [0])) * 17 * 21 + \
                sum(fundusz.get("sykl", [0])) * 21 + \
                sum(fundusz.get("knut", [0]))

    suma_galeon = suma_knut // (17 * 21)
    suma_knut %= (17 * 21)

    suma_sykl = suma_knut // 21
    suma_knut %= 21

    return {
        "galeon": suma_galeon,
        "sykl": suma_sykl,
        "knut": suma_knut
    }

fundusz = {
    "galeon": [1, 3, 5],
    "sykl": [18, 20, 10],
    "knut": [30, 40, 7]
}

print(sumuj_fundusze(fundusz))


