from flask import Flask
from flask_restful import Api
from resources.logreg import Logreg
import pymysql

app=Flask(__name__)
api=Api(app)

api.add_resource(Logreg,'/login')                                

app.run(port="8055",debug=True)