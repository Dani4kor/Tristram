#!/usr/bin/env python
# -*- coding: utf-8 -*-

# URI mongoDB

import os

if 'MONGOLAB_URI' in os.environ:
    MONGO_URI = str(os.environ.get('MONGOLAB_URI'))
else:
    with open('mysettings.txt', 'r') as f:
        MONGO_URI = f.readline()

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']



image = {

    'item_title': 'images',

    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'filename'
    },
    'schema': {
        'filename': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 32,
            'required': True,
            'unique': True,
        },
        'tag': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'image': {
            'type': 'media',
        }

    }
}

EXTENDED_MEDIA_INFO = ['content_type', 'name', 'length']

# disable default behaviour
RETURN_MEDIA_AS_BASE64_STRING = False

# return media as URL instead
RETURN_MEDIA_AS_URL = True

# set up the desired media endpoint
# MEDIA_BASE_URL = ''
MEDIA_ENDPOINT = 'image/media'


# Enable URL_PREFIX.  Used in conjunction with API_VERSION to build
# API Endpoints of the form <base_route>/<url_prefix>/<api_version>/
URL_PREFIX = 'api'

# Enable API Versioning.  This will force API Calls to follow a form of
# <base_route>/<api_version>/<resource_title>/...
API_VERSION = 'v1'

DOMAIN = {'image': image}

HATEOAS = True

PROJECTION = True

DEBUG = False