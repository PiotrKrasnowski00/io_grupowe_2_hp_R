import csv
  
def wyslij_sowe(adresat, tresc_wiadomosci):
    # Symulacja wysyłania sowy
    print(f"Wysłano sowę do: {adresat} z wiadomością: {tresc_wiadomosci}")

def poczta_wyslij_sowy(sciezka_pliku):
    with open(sciezka_pliku, mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        adresat = row['adresat']
        tresc_wiadomosci = row['tresc_wiadomosci']
        koszt_przesylki = float(row['koszt_przesylki'])
        potwierdzenie_odbioru = row['potwierdzenie_odbioru']

        wyslano_sowe = False  # Zakładamy, że na początku sowa nie doleciała

        # Symulacja wysłania sowy - w rzeczywistości ta część będzie zależeć od sposobu wysyłki
        # Tutaj przyjmujemy, że sowa zawsze doleci
        wyslij_sowe(adresat, tresc_wiadomosci)
        wyslano_sowe = True

        if potwierdzenie_odbioru == 'nie':
            rzeczywisty_koszt = koszt_przesylki
        else:
            rzeczywisty_koszt = 0

        # Aktualizacja danych w wierszu
        row['rzeczywisty_koszt'] = rzeczywisty_koszt

    # Zapis do pliku wynikowego
    output_file = f"output_sowy_z_poczty_{sciezka_pliku.split('.')[0]}_{sciezka_pliku.split('.')[1]}.csv"
    with open(output_file, mode='w', newline='') as file:
        fieldnames = ['adresat', 'tresc_wiadomosci', 'koszt_przesylki', 'potwierdzenie_odbioru', 'rzeczywisty_koszt']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)

# Przykładowe użycie
poczta_wyslij_sowy("zad.csv")