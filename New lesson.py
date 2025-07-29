# my_list = []
# my_list.append(5)
# my_list.append(10)
# my_list.append(15)
# print(my_list)
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# print(list1)
#
# my_list = [1, 2, 3, 4, 2]
# my_list.remove(2)
# my_list.pop()
# print(my_list)
#
# my_list = [10, 20, 40, 30, 20]
# index_40 = my_list.index(40)
# print(index_40)
#
# my_list = [1, 2, 2, 3, 2, 4, 2]
# count_2 = my_list.count(2)
# print(count_2)

# numbers = [40, 21, 76, 34, 12, 67]
#
# divisible_by_7 = [x for x in numbers if x % 7 == 0]
# print(divisible_by_7)
#
# greater_than_50 = [x for x in numbers if x > 50]
# print(greater_than_50)
#
# divided = [x / 2 for x in numbers]
# print(divided)
#
# numbers = [40, 21, 76, 34, 12, 67]
# doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

#
# produkt = {
#     "nazwa": "Laptop X200",                      # string
#     "cena": 4599.99,                             # float
#     "dostepny": True,                            # bool
#     "ilosc_sztuk": 25,                           # int
#     "specyfikacja": {                            # zagnieżdżony słownik
#         "procesor": "Intel Core i7",
#         "ram": "16GB",
#         "dysk": "512GB SSD"
#     },
#     "kolory_dostepne": ["czarny", "srebrny"],    # lista
#     "oceny_uzytkownikow": [                      # lista słowników
#         {"uzytkownik": "Anna", "ocena": 5},
#         {"uzytkownik": "Tomek", "ocena": 4}
#     ],
#     "producent": "TechMaster",                   # string
#     "gwarancja_lata": 2,                         # int
#     "kod_produktu": "TM-X200-16GB-512SSD"        # string
# }

# # Wyciągamy nazwę laptopa
# nazwa = produkt["nazwa"]  # dostęp do wartości po kluczu "nazwa"
#
# # Wyciągamy informację o procesorze
# procesor = produkt["specyfikacja"]["procesor"]  # dostęp do klucza zagnieżdżonego słownika
#
# # Kod produktu zamieniony na małe litery
# kod_maly = produkt["kod_produktu"].lower()  # metoda .lower() zamienia tekst na małe litery
#
# # Szukamy oceny użytkownika "Tomek"
# ocena_tomka = None  # na start brak wartości
# for ocena in produkt["oceny_uzytkownikow"]:  # przechodzimy przez listę ocen
#     if ocena["uzytkownik"] == "Tomek":       # sprawdzamy nazwę użytkownika
#         ocena_tomka = ocena["ocena"]         # zapisujemy ocenę
#         break                                # przerywamy pętlę po znalezieniu
#
# # Wyświetlamy wszystkie dane w czytelnej formie
# print("Informacje o produkcie:")
# print(f"Nazwa: {nazwa}")                     # wypisujemy nazwę
# print(f"Procesor: {procesor}")               # wypisujemy procesor
# print(f"Kod produktu (małymi literami): {kod_maly}")  # wypisujemy kod
# print(f"Ocena Tomka: {ocena_tomka}")         # wypisujemy ocenę użytkownika Tomek

# print("Oceny użytkowników:")
#
# for ocena in produkt["oceny_uzytkownikow"]:         # przechodzimy przez każdy słownik w liście ocen
#     imie = ocena["uzytkownik"]                      # pobieramy imię użytkownika
#     wartosc_oceny = ocena["ocena"]                  # pobieramy ocenę
#     print(f"{imie} - {wartosc_oceny}")              # wypisujemy w formacie: Imię - ocena



