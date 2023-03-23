import requests


def get_all_astronaut():
    res_astronaut = requests.get('http://api.open-notify.org/astros.json')
    res_astronaut.status_code
    response_json = res_astronaut.json()
    for obj in response_json['people']:
        print(f"Name: {obj['name']}\n")
    print(f"Total astronauts: {response_json['number']}")
