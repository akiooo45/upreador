import requests
import json

from requests.api import get

username = "admin"
password = "302562020"


def login():
    url = "http://chirsemby.top:4396/reader3/login"
    data = {"username": username, "password": password, "isLogin": True}
    headers = {
        "Content-Type": "application/json",
    }
    re = requests.post(url, data=json.dumps(data), headers=headers)
    print(json.dumps(re.json(), sort_keys=True, indent=4))


login()


def get_booksource():
    booksource_url = "https://jihulab.com/aoaostar/legado/-/raw/release/cache/8274870a1493d7c4e51c41682a8d1e9500457826.json"
    booksource = requests.get(booksource_url)
    return booksource


# @get_booksource
def upload_booksource():
    url = "http://127.0.0.1:1234/reader3/saveBookSources"
    headers = {"Content-Type": "application/json"}
    data = get_booksource()
    re = requests.post(url, data=data, headers=headers)


upload_booksource()
