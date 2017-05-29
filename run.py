#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import app
import os

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
else:
    port = 5000
    host = '0.0.0.0'

app.run(host=host, port=port)