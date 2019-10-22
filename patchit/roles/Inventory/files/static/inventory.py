from datetime import datetime
from pymongo.errors import BulkWriteError
from bson.json_util import dumps
import pymongo
import json
import sys
import socket


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def DBConnection():
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        mydb = myclient['mydatabase']
        mycol = mydb['customers']
        return mycol
    except pymongo.errors.ConnectionFailure as e:
        print ('Could not connect to server: %s', e)
def create():
    try:
        mycol = DBConnection()
        myquery = {'hostName': sys.argv[1]}
        #count = mycol.count()
        #if count == 0:
        print(request.get_json()) 
        mylist = {"$set": 
            "os": {
                "name": sys.argv[2], 
                "version": sys.argv[3], 
             }
        }}

    
        print(mylist)
        x = mycol.update_one(myquery,mylist)
        print(x)
        task = {'status': 'Sucessfully inserted record'}
        res = json.dumps(task)
        res1=json.loads(res)
if _name_ == '_main_':
    create()