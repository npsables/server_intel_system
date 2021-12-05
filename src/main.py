import os
import logging
import sys
# sys.path.append('..')
from flask import request, jsonify, Flask, render_template, session
from flask_api import status

from src.config_api import ApiResponse
from src import app, db

log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/createdefault', methods=["POST"])
def get():
    pass