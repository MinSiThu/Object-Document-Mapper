import json
from pymongo import MongoClient
from bson import json_util
from pprint import pprint

class ObjectDocumentMapper:
    def __init__(self,mongodb_url,database_name):
        self.client = MongoClient(mongodb_url)
        self.database = self.client[database_name]
        self.schema_collection = self.database['schema_collection'] # This name is fixed name
        print("Database Connection Succeed")

    def parse_json(self,data):
        return json.loads(json_util.dumps(data)) 

    # These code block relates to creating schema
    def list_schema(self):
        return self.database.list_collection_names()

    def create_schema(self,schema):
        return self.schema_collection.insert_one(schema).inserted_id

    def get_schema(self,schemaName):
        return self.schema_collection.find_one({'model_name':schemaName})

    def update_schema(self,schemaName,update_data):
        return self.schema_collection.update_one({"$set":update_data})

    # These code block relates to creating data entries
    def count_entries(self,schema):
        count = self.database[schema].count_documents({})
        return count

    def create(self,schema,entry):
        objectId = self.database[schema].insert_one(entry).inserted_id
        return objectId

    def getAll(self,schema):
        entries = self.database[schema].find({})
        list = []
        for entry in entries:
            list.append(entry)
        return list

    def getByQuery(self,schema,query):
        results = self.database[schema].find(query)
        list = []
        for result in results:
            list.append(result)
        return list

    def updateOne(self,schema,filter,entry):
        result = self.database[schema].update_one(filter,{"$set":entry})
        return result

    def deleteOne(self,schema,filter):
        result = self.database[schema].delete_one(filter)
        return result

    def getOne(self,schema):
        result = self.database[schema].find_one({})
        return result

# print(odm.create_schema(post_schema))