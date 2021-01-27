#!/usr/bin/env python3
#coding:utf-8

from app import app

if __name__ == '__main__':
    app.run('localhost', port=8888, debug=True)
