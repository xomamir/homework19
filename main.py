import requests
from flask import Flask

app = Flask(__name__)

response: requests.Response = requests.get('https://api.hearthstonejson.com/v1/121569/ruRU/cards.collectible.json')
my_cart = response.json()


@app.route('/')
def index():
    result: str = ""
    for i in my_cart:
        result += f"<h2>Название карты:{i['name']} <br> id:{i['id']}</h2>"
    return result


if __name__ == "__main__":
    app.run(
        port=8080,
        debug=False
    )