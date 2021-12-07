import os
import logging
import sys
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
	if type(result) is int:
		# when return only correct answer
		return jsonify({"correct_answer": result})
	else:
		# return all probabilities
		answer = [f"answer_{i}" for i in range(4)]
		return jsonify(dict(zip(answer, result.squeeze())))