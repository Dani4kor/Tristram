#!/usr/bin/env python
# -*- coding: utf-8 -*-


from eve import Eve

app = Eve(__name__, settings='settings.py', template_folder='templates')

from src import views
