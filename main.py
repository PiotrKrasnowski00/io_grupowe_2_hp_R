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


