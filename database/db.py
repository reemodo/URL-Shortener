
import mongoengine 


def initialize():
     mongoengine.connect('urlshortener', host="mongodb://mongodb/dev" ,alias='core')

     
     
   
  
        
        
