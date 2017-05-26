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




URL_PREFIX='api'

API_VERSION='v1'

DOMAIN = {'pic': pic}
