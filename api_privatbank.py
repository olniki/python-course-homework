import requests


def get_pb_rates(currency_code=''):
    try:
        currency_code = currency_code.upper()
        if currency_code != '' and currency_code != 'USD' and currency_code != 'EUR':
            print('Немає інформації по даній валюті')
            return
        res_privatbank = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
        res_privatbank.status_code
        # Приватбанк повертає лише дві валюти
        if res_privatbank.status_code == 200:
            currency_rates = res_privatbank.json()
            for obj in currency_rates:
                if currency_code != '' and currency_code != obj['ccy']:
                    continue
                else:
                    print(f"Валюта: {obj['ccy']} Покупка: {obj['buy']} Продаж: {obj['sale']}")
        else:
            print('Smth went wrong')
    except:
        print('Network error')
