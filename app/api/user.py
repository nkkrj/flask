from flask_restful import Resource, reqparse
from flask import jsonify

class User(Resource):
    def __init__(self):
      self.reqparse = reqparse.RequestParser(bundle_errors=True)
      super().__init__()

    def get(self):
      return jsonify(data='get_user')

    def post(self):
      return jsonify(data="post_user")
        