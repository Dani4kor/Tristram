#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import environ

if 'MONGOLAB_URI' and 'PORT' in environ:
    SERVER_NAME = str(environ.get('HEROKUDOMAIN'))
    PORT = int(environ.get('PORT'))
    MONGO_URI = str(environ.get('MONGOLAB_URI'))
    REDISPORT = str(environ.get('REDISPORT'))
    REDISHOST = str(environ.get('REDISHOST'))

    DEBUG = False
else:
    from configparser import ConfigParser

    config = ConfigParser()
    config.read("mysettings.ini")

    MONGO_URI = config['MONGODB']['MONGO_URI']
    PORT = int(config['SERVERNAME']['PORT'])
    HOST = str(config['SERVERNAME']['HOST'])
    REDISHOST = config['REDIS']['REDISHOST']
    REDISPORT = config['REDIS']['REDISPORT']

    DEBUG = True

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

image = {

    "item_title": 'images',

    "additional_lookup": {
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

PAGINATION = True

# Cache Control HTTP/1.1
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Rate Limitation
LIMIT = (5, 3)
RATE_LIMIT_GET = LIMIT
RATE_LIMIT_POST = LIMIT
RATE_LIMIT_PATCH = LIMIT
RATE_LIMIT_DELETE = LIMIT

JSON = True
XML = False

EMBEDDING = True
PROJECTION = True
