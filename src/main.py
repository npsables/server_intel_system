import os
import logging
import sys
import numpy as np
# sys.path.append('..')
from flask import request, jsonify, Flask, render_template, session
from flask_api import status

from src.config_api import ApiResponse
from src import app, model

log = logging.getLogger()
log.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)

# import the transformer model
# remember to read the README in folder model
from src.model import McqModel
model = McqModel("src/model")

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/mass', methods=["GET"])
def get():
    args = request.args
    result = model.inference(args)
    if type(result) is np.int64:
        # when return only correct answer
        return jsonify({"correct_answer": int(result)})
    else:
        # return all probabilities
        answer = [f"answer_{i}" for i in range(4)]
        result = [float(x) for x in result.squeeze()]
        return jsonify(dict(zip(answer, result)))