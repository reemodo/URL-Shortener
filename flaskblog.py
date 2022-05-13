

from random import choice
from flask import Flask, flash , redirect, request ,render_template 
from database.db import db
from database.url import url
import string
import hashlib , base64
db.initialize()
app = Flask(__name__)


def generate_short_id(longURL): 
    hashresult = hashlib.md5(longURL.encode())
    bytes = base64.b64encode(hashresult.digest()[0:6])
    return bytes.decode('utf-8')
  

@app.route('/',methods=['POST','GET'])
def main():
    if request.method == "POST" :
        insertedURL = request.form["url"]
        if not insertedURL:
            flash('The URL is required!')
            return render_template('MainHtml.html')

        short_id = request.form['custom_id']
        dbContainURL = url.objects(originalURL = insertedURL).first()

        if short_id and dbContainURL is not None:
            flash('Please enter different custom id!')
            return render_template('MainHtml.html')

        if dbContainURL == None:
            if not short_id:
                short_id = generate_short_id(insertedURL)
            urlone=url()
            urlone.originalURL = insertedURL
            urlone.shortURL = request.host_url+short_id
            urlone.save()

            return render_template('MainHtml.html',short_url = urlone.shortURL)
        else :
            return render_template('MainHtml.html',short_url =request.host_url+dbContainURL.shortURL)
            
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
    app.run(debug = True)
