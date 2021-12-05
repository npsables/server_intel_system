import os
import json
from flask.logging import default_handler
from flask import Flask

# import src.const as env_const
from src.config_api import FlaskApp

class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        # if isinstance(o, ObjectId):
        #     return str(o)
        # if isinstance(o, datetime.datetime):
        #     return str(o)
        return json.JSONEncoder.default(self, o)


app = FlaskApp(__name__)
app.logger.removeHandler(default_handler)

# try:
#     client = MongoClient('mongodb://admin:admin@127.0.0.1:27017/?authSource=admin')
#     client.server_info()
# except pymongo.errors.ServerSelectionTimeoutError as err:
#     # do whatever you need
#     print('Err:',err)
    
# db =client.address_service

# use the modified encoder class to handle ObjectId & datetime object while jsonifying the response.
app.json_encoder = JSONEncoder
# app.run(host='0.0.0.0', port=80, debug=True)

# import the transformer model
# remember to read the README in folder model
from transformers import McqModel
model = McqModel("model/")