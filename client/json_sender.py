#!/usr/bin/python3

import requests
import json

def json_sender(url, dic):
    files = json.dumps(dic)
    print(files)
    r = requests.post(url, files)
    print(r.text)


if __name__ == "__main__":
    json_sender('http://localhost:6088/', {'a' : '1', 'b' : '2', 'c' : '3'})
