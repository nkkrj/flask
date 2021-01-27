import os
basedir = os.path.abspath(os.path.dirname(__file__))
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '1234qwer!@#$'
HOST = 'cdb-jx3ochup.gz.tencentcdb.com'
PORT = '10060'
DATABASE = 'eva'

class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTFUL_JSON = {
        'ignore_nan':True
    }