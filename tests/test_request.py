# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

import sys

import requests
import json
import unittest



# import pymongo
#
# from pprint import pprint
# from pymongo import MongoClient
#
# # add local mongo or mongodb URL
# client = MongoClient('mongodb://')
#
# db = client.everest
# pic_collection = db.image
#
# cursor = pic_collection.find({})
# pprint([document for document in cursor])
#


class GetListImagesTestCase(unittest.TestCase):
    def get_image(self):
        image = [{}, ]
        return self.perform_get('image', json.dumps(image))

    def perform_get(self, resource, data):
        headers = {'Content-Type': 'application/json'}
        return requests.get(self.endpoint(resource), data, headers=headers)

    def endpoint(self, resource):
        self.ENTRY_POINT = 'tristram.herokuapp.com'
        self.END_POINT = 'api/v1'
        return 'http://%s/%s/%s' % (self.ENTRY_POINT if not sys.argv[1:] else sys.argv[1], self.END_POINT, resource)

    def test_status(self):
        assert self.get_image().status_code == 200


if __name__ == '__main__':
    unittest.main()
