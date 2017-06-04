#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

import requests
import json
import random

from pprint import pprint

ENTRY_POINT = 'tristram.herokuapp.com'


def post_image():
    image = [
        {
            'filenmae': 'testName',
            'tag': 'testNag',
            'role': ['author'],
            'image': ['PATH TO PICTURE']
        },
    ]

    r = perform_post('image', json.dumps(image))
    pprint("'image' posted", r.status_code)

    valids = []
    if r.status_code == 201:
        response = r.json()
        if response['_status'] == 'OK':
            for picture in response['_items']:
                if picture['_status'] == "OK":
                    valids.append(picture['_id'])

    return valids


def perform_post(resource, data):
    headers = {'Content-Type': 'application/json'}
    return requests.post(endpoint(resource), data, headers=headers)


def delete():
    r = perform_delete('image')
    print("'image' deleted", r.status_code)


def perform_delete(resource):
    return requests.delete(endpoint(resource))


def endpoint(resource):
    return 'http://%s/%s/api/v1' % (ENTRY_POINT if not sys.argv[1:] else sys.argv[1], resource)


if __name__ == '__main__':
    delete()
    post_image()
