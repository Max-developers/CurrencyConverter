import requests

class CurrencyConverter:
    def __init__(self):
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
        self.base_currency = "USD"  # валюта по умолчанию

    def get_exchange_rates(self, currency):
        response = requests.get(self.api_url + currency)
        if response.status_code != 200:
            raise Exception("Ошибка при получении данных о курсах валют.")
        return response.json()["rates"]

    def convert(self, amount, from_currency, to_currency):
        rates = self.get_exchange_rates(from_currency)
        if to_currency not in rates:
            raise Exception(f"Курс для валюты {to_currency} не найден.")

        converted_amount = amount * rates[to_currency]
        return converted_amount

def main():
    print("Добро пожаловать в конвертер валют!")
    converter = CurrencyConverter()

    while True:
        try:
            amount = float(input("Введите сумму для конвертации: "))
            from_currency = input("Введите валюту для конвертации (например, USD, EUR): ").upper()
            to_currency = input("Введите валюту, в которую хотите конвертировать: ").upper()

            converted_amount = converter.convert(amount, from_currency, to_currency)
            print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        again = input("Хотите конвертировать еще раз? (да/нет): ").strip().lower()
        if again != "да":
            break

if __name__ == "__main__":
    main()

