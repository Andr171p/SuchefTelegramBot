import requests


class ActualStock:
    def __init__(self):
        self.url = "https://сушеф.рф/catalog/its-sale/"


print(requests.get(ActualStock().url).text)