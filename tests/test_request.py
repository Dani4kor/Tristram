#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

import requests
import json

from pprint import pprint




ENTRY_POINT = 'tristram.herokuapp.com'



def get_image():
    image = [{},]
    r = perform_get('image', json.dumps(image))
    print("'image' GET", r.status_code)
    return r.json()


def perform_get(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.get(endpoint(resource), data, headers=headers)


def endpoint(resource):
    return 'http://%s/api/v1/%s' % (ENTRY_POINT if not sys.argv[1:] else sys.argv[1], resource)


if __name__ == '__main__':
    pprint(get_image())
