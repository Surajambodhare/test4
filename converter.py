def currency_converter(amount, from_currency, to_currency):
    conversion_rates = {
        ('USD', 'EUR'): 0.85,
        ('USD', 'GBP'): 0.73,
        ('EUR', 'USD'): 1.18,
        ('EUR', 'GBP'): 0.86,
        ('GBP', 'USD'): 1.37,
        ('GBP', 'EUR'): 1.16,
    }
    
    if (from_currency, to_currency) in conversion_rates:
        rate = conversion_rates[(from_currency, to_currency)]
        converted_amount = amount * rate
        return converted_amount
    else:
        return "Conversion not supported for given currencies."

# Example usage
amount = float(input("Enter amount: "))
from_currency = input("Enter from currency (USD/EUR/GBP): ").upper()
to_currency = input("Enter to currency (USD/EUR/GBP): ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)
if isinstance(converted_amount, str):
    print(converted_amount)
else:
    print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
