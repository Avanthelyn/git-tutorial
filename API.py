# import requests  # importujemy bibliotekę requests, która pozwala wysyłać zapytania HTTP
#
# # Ustalamy adres URL do API, z którego chcemy pobrać dane
# url = "https://official-joke-api.appspot.com/jokes/random"
#
# # Wysyłamy żądanie GET do podanego adresu URL
# response = requests.get(url)
#
# # Sprawdzamy, czy odpowiedź była poprawna (status kod 200 oznacza sukces)
# if response.status_code == 200:
#     # Zamieniamy odpowiedź z formatu JSON (tekstowego) na słownik Pythona
#     joke_data = response.json()
#
#     # Wydobywamy dane z odpowiedzi
#     setup = joke_data['setup']  # pierwsza część żartu
#     punchline = joke_data['punchline']  # puenta żartu
#
#     # Wyświetlamy żart
#     print("Żart dnia:")
#     print(setup)
#     print(punchline)
# else:
#     # Jeśli coś poszło nie tak (np. brak internetu, API nie działa), pokazujemy błąd
#     print("Błąd podczas pobierania żartu. Status:", response.status_code)


# import requests  # importujemy bibliotekę do zapytań HTTP
#
# # wysyłamy zapytanie do API
# response = requests.get("https://restcountries.com/v3.1/name/eesti")
#
# # przekształcamy odpowiedź JSON na dane Pythona
# data = response.json()
#
# # wybieramy pierwszy element z listy (Estonia)
# estonia = data[0]
#
# # wyciągamy oficjalną nazwę w języku estońskim
# official_name_estonian = estonia['translations']['est']['official']
#
# # wyciągamy symbol waluty (pierwsza z dostępnych)
# currencies = estonia['currencies']
# first_currency = list(currencies.values())[0]
# currency_symbol = first_currency['symbol']
#
# # wyciągamy stolicę (pierwsza z listy)
# capital = estonia['capital'][0]
#
# # wyciągamy nazwę języka (pierwszy z dostępnych)
# languages = estonia['languages']
# first_language = list(languages.values())[0]
#
# # wypisujemy wszystkie dane
# print("Oficjalna nazwa w języku estońskim:", official_name_estonian)
# print("Symbol waluty:", currency_symbol)
# print("Stolica:", capital)
# print("Język:", first_language)

import requests
def all_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,flags,population,continents,capital"
    try:
        response = requests.get(url)
        data = response.json()

        countries = []

        for x in data[:5]:
            country = {
                "Nazwa": x.get("name").get("common"),
                "Populacja": x.get("population"),
                "Flaga": x.get("flags").get("png", "Nie podano"),
                "Kontynenty": ",".join(x.get("continents")),
                "Stolica": ",".join(x.get("capital","Nie podano"))
            }
            countries.append(country)

        print(countries)

        return countries
    except:
        print("Wystąpił błąd")
        return []

countries = all_countries()