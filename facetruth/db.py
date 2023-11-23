from pymongo import MongoClient

class DB:
    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name

    def connect(self):
        self.client = MongoClient(self.host, self.port)
        self.db = self.client[self.db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def disconnect(self):
        self.client.close()

