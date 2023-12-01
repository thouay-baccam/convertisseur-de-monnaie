from forex_python.converter import CurrencyRates

def convertmonnaie(amount, source_currency, target_currency):
    c = CurrencyRates()
    
    try:
        exchange_rate = c.get_rate(source_currency, target_currency)
        converted_amount = amount * exchange_rate
        return converted_amount
    except:
        return None

amount = float(input("Entrez la valeur à convertir : "))
source_currency = input("Entrez la devise source (Exemple : USD) : ").upper()
target_currency = input("Entrez la devise cible (Exemple : EUR): ").upper()

result = convertmonnaie(amount, source_currency, target_currency)

if result is not None:
    print(f"{amount} {source_currency} correspond à {result:.2f} {target_currency}")
else:
    print("Conversion impossible.")