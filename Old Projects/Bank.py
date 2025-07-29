account_email = "dawid@wp.pl"
account_bill = 4500

def show_info():
    print("-------------------")
    return f"Email: {account_email} | Środki: {account_bill:.2f} zł"

def add_money():
    print("-------------------")
    value = input("Podaj kwotę do wpłaty: ")
    try:
        return float(value)
    except ValueError:
        print("Błąd: Podaj poprawną kwotę.")
        return 0

def withdraw_money():
    global account_bill
    print("-------------------")
    value = input("Podaj kwotę do wypłaty: ")
    try:
        value = float(value)
        if value <= account_bill:
            account_bill -= value
            print(f"Wypłacono {value:.2f} zł.")
        else:
            print("Błąd: Nie masz tyle środków.")
    except ValueError:
        print("Błąd: Podaj poprawną kwotę.")
á
def reset_balance():
    global account_bill
    account_bill = 0
    print("Saldo wyzerowane.")

def change_email():
    global account_email
    new_email = input("Podaj nowy adres e-mail: ")
    account_email = new_email
    print("E-mail został zmieniony.")

while True:
    print("\n----Witamy w aplikacji MONEY----")
    print("1. Informacje o koncie")
    print("2. Wpłać pieniądze")
    print("3. Wypłać pieniądze")
    print("4. Wyzeruj środki")
    print("5. Zmień adres e-mail")
    print("6. Zamknij aplikację")

    operation = input("Wybierz opcję (1–6): ")

    match operation:
        case "1":
            print(show_info())
        case "2":
            result = add_money()
            if result > 0:
                account_bill += result
                print(f"Wpłacono {result:.2f} zł na konto.")
        case "3":
            withdraw_money()
        case "4":
            reset_balance()
        case "5":
            change_email()
        case "6":
            print("Dziękujemy za skorzystanie z aplikacji. Do widzenia!")
            break