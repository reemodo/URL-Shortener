


from datetime import datetime
from flask import Flask, flash , redirect, request ,render_template, url_for 
import database.db as database
import hashlib , base64
from database.url import url
import mongoengine
from pymongo import MongoClient
import string
import random 

app = Flask(__name__)


def generate_short_id(longURL): 
    hashresult = hashlib.md5(longURL.encode())
    bytes = base64.b32encode(hashresult.digest())
    return bytes.decode('utf-8')


@app.route('/',methods=['POST','GET'])
def main():
    db=""
  
    db = database.initialize()
    mongoengine.connect(db.name , alias='core')
    if request.method == "POST" :
        insertedURL = request.form["urls"]
        if not insertedURL:
            # i used short_url as error massege becuse of flash is not working
            return render_template('MainHtml.html',short_url ="The URL is required!")
        
        custom_id = request.form['custom_id']
        dbContainURL = url.objects(originalURL = insertedURL).first()
        if dbContainURL is not None: 
            return render_template('MainHtml.html',short_url =request.host_url+dbContainURL.shortURL)
            
        
        if  not custom_id :
            print('hello')      
            custom_id = generate_short_id(insertedURL)[0:5]
            dbContainshortIDs = url.objects(shortURL = custom_id).first()

            while dbContainshortIDs :
                custom_id =generate_short_id(custom_id+datetime.now)[0:5]
                dbContainshortIDs = url.objects(shortURL = custom_id).first()

        else : 
            dbContainshortID = url.objects(shortURL = custom_id).first()
            if dbContainshortID is not None:
                # i used short_url as error massege becuse of flash is not working 
                #flash('Please enter different custom id!')
                print('hello')
                return render_template('MainHtml.html',short_url ='Please enter different custom id! or leave it empty')

            else:
                urlone=url()
                urlone.originalURL = insertedURL
                urlone.shortURL = custom_id
                urlone.save()
                return render_template('MainHtml.html',short_url = request.host_url+custom_id) 
               
        urlone=url()
        urlone.originalURL = insertedURL
        urlone.shortURL = custom_id
        urlone.save()
        return render_template('MainHtml.html',short_url = request.host_url+urlone.shortURL)
            
        
    else :
        return render_template('MainHtml.html')
   

@app.route('/<short_id>')
def redirects(short_id):
    urlexist = url.objects(shortURL = short_id).first()
    if urlexist :
        return redirect(urlexist.originalURL)
    else :
        return '<h1>not valid short url<h1>'

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5002 , debug=True)
