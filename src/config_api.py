
import sys
sys.path.append('..')

from typing import Any, Optional

#import dataclasses
#from dataclasses import dataclass
#from dataclasses_json import dataclass_json
from flask import Response, jsonify, Flask
import src.const as const
    
    
#@dataclass
class ApiResponse(Response):
    default_minetype = 'application/json'
    data: Optional[Any] = None
    success: bool = False
    message: Optional[str] = None
    code: Optional[int] = None
    

class FlaskApp(Flask):
    def make_response(self, rv):
        if isinstance(rv, ApiResponse):
            return super().make_response(make_json(rv))

        if isinstance(rv, tuple) and isinstance(rv[0], ApiResponse):
            rv = (make_json(rv[0]),) + rv[1:]
        return super().make_response(rv)

def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d  # For convenience


def make_json(d):
    return jsonify(del_none(dataclasses.asdict(d)))