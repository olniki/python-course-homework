import json
from urllib import parse, request


def get_gifs_by_name(name):
    try:
        url = "http://api.giphy.com/v1/gifs/search"

        params = parse.urlencode({
            "q": name,
            "api_key": "",
            "limit": "3"
        })

        with request.urlopen("".join((url, "?", params))) as response:
            data = json.loads(response.read())

        for obj in data['data']:
            print(obj['url'])
    except:
        print('Error')
