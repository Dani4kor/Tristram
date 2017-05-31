#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import app, settings

app.run(host='localhost', port=settings.PORT)
