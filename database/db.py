
import mongoengine 

class db(object):
    url = "shortenerURL"
    database = None
    
    def initialize():
        client = mongoengine.connect(db.url)
        db.database = client.shortenerURL

    def insert (collection , data):
        db.database.collection.insert(data)

    def find (collection , query):
        return db.database.collection.find(query)

    def find_one (collection , query):
        return db.database.collection.find_one(query)
    def count(collection):
        return db.database.collection.count()
        
        
#mycol= db.Usrers
#mydict = user( "name", "address","email" )
#x = mycol.insert_one(mydict)
#print (x.inserted_id)
