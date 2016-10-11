from Databases.DatabaseUtil import DBCommander
from pymongo import MongoClient

class MongoUtil:

    def __init__(self, host_name=None, database=None):

        self.host_name = host_name
        self.database = database

    def connect_mongo(self):

        try:
            connect_object = MongoClient(self.host_name, 27017)
        except Exception as e:
            print(e)
        return connect_object

    def insert(self, data=None, collection=None):

        my_database = self.connect_object['test_db']

        collection = my_database[collection]

        collection.insert({'id': 1, 'test_field':  data})



