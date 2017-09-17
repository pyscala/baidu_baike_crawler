from pymongo import MongoClient


class MongoUtils(object):
    def __init__(self):
        pass

    def getClient(self):
        return MongoClient("mongodb://127.0.0.1:27017")

    def getDB(self, dbName):
        if dbName is None:
            return self.getClient().baidu_baike
        return self.getClient()[dbName]

    def insert_baike_many(self, list):
        try:
            self.getDB(None).baike.insert(list)
        except Exception as e:
            print("insert into baike err : " + str(e))
