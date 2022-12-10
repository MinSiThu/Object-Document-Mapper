from datetime import datetime
from pymongo import MongoClient
from pprint import pprint

user_schema = {
    "model_name":"User",
    "model_name_lowercase":"user",
    "model_description":"a collection about user",
    "model_name_plural":"users",
    "model_created_time":datetime.utcnow(),
    "model_updated_time":datetime.utcnow(),

    "fields":[
        {
            "type":"String", 
            "attribute_name":"username",
        },
        {
            "type":"Text",
            "attribute_name":"password",
        },
        {
            "type":"Number",
            "attribute_name":"age",
        },
        {
            "type":"Boolean",
            "attribute_name":"agree to privacy policy",
        },
        {
            "type":"Date",
            "attribute_name":"birthday",
        },
        {
            "type":"Enumeration",
            "attribute_name":"hobbies",
            "predefined_values":["Swimming","Football",'Reading','Gaming','PingPong']
        },
        {
            "type":"JSON",
            "attribute_name":"anythingInJson",
        }
    ]
}

post_schema = {
    "model_name":"Post",
    "model_name_lowercase":"post",
    "model_description":"a collection about post",
    "model_name_plural":"posts",
    "model_created_time":datetime.utcnow(),
    "model_updated_time":datetime.utcnow(),

    "fields":[
        {
            "type":"String", 
            "attribute_name":"title",
        },
        {
            "type":"Text",
            "attribute_name":"content",
        },
        {
            "type":"Date",
            "attribute_name":"birthday",
        },
        {
            "type":"Enumeration",
            "attribute_name":"type_of_post",
            "predefined_values":["Swimming","Football",'Reading','Gaming','PingPong']
        },
        {
            "type":"JSON",
            "attribute_name":"anythingInJson",
        }
    ]
}

client = MongoClient("mongodb://localhost:27017/")
database = client['pymongo']
schema_collection = database['schema_collection']

added_schema_objectId = schema_collection.insert_one(user_schema).inserted_id
print(added_schema_objectId)

serached_schema = schema_collection.find_one({"model_name":"User"})
pprint(serached_schema)

pprint(database.list_collection_names())