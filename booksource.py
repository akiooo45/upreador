import requests
import json
import urllib.parse


username = "admin"
password = "admin"
remote_booksource = "https://jihulab.com/aoaostar/legado/-/raw/release/cache/1b8256c78b385543b5e8aa6a0d7693c76f8e60d4.json"
reader_addr = "http://127.0.0.1:4396"
session = requests.session()


def login():
    login_url = "/reader3/login"
    url = urllib.parse.urljoin(reader_addr, login_url)
    # print(url)
    data = {"username": username, "password": password, "isLogin": True}
    headers = {
        "Content-Type": "application/json",
    }
    session.post(url, data=json.dumps(data), headers=headers).json()


def deleteBookSource():
    deleteBookSource_url = "/reader3/deleteAllBookSources"
    url = urllib.parse.urljoin(reader_addr, deleteBookSource_url)
    print(session.post(url).json())


def get_remotebs():
    return requests.get(remote_booksource).json()


def send_bs():
    remote_booksource = "/reader3/saveBookSources"
    url = urllib.parse.urljoin(reader_addr, remote_booksource)
    headers = {
        "Content-Type": "application/json",
    }
    data = get_remotebs()
    print(session.post(url, json=data, headers=headers).json())


login()
deleteBookSource()
send_bs()
