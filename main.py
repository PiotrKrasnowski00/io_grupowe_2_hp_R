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
def waluta_dict_na_str():
    waluta_dict = {}
    for waluta in ["galeon", "sykl", "knut"]:
        ilosc = int(input(f"Ile masz {waluta}ów? "))
        if ilosc > 0:
            waluta_dict[waluta] = ilosc

    coins = []
    if waluta_dict.get("galeon", 0) > 0:
        coins.append(str(waluta_dict["galeon"]) + " galeon")
    if waluta_dict.get("sykl", 0) > 0:
        coins.append(str(waluta_dict["sykl"]) + " sykl")
    if waluta_dict.get("knut", 0) > 0:
        coins.append(str(waluta_dict["knut"]) + " knut")
    return " ".join(coins)

# Testowanie funkcji
print(waluta_dict_na_str())

def waluta_str_na_dict(ciag_znakow):
    bilony = ciag_znakow.split()
    cena = {"galeon": 0, "sykl": 0, "knut": 0} 
    for i in range(0, len(bilony), 2):
        wartosc = int(bilony[i]) if bilony[i].isdigit() else 0
        klucz = bilony[i + 1]
        if klucz[0] == 'g':
            cena['galeon'] = wartosc
        elif klucz[0] == 's':
            cena['sykl'] = wartosc
        elif klucz[0] == 'k':
            cena['knut'] = wartosc
    return cena

ciag_znakow = "17 galeon 2 sykl 13 knut"
ceny = waluta_str_na_dict(ciag_znakow)
print(ceny)