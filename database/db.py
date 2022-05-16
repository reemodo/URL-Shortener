
import mongoengine 
from pymongo  import MongoClient
from os import getenv

def initialize():
     client =MongoClient('mongodb',
                         username='root', 
                         password='pass',
                         authSource="admin")
     return client['urlshortener']
     
     
   
  
        
        
