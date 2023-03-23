import api_privatbank
import api_giphy
import api_astronaut
import api_weather

# Виводити усі курси валют від ПриватБанку
api_privatbank.get_pb_rates()

# Виводити курс заданий користувачем
user_input = input('Enter the currency: USD or EUR: ')
api_privatbank.get_pb_rates(user_input)

# Завдання з Giphy
user_word_search = input('Enter the word you want to find: ')
api_giphy.get_gifs_by_name(user_word_search)

# Завдання з астронавтами
api_astronaut.get_all_astronaut()

# Завдання з прогнозом погоди
user_city = input('Enter city in english: ')
api_weather.get_forecast(user_city)
