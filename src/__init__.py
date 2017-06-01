#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

from eve import Eve
from .settings import REDISHOST, REDISPORT

r = redis.Redis(host=REDISHOST, port=REDISPORT)

app = Eve(__name__, settings='settings.py', template_folder='templates', redis=r)

from src import views
