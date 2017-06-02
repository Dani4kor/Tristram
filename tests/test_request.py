#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from pprint import pprint

HOST = 'localhost:5001'
ENTERPOINT = '/api/v1/'

ENDPOINT = 'image'

try:
    pprint(requests.get('http://' + HOST +
                        ENTERPOINT + ENDPOINT).json())
except Exception as e:
    print(str(e) + '\n')
