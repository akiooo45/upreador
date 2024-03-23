import requests
import json


username = "admin"  # 账号
password = "302562020"  # 密码

session = requests.Session()


def login():
    url = "http://127.0.0.1:4396/reader3/login"  # reader地址
    data = {"username": username, "password": password, "isLogin": True}
    headers = {
        "Content-Type": "application/json",
    }
    re = session.post(url, data=json.dumps(data), headers=headers)
    print(json.dumps(re.json(), sort_keys=True, indent=4))


def get_bs():
    bs_url = "https://jihulab.com/aoaostar/legado/-/raw/release/cache/71e56d4f1d8f1bff61fdd3582ef7513600a9e108.json"  # 书源地址
    return requests.get(bs_url).json()


def send_bs():
    reader_addr = "http://127.0.0.1:4396/reader3/saveBookSources/"  # reader地址
    data = get_bs()
    headers = {"Content-Type": "application/json"}
    print(session.post(url=reader_addr, headers=headers, json=data).json())


login()
send_bs()
