from main import *

slownik = {"galeon": [1, 3, 5],
           "sykl": [18, 20, 10],
           "knut": [30, 40, 7]}
assert sumuj_fundusze(slownik) == {
    "galeon" : 12,
    "sykl" : 0,
    "knut" : 14
}
print('Test wykonany pomyślnie')