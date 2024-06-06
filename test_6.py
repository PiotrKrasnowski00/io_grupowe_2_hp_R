from main import *


slownik = {"galeon": 0,
        "sykl": 0,
        "knut": 13}
ciag = "13 knut"
assert waluta_str_na_dict(ciag) == slownik
print('Test wykonany pomyślnie')