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
