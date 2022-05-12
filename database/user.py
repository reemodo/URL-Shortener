
import mongoengine 
import  datetime
class user(mongoengine.Document):
    name = mongoengine.StringField(required = True, unique = True)
    email = mongoengine.StringField(unique = True, required = True)
    userID = mongoengine.FloatField(required = False)
    creationDate = mongoengine.DateTimeField(default = datetime.datetime.now)