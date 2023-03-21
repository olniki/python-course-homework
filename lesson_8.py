#Task 1
#Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).
low_int, high_int = 3,7
result_list = [i for i in range(low_int, high_int+1)  if i % 2 != 0]
print(len(result_list))

#2. You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary.
salary_list =  [4000,3000,1000,2000]
average_salary = 0
salary_list.sort()
salary_list.pop(0)
salary_list.pop(len(salary_list)-1)
average_salary = sum(salary_list) / len(salary_list)
print(average_salary)

#Practice 1:
#1.Create emtpy dictionary named en_ua_dictionary.
en_ua_dictionary = {}
#Add few key-value pairs to the dictionary. Example: 'red': 'червоний'
en_ua_dictionary['red'] = 'червоний'
en_ua_dictionary['blue'] = 'блакитний'
en_ua_dictionary['green'] = 'зелений'
#Check if the dictionary contains key 'blue' and 'purple'. If not, set their values to unknown.
if 'purple' not in en_ua_dictionary:
    en_ua_dictionary['purple'] = 'unknown'
if 'blue' not in en_ua_dictionary:
    en_ua_dictionary['blue'] = 'unknown'
#Create a loop over existing values and print them to the console in the following format:
#Delete all key-values pairs from the dictionary if the lenght of value is lower than 5.
for color_en,color_ua in en_ua_dictionary.items():
    print(f'{color_en} in Ukrainian is {color_ua}')
    if len(color_ua) < 5:
        en_ua_dictionary.pop(color_en)

#Write a game where user should guess of a capital of the country that you have in your dictionary.

capitals = { 'Ukraine': 'Kyiv',
             'France': 'Paris',
             'Germany': 'Berlin',
             'Italy': 'Rome',
             'USA': 'Washington',
             'Canada': 'Ottawa',
             'Switzerland': 'Bern',
             'Austria': 'Vienna',
             'Belgium': 'Brussels',
             'Sweden': 'Stockholm',
             'Norway': 'Oslo',
             'Denmark': 'Copenhagen',
             'Finland': 'Helsinki',
             'Poland': 'Warsaw',
             'Romania': 'Bucharest',
             'Bulgaria': 'Sofia',
             'Greece': 'Athens'}

# You should show user a random country from the list and ask him to guess the capital.
# If user input right capital, print "You are right!", add him a point and ask him to guess another country.
# If not, you should ask again. User should be able to quit the game by typing "exit".
# You should print current score after each round.
# Also, you should print the final score before user quit the game.
import random
print('Hello! Let\'s play. Guess the capital of the country. To stop the game enter \'exit\'')
score = 0

while True:
    country,capital = random.choice(list(capitals.items()))
    user_answer = input(f'Enter the capital of {country}: ')
    if user_answer == capital:
        score+=1
        print('You are right. You current score is: {score}')
    elif user_answer == 'exit':
        print(f'You total score is: {score}')
        break
    else:
        print('Wrong answer. Try again')



#Task 3
# In an array of integers of length n + 1 (n > 1),
# # every number in the range 1...n appears once except for one number which appears twice (so the array’s length is n+1).
# # # Write an efficient function that finds the number that appears twice.

check_numbers = [1,2,2,3]

def check_duplicates (values: list) -> int:
    for i in check_numbers:
        if check_numbers.count(i) > 1:
            return i
print(check_duplicates(check_numbers))

#Task 4 Intersection
# Given two arrays of numbers where each one contains unique values and is already sorted in ascending order,
# find the number of elements that belong to both arrays.
arr_1 = [1,2,3,4]
arr_2 = [1,2,5,6]

print(len(set(arr_1) & set(arr_2)))

#Task 5. RLE
# Given a string of letters (without numbers), create a string encoding it by the rules where the first character is char itself,
# followed by a number indicating the number of letter repeats.
test_string = 'ABBA'

def string_encoding (text):
    count = 1
    current_char = text[0]
    result = ''
    for i in range(1, len(text)):
        if current_char == text[i]:
            count+=1
        else:
            result += current_char + str(count)
            count = 1
            current_char = text[i]
    result += current_char + str(count)
    return result

print(string_encoding(test_string))