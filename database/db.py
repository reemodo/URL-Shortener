
from ast import alias
from sqlite3 import connect
import mongoengine 
from pymongo  import MongoClient
from os import getenv

def initialize():
     mongoengine.connect(name='db', alias='core',
                            username=getenv('MONGO_INITDB_ROOT_USERNAME'),
                            password=getenv('MONGO_INITDB_ROOT_PASSWORD'))

  
        
        
#mycol= db.Usrers
#mydict = user( "name", "address","email" )
#x = mycol.insert_one(mydict)
#print (x.inserted_id)
