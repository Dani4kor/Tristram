# -*- coding: utf-8 -*-


import requests
import pprint
import os


HOST = 'localhost:5001'
ENTERPOINT = '/api/v1/'

ENDPOINT = 'pic'

try:
    pprint.pprint(requests.get('http://' + HOST + ENTERPOINT+ENDPOINT).json())
except Exception as e:
    print str(e) + '\n'
