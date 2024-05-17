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
print(ceny)def nadaj_sowe():
    adresat = input("Podaj adresata: ")
    tresc_wiadomosci = input("Podaj treść wiadomości: ")

    potwierdzenie_odbioru_opcje = [True, False]
    odleglosc_opcje = ["lokalna", "krajowa", "dalekobieżna"]
    typ_opcje = ["list", "paczka"]
    specjalna_opcje = ["nie dotyczy", "wyjec", "list gończy"]

    print("\nWybierz potwierdzenie odbioru:")
    for i, opcja in enumerate(potwierdzenie_odbioru_opcje):
        print(f"{i + 1}. {'tak' if opcja else 'nie'}")
    potwierdzenie_odbioru = potwierdzenie_odbioru_opcje[int(input("Wybór (numer): ")) - 1]

    print("\nWybierz odległość:")
    for i, opcja in enumerate(odleglosc_opcje):
        print(f"{i + 1}. {opcja}")
    odleglosc = odleglosc_opcje[int(input("Wybór (numer): ")) - 1]

    print("\nWybierz typ przesyłki:")
    for i, opcja in enumerate(typ_opcje):
        print(f"{i + 1}. {opcja}")
    typ = typ_opcje[int(input("Wybór (numer): ")) - 1]

    print("\nWybierz specjalną opcję:")
    for i, opcja in enumerate(specjalna_opcje):
        print(f"{i + 1}. {opcja}")
    specjalna = specjalna_opcje[int(input("Wybór (numer): ")) - 1]

    wiadomość = f"Adresat: {adresat}\n"
    wiadomość += f"Treść wiadomości: {tresc_wiadomosci}\n"
    wiadomość += f"Potwierdzenie odbioru: {'True' if potwierdzenie_odbioru else 'False'}\n"
    wiadomość += f"Odległość: {odleglosc}\n"
    wiadomość += f"Typ przesyłki: {typ}\n"
    wiadomość += f"Specjalna: {specjalna}\n"

    if typ == "list":
        wiadomość += " Wysłano list."
        if specjalna == "wyjec":
            wiadomość += " To jest wyjec. Uwaga!"
        elif specjalna == "list gończy":
            wiadomość += " To jest list gończy. Bądź ostrożny!"
    elif typ == "paczka":
        wiadomość += " Wysłano paczkę."
        if specjalna == "wyjec":
            wiadomość += " Paczka zawiera wyjca. Uwaga!"
        elif specjalna == "list gończy":
            wiadomość += " Paczka zawiera list gończy. Bądź ostrożny!"

    if odleglosc == "lokalna":
        wiadomość += " Przesyłka jest lokalna."
    elif odleglosc == "krajowa":
        wiadomość += " Przesyłka jest krajowa."
    elif odleglosc == "dalekobieżna":
        wiadomość += " Przesyłka jest dalekobieżna."

    return wiadomość

wiadomosc = nadaj_sowe()
print("\nWygenerowana wiadomość:")
print(wiadomosc)

import csv

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

    return {"PLN": koszt}

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

def dodaj_do_csv(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt = wybierz_sowe_zwroc_koszt(odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt)
    print(f"Koszt wysłania sowy: {koszt_str}")
    potwierdzenie_odbioru_str = "TAK" if potwierdzenie_odbioru else "NIE"
    dane = [adresat, tresc_wiadomosci, koszt_str, potwierdzenie_odbioru_str]
    with open("poczta_nadania_lista.csv", mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(dane)

dodaj_do_csv(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna)

print("Dane zostały dodane do pliku poczta_nadania_lista.csv.")

