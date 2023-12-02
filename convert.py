from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency, history):
    c = CurrencyRates()
    if c.get_rate(from_currency, to_currency) is None:
        print("Conversion impossible. Veuillez vérifier les codes de devise.")
        return
    converted_amount = c.convert(from_currency, to_currency, amount)
    print(f"{amount} {from_currency} équivaut à {converted_amount:.2f} {to_currency}")
    history.append({'amount': amount, 'from_currency': from_currency, 'to_currency': to_currency, 'converted_amount': converted_amount})

def display_history(history):
    print("\nHistorique des conversions :")
    for entry in history:
        print(f"{entry['amount']} {entry['from_currency']} -> {entry['converted_amount']} {entry['to_currency']}")

def main():
    conversion_history = []
    while True:
        amount = float(input("Veuillez saisir la valeur à convertir : "))
        from_currency = input("Veuillez saisir la devise source (Exemple : USD) : ").upper()
        to_currency = input("Veuillez saisir la devise cible (Exemple : EUR) : ").upper()
        convert_currency(amount, from_currency, to_currency, conversion_history)
        another_conversion = input("Une autre conversion ? (Oui/Non) : ").lower()
        if another_conversion != 'oui':
            display_history(conversion_history)
            break

main()