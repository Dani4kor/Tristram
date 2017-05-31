#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, jsonify
from time import time
from eve_healthcheck import EveHealthCheck

from src import app


@app.route('/api/v1/datetime', methods=['GET'])
def get_datetime():
    return jsonify(datetime=time(), mimetype='application/json')


@app.route('/')
def hello_world():
    return render_template('index.html')


EveHealthCheck(app, '/healthcheck')
