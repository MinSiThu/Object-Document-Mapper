from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
database = client['pymongo']
schema_collection = database['schema_collection']

class ObjectDocumentMapper:
    def __init__(self):
        print("ODM Created")

    def list_schema(self):
        return database.list_collection_names()

    def create_schema(self,schema):
        return schema_collection.insert_one(schema).inserted_id

    def get_schema(self,schemaName):
        return schema_collection.find_one({'model_name':schemaName})

    def create(self,schema,entry):
        objectId = database[schema].insert_one(entry).inserted_id
        return objectId

    def getByQuery(self,schema,query):
        results = database[schema].find(query)
        list = []
        for result in results:
            list.append(result)
        return list

    def updateOne(self,schema,filter,entry):
        result = database[schema].update_one(filter,{"$set":entry})
        return result

    def deleteOne(self,schema,filter):
        result = database[schema].delete_one(filter)
        return result

    def getOne(self,schema):
        result = database[schema].find_one({})
        return result

odm = ObjectDocumentMapper()
# print(odm.create_schema(post_schema))