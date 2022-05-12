import mongoengine
import datetime
{{"originalURL" : " " , "shortURL" : " " , "creationDate" : " " ,"userID" : " " }}
class url(mongoengine.Document):
    originalURL = mongoengine.StringField(required = True, unique = True)
    shortURL = mongoengine.StringField(unique = True, required = True)
    creationDate = mongoengine.DateTimeField(default = datetime.datetime.now)
    userID = mongoengine.EmbeddedDocumentListField(default = " " , required=False)