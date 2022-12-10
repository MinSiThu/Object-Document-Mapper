from datetime import datetime
from pprint import pprint
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")

database = client['pymongo'] # same as client.pymongo
user_collection = database['users'] # same as database.users

user1 = {
    'name':"KaungKaung",
    'age':21,
    'address':'Thailand',
    'created_time':datetime.now()
}

added_user = user_collection.insert_one(user1)
searched_user = user_collection.find_one({"name":"KaungKaung"})
pprint(searched_user)