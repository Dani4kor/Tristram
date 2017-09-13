#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import render_template, jsonify, request
from time import time
from eve_healthcheck import EveHealthCheck

from src import app


@app.route('/api/v1/datetime', methods=['GET'])
def get_datetime():
    return jsonify(datetime=time(), mimetype='application/json')

@app.route('/api/v1/calc', methods=['GET'])
def get_calc():
    args =  dict(request.args) 
    data = ''
    if 'a' and 'b' in args.keys() and len(args.keys()) == 2: 
        data = 'success'
        return jsonify(result = calc(args['a'], args['b']), state=data, mimetype='application/json') 
    else: 
        data = 'fail'
        return jsonify(result = '2 params(a & b) required ', state=data, mimetype='application/json')

def calc(a, b): return int(a[0]) + int(b[0])

@app.route('/')
def hello_world():
    return render_template('index.html')


EveHealthCheck(app, '/healthcheck')
