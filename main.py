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