#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from eve import Eve
from flask import render_template, jsonify
from datetime import datetime
from eve_healthcheck import EveHealthCheck

# Heroku support: bind to PORT if defined, otherwise default to 5000.
if 'PORT' in os.environ:
    port = int(os.environ.get('PORT'))
    host = '0.0.0.0'
else:
    port = 5001
    host = '127.0.0.1'

app = Eve(__name__, settings='settings.py', template_folder='templates')


@app.route('/api/v1/datetime', methods=['GET'])
def get_datetime():
    return jsonify(datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), mimetype='application/json')


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    EveHealthCheck(app, '/healthcheck')
    app.run(host=host, port=port)
