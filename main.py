# 1.Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt
# To each file append a random number between 1 and 100.
# Create a summary file (summary.txt) that contains name of the file and number in that file:
import random
import csv


text = ''
for i in range(ord('A'), ord('Z')+1):
    random_number = random.randint(1, 100)
    with open(chr(i) + '.txt', 'w') as file:
        file.write(str(random_number))
    text = text + chr(i) + '.txt: ' + str(random_number)+'\n'

with open('summary.txt', 'w') as sum_file:
    sum_file.write(text)

# 2.Create file with some content. As example you can take this one
# Create second file and copy content of the first file to the second file in upper case.
text = '''
    Тому що ніколи тебе не вирвеш,
    ніколи не забереш,
    тому що вся твоя свобода
    складається з меж,
    тому що в тебе немає
    жодного вантажу,
    тому що ти ніколи не слухаєш,
    оскільки знаєш і так,
    що я скажу,
'''
with open('homework.txt', 'w') as file:
    file.write(text)

with open('homework.txt', 'r') as file:
    text = file.read()

with open('homework_copy.txt', 'w', encoding='utf-8') as file:
    file.write(text.upper())

# Write a program that will simulate user score in a game.
# Create a list with 5 player's names.
# After that simulate 100 games for each player.
# As a result of the game create a list with player's name and his score (0-1000 range).
# And save it to a CSV file.


players_list = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
fields = ['Player name', 'Score']
results_list = []

for player in players_list:
    for i in range(0, 100):
        game_result = [player, str(random.randint(0, 1000))]
        results_list.append(game_result)

with open('game_score.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(results_list)


# 4. Write a script that reads the data from previous CSV file and creates a new file called high_scores.csv where each row contains
# the player name and their highest score. Final score should sorted by descending of highest score
result = {}
with open('game_score.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        print(row)
        if row[0] not in result or result[row[0]] < row[1]:
            result[row[0]] = row[1]
result_list = [[key, value] for key, value in result.items()]
with open('high_scores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)
    writer.writerows(result_list)
