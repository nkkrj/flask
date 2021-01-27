from app import app, api2
from flask import g, jsonify
from flask import render_template,send_from_directory

from .api.demo import Demo

from .api.user import User


@app.route('/filedata/<path:filename>') 
def custom_static(filename): 
    return send_from_directory(app.config['CUSTOM_STATIC_PATH'], filename) 

@app.route('/')
def index():
    return render_template('index.html',name='index') 

api2.add_resource(Demo, 'demo')

api2.add_resource(User, 'user')
