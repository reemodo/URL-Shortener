
import mongoengine
import datetime


class url (mongoengine.Document):
    originalURL = mongoengine.StringField(max_length=300,required = True, unique = True)
    shortURL = mongoengine.StringField(max_length=30,unique = True, required = True)
    creationDate = mongoengine.DateTimeField(default = datetime.datetime.now)
    userID =mongoengine.IntField(required=False)
    meta={
          'db_alias' : 'core',
          'collection' : 'url'
    }
    


    