loty = [
    {
        'model': 'Boeing 737',
        'kierunek': 'Londyn',
        'ilosc_pasażerów': 162,
        'godzina_odlotu': '08:30',
        'lotnisko': 'Warszawa Chopina',
        'cena_biletu': 560.00,
        'pierwsza_klasa': False
    },
    {
        'model': 'Airbus A320',
        'kierunek': 'Paryż',
        'ilosc_pasażerów': 174,
        'godzina_odlotu': '10:15',
        'lotnisko': 'Kraków Balice',
        'cena_biletu': 610.50,
        'pierwsza_klasa': True
    },
    {
        'model': 'Boeing 787 Dreamliner',
        'kierunek': 'Nowy Jork',
        'ilosc_pasażerów': 240,
        'godzina_odlotu': '12:45',
        'lotnisko': 'Warszawa Chopina',
        'cena_biletu': 1980.00,
        'pierwsza_klasa': True
    },
    {
        'model': 'Embraer E175',
        'kierunek': 'Berlin',
        'ilosc_pasażerów': 88,
        'godzina_odlotu': '06:50',
        'lotnisko': 'Gdańsk Rębiechowo',
        'cena_biletu': 420.00,
        'pierwsza_klasa': False
    },
{
        'model': 'Airbus A321',
        'kierunek': 'Barcelona',
        'ilosc_pasażerów': 190,
        'godzina_odlotu': '09:20',
        'lotnisko': 'Poznań Ławica',
        'cena_biletu': 720.00,
        'pierwsza_klasa': False
    },
    {
        'model': 'Boeing 777',
        'kierunek': 'Tokio',
        'ilosc_pasażerów': 310,
        'godzina_odlotu': '23:10',
        'lotnisko': 'Warszawa Chopina',
        'cena_biletu': 3150.00,
        'pierwsza_klasa': True
    },
    {
        'model': 'Airbus A319',
        'kierunek': 'Amsterdam',
        'ilosc_pasażerów': 132,
        'godzina_odlotu': '07:40',
        'lotnisko': 'Wrocław Strachowice',
        'cena_biletu': 495.00,
        'pierwsza_klasa': False
    },
    {
        'model': 'Boeing 767',
        'kierunek': 'Toronto',
        'ilosc_pasażerów': 260,
        'godzina_odlotu': '14:25',
        'lotnisko': 'Warszawa Chopina',
        'cena_biletu': 2480.00,
        'pierwsza_klasa': True
    },
{
        'model': 'Embraer E195',
        'kierunek': 'Oslo',
        'ilosc_pasażerów': 112,
        'godzina_odlotu': '11:05',
        'lotnisko': 'Katowice Pyrzowice',
        'cena_biletu': 540.00,
        'pierwsza_klasa': False
    },
    {
        'model': 'Airbus A330',
        'kierunek': 'Dubai',
        'ilosc_pasażerów': 280,
        'godzina_odlotu': '21:00',
        'lotnisko': 'Warszawa Chopina',
        'cena_biletu': 1890.00,
        'pierwsza_klasa': True
    }
]

# 1. Lista wszystkich modeli samolotów
modele_samolotow = [lot["model"] for lot in loty]
print("Modele samolotów:", modele_samolotow)

# 2. Loty tylko z lotniska "Katowice Pyrzowice"
loty_z_katowic = [lot for lot in loty if lot["lotnisko"] == "Katowice Pyrzowice"]
print("\nLoty z Katowic:", loty_z_katowic)

# 3. Loty z liczbą pasażerów powyżej 250
loty_duzo_pasazerow = [lot for lot in loty if lot["ilosc_pasażerów"] > 250]
print("\nLoty z >250 pasażerami:", loty_duzo_pasazerow)

# 4. Loty do Dubaju z lotniska "Warszawa Chopina"
loty_dubai_warszawa = [lot for lot in loty if lot["kierunek"] == "Dubai" and lot["lotnisko"] == "Warszawa Chopina"]
print("\nLoty do Dubaju z Warszawy:", loty_dubai_warszawa)

# 5. Policz wszystkich pasażerów
suma_pasazerow = sum(lot["ilosc_pasażerów"] for lot in loty)
print("\nŁączna liczba pasażerów:", suma_pasazerow)

# 6. Dodaj do każdego lotu pole 'total' = liczba pasażerów * cena biletu
for lot in loty:
    lot["total"] = lot["ilosc_pasażerów"] * lot["cena_biletu"]

print("\nLoty z dodanym zarobkiem (total):")
for lot in loty:
    print(f"{lot['model']} -> {lot['total']} zł")