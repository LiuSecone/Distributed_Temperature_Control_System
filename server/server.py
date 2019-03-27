#!/usr/bin/python3

import argparse
import json
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post():
    dic = json.loads(request.data)
    log_recorder(dic)
    return process_dict(dic)

def parse_args():
    parser = argparse.ArgumentParser(description='Parsing args...')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--port', type=int, default=6088)
    return parser.parse_args()

def log_recorder(dic):
    pass

# 处理的dict请求包括空调调节的请求和前台的查询请求
# 可以使用数据库等结构来存储
def process_dict(dic):
    pass
    return 'Success!'


if __name__ == '__main__':
    args = parse_args()
    app.run(host=args.host, port=args.port)
