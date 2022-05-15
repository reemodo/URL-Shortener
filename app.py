


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

@app.route('/') 
def index():
    return render_template('MainHtml.html')

@app.route('/main',methods=['POST','GET'])
def main():
    db=""
    try:
        db = database.initialize()
        mongoengine.connect(db.name , alias='core')
        if request.method == "POST" :
            

            insertedURL = request.form["url"]
            if not insertedURL:
                # i used short_url as error massege becuse of flash is not working
                return render_template('MainHtml.html',short_url ="The URL is required!")
            
            custom_id = request.form['custom_id']
            dbContainURL = url.objects(originalURL = insertedURL).first()
            if dbContainURL is not None: 
                return render_template('MainHtml.html',short_url =request.host_url+dbContainURL.shortURL)
             
            
            if custom_id is not None:
                print('hello')
                dbContainshortID = url.objects(shortURL = custom_id).first()
                print('hello')
                if dbContainshortID is not None:
                    # i used short_url as error massege becuse of flash is not working 
                    #flash('Please enter different custom id!')
                    print('hello')
                    return render_template('MainHtml.html',short_url ='Please enter different custom id!')

                else:
                    custom_id = generate_short_id(insertedURL)
                    dbContainshortIDs = url.objects(shortURL = custom_id).first()[0:5]

                    while dbContainshortIDs :
                        custom_id =generate_short_id(custom_id+datetime.now)[0:5]
                        dbContainshortIDs = url.objects(shortURL = custom_id).first()
                        
                    urlone=url()
                    urlone.originalURL = insertedURL
                    urlone.shortURL = custom_id
                    urlone.save()
                    return render_template('MainHtml.html',short_url = request.host_url+urlone.shortURL)
            else :
                
                return render_template('MainHtml.html',short_url =request.host_url+dbContainURL.shortURL)
                
            
            
        else :
            return render_template('MainHtml.html')
    except:
        pass
    finally:
        if type(db)==MongoClient:
            db.close()

@app.route('/<short_id>')
def redirects(short_id):
    urlexist = url.objects(shortURL = short_id).first()
    if urlexist :
        return redirect(urlexist.originalURL)
    else :
        return '<h1>not valid short url<h1>'

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=5002 , debug=True)
