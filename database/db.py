from pymongo import MongoClient

cluster = "localhost:27017"
client = MongoClient(cluster)
db = client.test
print(client.list_database_names())
