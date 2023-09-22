import requests
import json


def parse(url):
    r = requests.get(url)
    jsonData = r.json()['chartPositions']
    result = {}
    

    for data in jsonData:
        position = data["chartPosition"]["position"]
        artists = [art["name"] for art in data["track"]["artists"]]
        name = data["track"]["title"]
        
        result[position] = {
            name: artists
        }

    return result





if __name__ == "__main__":
    YANDEX_URL = 'https://music.yandex.ru/handlers/main.jsx?what=chart&lang=ru&external-domain=music.yandex.ru&overembed=false&ncrnd=0.4346034032624708'

    with open("charts.json", "w") as file:
        json.dump(parse(YANDEX_URL), file, ensure_ascii=False)
    file.close()
