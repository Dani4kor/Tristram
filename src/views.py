from flask import render_template, jsonify
from datetime import datetime
from eve_healthcheck import EveHealthCheck

from src import app


@app.route('/api/v1/datetime', methods=['GET'])
def get_datetime():
    return jsonify(datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), mimetype='application/json')


@app.route('/')
def hello_world():
    return render_template('index.html')

EveHealthCheck(app, '/healthcheck')    
