#!/usr/bin/env python
import requests
import json

user = "admin"
password = "302562020"


def login():
    data = {"username": "admin", "password": "302562020", "isLogin": True}
    re = requests.post("http://127.0.0.1:4396/reader3/login", data=data)
    print(json.dumps(re.json(), sort_keys=True, indent=4))
    # print(data)


login()
