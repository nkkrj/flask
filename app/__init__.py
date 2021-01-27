from flask import Flask, request, g
from .config import Config
from logging.config import dictConfig
from flask_restful import Api
from flask import make_response, current_app
from flask_restful.utils import PY3
from simplejson import dumps
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

path = os.getcwd()

dictConfig({
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s %(message)s',
        }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi', 'file']
        },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
            }, 
        'file':{
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': path + r'/logs/request.log',
            'level': 'INFO'
            },
	'error_file': {
	    'class': 'logging.FileHandler',
	    'formatter': 'default',
	    'filename': path +  r'/logs/gunicorn.error.log',
	    },
	'access_file': {
	    'class': 'logging.FileHandler',
	    'formatter': 'default',
	    'filename': path +  '/logs/gunicorn.access.log',
            },
        },
    'loggers': {
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['error_file'],
            'propagate': True,
            },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['access_file'],
            'propagate': False,
            },
        }
    })

api2 = Api(app, prefix='/api2/', decorators=[])

@api2.representation('application/json')
def output_simplejson(data, code, headers=None):
    """Makes a Flask response with a JSON encoded body"""

    settings = current_app.config.get('RESTFUL_JSON', {})

    # If we're in debug mode, and the indent is not set, we set it to a
    # reasonable value here.  Note that this won't override any existing value
    # that was set.  We also set the "sort_keys" value.
    if current_app.debug:
        settings.setdefault('indent', 2)
        settings.setdefault('sort_keys', not PY3)

    # always end the json dumps with a new line
    # see https://github.com/mitsuhiko/flask/pull/1262
    dumped = dumps(data, **settings) + "\n"

    resp = make_response(dumped, code)
    resp.headers.extend(headers or {})
    return resp

from app import routes