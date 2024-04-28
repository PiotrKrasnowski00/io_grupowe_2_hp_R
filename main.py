import time
import random

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
