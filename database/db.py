from pymongo import MongoClient

class db(object):
    url = "localhost:27017"
    database = None
    def initialize():
        client = MongoClient(db.url)
        db.database = client.shortenerURL

    def insert (collection , data):
        db.database.collection.insert(data)

    def find (collection , query):
        return db.database.collection.find(query)

    def find_one (collection , query):
        return db.database.collection.find_one(query)

db.initialize()
print(db.database.list_collection_names())

#mycol= db.Usrers
#mydict = user( "name", "address","email" )
#x = mycol.insert_one(mydict)
#print (x.inserted_id)
