import unittest
import mongomock
from Databases.DatabaseUtil.Mongo.MongoUtil import MongoUtil

class TestDatabase(unittest.TestCase):



    def test_connection(self):

        connection = MongoUtil(host_name="localhost", database="testdb")

        connection.connect_mongo = mongomock.MongoClient()

    def test_insert(self):

        connection = MongoUtil(host_name="localhost", database="testdb")












