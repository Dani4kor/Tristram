#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src import app, settings

app.run(host=settings.HOST, port=settings.PORT)
