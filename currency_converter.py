import requests


def print_currencies(currencies):
    print("Available currencies".center(56, "-"))
    left_offset = 0
    right_offset = 8
    for i in range(4):
        print(currencies[left_offset:right_offset])
        left_offset = left_offset + 8
        right_offset = right_offset + 8


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


URL = "https://api.exchangeratesapi.io/latest"
response = requests.get(URL)
print("Wait for response...")
if response.status_code:
    print("@@@ Successful HTTP request @@@\n")
else:
    print("An error has occured")
data = response.json()
list_of_currencies = sorted(data['rates'].keys())

print("Currency Exchanger".center(56, "-"))
print_currencies(list_of_currencies)

while True:
    currency = input("Write currency shortcut you want to exchange: ")
    currency = currency.upper()
    if currency not in list_of_currencies:
        print("There is no such currency!!!\n")
        print_currencies(list_of_currencies)
        continue
    break

while True:
    money = input("Write your money count: ")
    if not is_number(money):
        print("Write proper number!!!")
        continue
    money = float(money)
    break

while True:
    exchange = input("Write currency shortcut you want to be given: ")
    exchange = exchange.upper()

    if exchange == "EUR":
        break  # EUR is standard base

    if exchange not in list_of_currencies:
        print("There is no such currency!!!\n")
        continue
    break

URL_CURRENCY_RATES = URL + "?" + "base=" + currency
response_rates = requests.get(URL_CURRENCY_RATES)
print("Wait for response...")
if response_rates.status_code:
    print("@@@ Successful HTTP request @@@\n")
else:
    print("@@@ An error has occured @@@\n")
rates_data = response_rates.json()

result = float(rates_data['rates'][exchange] * money)
print(f"You will receive about {round(result, 2)} {exchange}")
