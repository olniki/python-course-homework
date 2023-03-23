import api_privatbank

# Виводити усі курси валют від ПриватБанку
api_privatbank.get_pb_rates()

# Виводити курс заданий користувачем
user_input = input('Enter the currency: USD or EUR: ')
api_privatbank.get_pb_rates(user_input)
