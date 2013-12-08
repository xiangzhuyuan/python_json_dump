#!/usr/bin/python
# -*- coding: utf-8 -*-
import json

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/test')
def test():
    arr = {
        'a': [{'name': '香柱元', 'gender': '男'}],
        'b': [{'name': '杨贵妃', 'gender': '女'}]
    }
    arr1 = {
        'a': [{'name': 'aaaa', 'gender': 'dd'}],
        'b': [{'name': 'bbbb', 'gender': 'bb'}]
    }
    return json.dumps(arr1, ensure_ascii=False)


if __name__ == '__main__':
    app.run()