import pymongo


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    #  neither self (the object instance) nor cls (the class) is implicitly
    #  passed as the first argument. They behave like plain functions except
    #  that you can call them from an instance or the class:
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)  # put

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
