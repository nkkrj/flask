from flask_restful import Resource, reqparse
from flask import jsonify
from app.models.demo import Demodb
from app import db

class Demo(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser(bundle_errors=True)
        self.reqparse.add_argument('a', required=True)        
        super().__init__()
    def get(self):
        arr = []
        args = self.reqparse.parse_args()
        print(args)   #请求的参数
        #result = Demodb.query.all() #查询所有数据
        result = Demodb.query.filter(Demodb.name=='test')
        for item in result:
            obj = {'name':'','lat':0,'lon':0,'point_type':''}
            obj['name']= item.name
            obj['lat'] = item.lat
            obj['lon'] = item.lon
            obj['point_type'] = item.point_type
            arr.append(obj)
        return jsonify({'code':0, 'data':arr})
    def post(self):
        args = self.reqparse.parse_args()
        a = args["a"]
        if a == "1":
            print("add")
            demo = Demodb(name="test",lat=13.34,lon=117.3,point_type=3)
            db.session.add(demo)
            db.session.commit()
        elif a == "2":
            print("update")
            result = Demodb.query.filter(Demodb.id == 3).first()
            result.name = "test888"
            db.session.commit()
        elif a == "3":
            print("delete")
            result = Demodb.query.filter(Demodb.id == 3).first()
            db.session.delete(result)
            db.session.commit()
        return "post"