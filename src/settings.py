# -*- coding: utf-8 -*-

# URI mongoDB
MONGO_URI = ""

# local mongoDB
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
# MONGO_DBNAME = 'apitest'


RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

pic = {

    'item_title': 'picture',

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
        'pic': {
            'type': 'media',
        },

        'born': {
            'type': 'datetime',
        },

        'active': {
            'type': 'boolean',
            'default': True
        }
    }
}

EXTENDED_MEDIA_INFO = ['content_type', 'name', 'length']

# Enable URL_PREFIX.  Used in conjunction with API_VERSION to build
# API Endpoints of the form <base_route>/<url_prefix>/<api_version>/
URL_PREFIX = 'api'

# Enable API Versioning.  This will force API Calls to follow a form of
# <base_route>/<api_version>/<resource_title>/...
API_VERSION = 'v1'

DOMAIN = {'pic': pic}
